"""Runs the benchmarks and inserts the results into the database."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime

import psycopg2


def extract_stats_from_json(json_file: str) -> list[dict]:
    """Extracts the stats from the JSON data and returns them as a list of dictionaries.

    Args:
        json_file: The JSON file to extract the stats data from.

    Returns:
        list[dict]: The stats for each test.
    """
    with open(json_file, "r") as file:
        json_data = json.load(file)

    # Load the JSON data if it is a string, otherwise assume it's already a dictionary
    data = json.loads(json_data) if isinstance(json_data, str) else json_data

    # Initialize an empty list to store the stats for each test
    test_stats = []

    # Iterate over each test in the 'benchmarks' list
    for test in data.get("benchmarks", []):
        group = test.get("group", None)
        stats = test.get("stats", {})
        full_name = test.get("fullname")
        file_name = (
            full_name.split("/")[-1].split("::")[0].strip(".py") if full_name else None
        )
        test_name = test.get("name", "Unknown Test")

        test_stats.append(
            {
                "test_name": test_name,
                "group": group,
                "stats": stats,
                "full_name": full_name,
                "file_name": file_name,
            }
        )
    return test_stats


def insert_benchmarking_data(
    db_connection_url: str,
    os_type_version: str,
    python_version: str,
    performance_data: list[dict],
    commit_sha: str,
    pr_title: str,
    branch_name: str,
    event_type: str,
    actor: str,
    pr_id: str,
):
    """Insert the benchmarking data into the database.

    Args:
        db_connection_url: The URL to connect to the database.
        os_type_version: The OS type and version to insert.
        python_version: The Python version to insert.
        performance_data: The performance data of reflex web to insert.
        commit_sha: The commit SHA to insert.
        pr_title: The PR title to insert.
        branch_name: The name of the branch.
        event_type: Type of github event(push, pull request, etc)
        actor: Username of the user that triggered the run.
        pr_id: Id of the PR.
    """
    # Serialize the JSON data
    simple_app_performance_json = json.dumps(performance_data)

    # Get the current timestamp
    current_timestamp = datetime.now()

    # Connect to the database and insert the data
    with psycopg2.connect(db_connection_url) as conn, conn.cursor() as cursor:
        insert_query = """
            INSERT INTO simple_app_benchmarks (os, python_version, commit_sha, time, pr_title, branch_name, event_type, actor, performance, pr_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
        cursor.execute(
            insert_query,
            (
                os_type_version,
                python_version,
                commit_sha,
                current_timestamp,
                pr_title,
                branch_name,
                event_type,
                actor,
                simple_app_performance_json,
                pr_id,
            ),
        )
        # Commit the transaction
        conn.commit()


def main():
    """Runs the benchmarks and inserts the results."""
    # Get the commit SHA and JSON directory from the command line arguments
    parser = argparse.ArgumentParser(description="Run benchmarks and process results.")
    parser.add_argument(
        "--os", help="The OS type and version to insert into the database."
    )
    parser.add_argument(
        "--python-version", help="The Python version to insert into the database."
    )
    parser.add_argument(
        "--commit-sha", help="The commit SHA to insert into the database."
    )
    parser.add_argument(
        "--benchmark-json",
        help="The JSON file containing the benchmark results.",
    )
    parser.add_argument(
        "--db-url",
        help="The URL to connect to the database.",
        required=True,
    )
    parser.add_argument(
        "--pr-title",
        help="The PR title to insert into the database.",
    )
    parser.add_argument(
        "--branch-name",
        help="The current branch",
        required=True,
    )
    parser.add_argument(
        "--event-type",
        help="The github event type",
        required=True,
    )
    parser.add_argument(
        "--actor",
        help="Username of the user that triggered the run.",
        required=True,
    )
    parser.add_argument(
        "--pr-id",
        help="ID of the PR.",
        required=True,
    )
    args = parser.parse_args()

    # Get the PR title from env or the args. For the PR merge or push event, there is no PR title, leaving it empty.
    pr_title = args.pr_title or os.getenv("PR_TITLE", "")

    # Get the results of pytest benchmarks
    cleaned_benchmark_results = extract_stats_from_json(args.benchmark_json)
    # Insert the data into the database
    insert_benchmarking_data(
        db_connection_url=args.db_url,
        os_type_version=args.os,
        python_version=args.python_version,
        performance_data=cleaned_benchmark_results,
        commit_sha=args.commit_sha,
        pr_title=pr_title,
        branch_name=args.branch_name,
        event_type=args.event_type,
        actor=args.actor,
        pr_id=args.pr_id,
    )


if __name__ == "__main__":
    main()
