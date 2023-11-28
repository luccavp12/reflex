"""Stub file for reflex/components/forms/pininput.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Optional, Union
from reflex.components.component import Component
from reflex.components.libs.chakra import ChakraComponent, LiteralInputVariant
from reflex.components.tags.tag import Tag
from reflex.constants import EventTriggers
from reflex.utils import format
from reflex.utils.imports import ImportDict, merge_imports
from reflex.vars import Var

class PinInput(ChakraComponent):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    def get_ref(self) -> str | None: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        value: Optional[Union[Var[str], str]] = None,
        auto_focus: Optional[Union[Var[bool], bool]] = None,
        default_value: Optional[Union[Var[str], str]] = None,
        error_border_color: Optional[Union[Var[str], str]] = None,
        focus_border_color: Optional[Union[Var[str], str]] = None,
        id_: Optional[Union[Var[str], str]] = None,
        length: Optional[Union[Var[int], int]] = None,
        is_disabled: Optional[Union[Var[bool], bool]] = None,
        is_invalid: Optional[Union[Var[bool], bool]] = None,
        manage_focus: Optional[Union[Var[bool], bool]] = None,
        mask: Optional[Union[Var[bool], bool]] = None,
        placeholder: Optional[Union[Var[str], str]] = None,
        type_: Optional[Union[Var[str], str]] = None,
        variant: Optional[
            Union[
                Var[Literal["outline", "filled", "flushed", "unstyled"]],
                Literal["outline", "filled", "flushed", "unstyled"],
            ]
        ] = None,
        name: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_change: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_complete: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "PinInput":
        """Create a pin input component.

        If no children are passed in, the component will create a default pin input
        based on the length prop.

        Args:
            *children: The children of the component.
            value: State var to bind the the input.
            auto_focus: If true, the pin input receives focus on mount
            default_value: The default value of the pin input
            error_border_color: The border color when the input is invalid.
            focus_border_color: The border color when the input is focused.
            id_: The top-level id string that will be applied to the input fields. The index of the input will be appended to this top-level id.
            length: The length of the number input.
            is_disabled: If true, the pin input component is put in the disabled state
            is_invalid: If true, the pin input component is put in the invalid state
            manage_focus: If true, focus will move automatically to the next input once filled
            mask: If true, the input's value will be masked just like `type=password`
            placeholder: The placeholder for the pin input
            type_: The type of values the pin-input should allow ("number" | "alphanumeric").
            variant: "outline" | "flushed" | "filled" | "unstyled"
            name: The name of the form field
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The pin input component.
        """
        ...

class PinInputField(ChakraComponent):
    @classmethod
    def for_length(cls, length: Var | int, **props) -> Var: ...
    def get_ref(self): ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        index: Optional[Var[int]] = None,
        name: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "PinInputField":
        """Create the component.

        Args:
            *children: The children of the component.
            index: the position of the PinInputField inside the PinInput.  Default to None because it is assigned by PinInput when created.
            name: The name of the form field
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
