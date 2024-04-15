import re
from typing import Any
import requests

from cli.conf.format import name_from_camel_case
from zentra.core import (
    LOWER_CAMELCASE_SINGLE_WORD,
    LOWER_CAMELCASE_WITH_DIGITS,
    LOWERCASE_SINGLE_WORD,
    Component,
    has_valid_pattern,
)
from zentra.core.enums.ui import (
    ButtonSize,
    ButtonVariant,
    ButtonIconPosition,
    IconButtonSize,
    InputOTPPatterns,
    InputTypes,
    ScrollType,
)
from zentra.ui import ShadcnUi

from pydantic import Field, HttpUrl, PrivateAttr, ValidationInfo, field_validator
from pydantic_core import PydanticCustomError


class Button(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Button component focusing on text.

    Parameters:
    - `text` (`string`) - the text displayed inside the button
    - `url` (`string, optional`) - the URL the button links to. `None` by default. When `None` removes it from `Button`
    - `variant` (`string, optional`) - the style of the button. Valid options: `['default', 'secondary', 'destructive', 'outline', 'ghost', 'link']`. `default` by default
    - `size` (`string, optional`) - the size of the button. Valid options: `['default', 'sm', 'lg']`. `default` by default
    - `disabled` (`boolean, optional`) - adds the disabled property, preventing it from being clicked. `False` by default
    """

    text: str = Field(min_length=1)
    url: HttpUrl = None
    variant: ButtonVariant = "default"
    size: ButtonSize = "default"
    disabled: bool = False


class IconButton(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Button component with a [Lucide React Icon](https://lucide.dev/icons).

    Parameters:
    - `icon` (`string`) - the name of the [Lucide React Icon](https://lucide.dev/icons) to add inside the button. Must be in React format (Capitalised camelCase). E.g., `CircleArrowDown` or `Loader`
    - `icon_position` (`string, optional`) - the position of the icon inside the button. When set to `start`, icon appears before the text. When `end`, it appears after the text. `start` by default. Valid options: `['start', 'end']`
    - `text` (`string, optional`) - the text displayed inside the button. `None` by default. When `None` removes it from `Button`
    - `url` (`string, optional`) - the URL the button links to. `None` by default. When `None` removes it from `Button`
    - `variant` (`string, optional`) - the style of the button. Valid options: `['default', 'secondary', 'destructive', 'outline', 'ghost', 'link']`. `default` by default
    - `size` (`string, optional`) - the size of the button. Valid options: `['default', 'sm', 'lg', 'icon']`. `icon` by default
    - `disabled` (`boolean, optional`) - adds the disabled property, preventing it from being clicked. `False` by default
    """

    icon: str = Field(min_length=1)
    icon_position: ButtonIconPosition = "start"
    text: str = None
    url: HttpUrl = Field(default=None)
    variant: ButtonVariant = "default"
    size: IconButtonSize = "icon"
    disabled: bool = False

    _classname = PrivateAttr(default="Button")

    @field_validator("icon")
    def validate_icon(cls, icon: str) -> str:
        icon_name = name_from_camel_case(icon)
        response = requests.get(f"https://lucide.dev/icons/{icon_name}")

        if response.status_code != 200:
            raise PydanticCustomError(
                "invalid_icon",
                f"'{icon}' at '{response.url}' does not exist",
                dict(wrong_value=icon, error_code=response.status_code),
            )

        return icon


class Calendar(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Calendar component.

    Parameters:
    - `name` (`string`) - an identifier for the component. Prepended to `get` and `set` for the `useState()` hook. Must be `lowercase` or `camelCase` and up to a maximum of `15` characters

    Example:
    1. `name='monthly'` ->
        `const [monthlyDate, monthlySetDate] = useState(new Date());"`
    2. `name='yearlyCalendar'` ->
        `const [yearlyCalendarDate, yearlyCalendarSetDate] = useState(new Date());"`
    """

    name: str = Field(min_length=1, max_length=15)

    @field_validator("name")
    def validate_id(cls, name: str) -> str:
        if not has_valid_pattern(pattern=LOWER_CAMELCASE_WITH_DIGITS, value=name):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                "must be lowercase or camelCase",
                dict(wrong_value=name, pattern=LOWER_CAMELCASE_WITH_DIGITS),
            )
        return name


class Checkbox(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Checkbox component.

    Parameters:
    - `id` (`string`) - an identifier for the component. Must be `lowercase` or `camelCase` and up to a maximum of `15` characters
    - `label` (`string`) - the text associated to the checkbox
    - `more_info` (`string, optional`) - additional information to add under the checkbox. `None` by default. When `None` removes it from `Checkbox`
    - `disabled` (`boolean, optional`) - adds the disabled property, preventing it from being selected. `False` by default
    """

    id: str = Field(min_length=1, max_length=15)
    label: str = Field(min_length=1)
    more_info: str = None
    disabled: bool = False

    @field_validator("id")
    def validate_id(cls, id: str) -> str:
        if not has_valid_pattern(pattern=LOWER_CAMELCASE_WITH_DIGITS, value=id):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                "must be lowercase or camelCase",
                dict(wrong_value=id, pattern=LOWER_CAMELCASE_WITH_DIGITS),
            )
        return id


class MultiCheckbox(Component, ShadcnUi):
    """
    A Zentra model for multiple [shadcn/ui](https://ui.shadcn.com/) Checkbox components.

    Parameters:
    - `items` (`list[Checkbox]`) - a list of Checkbox components. Requires a `minimum` of `2` items
    """

    items: list[Checkbox] = Field(min_length=2)

    _classname = PrivateAttr(default="Checkbox")

    # TODO: add logic specific to `Forms`


class Collapsible(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Collapsible component.

    Parameters:
    - `name` (`string`) - an identifier for the component. Prepended to `get` and `set` for the `useState()` hook. Must be `lowercase` or `camelCase` and up to a maximum of `15` characters
    - `title` (`string`) - the main heading of the collapsible
    - `items` (`list[str]`) - a list of strings representing the text to add into each collapsible block. Requires a `minimum` of `1` item
    """

    name: str = Field(min_length=1, max_length=15)
    title: str = Field(min_length=1)
    items: list[str] = Field(min_length=1)

    @field_validator("name")
    def validate_id(cls, name: str) -> str:
        if not has_valid_pattern(pattern=LOWER_CAMELCASE_WITH_DIGITS, value=name):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                "must be lowercase or camelCase",
                dict(wrong_value=name, pattern=LOWER_CAMELCASE_WITH_DIGITS),
            )
        return name


class Combobox(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Combobox component.

    Parameters:
    - `name` (`string`) - the name of the component
    """

    # TODO: come back once 'popover' and 'command' created


class DatePicker(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) DatePicker component.

    Parameters:
    - `name` (`string`) - the name of the component
    """

    # TODO: come back once 'popover' created


class Input(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Input component.

    Inputs are extremely versatile as expressed in the [HTML Input docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/url). We've limited the attributes to the basics for simplicity. Once components are generated, you can edit them in the respective `.tsx` files with additional attributes if needed.

    Parameters:
    - `id` (`string`) - an identifier for the component. Must be `lowercase` or `camelCase` and up to a maximum of `15` characters
    - `type` (`string`) - the type of input field. Options `['text', 'email', 'password', 'number', 'file', 'tel', 'search', 'url', 'color']`
    - `placeholder` (`string`) - the placeholder text for the input
    - `disabled` (`boolean, optional`) - adds the disabled property, preventing it from being selected. `False` by default
    """

    id: str = Field(min_length=1, max_length=15)
    type: InputTypes
    placeholder: str
    disabled: bool = False

    @field_validator("id")
    def validate_id(cls, id: str) -> str:
        if not has_valid_pattern(pattern=LOWER_CAMELCASE_WITH_DIGITS, value=id):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                "must be lowercase or camelCase",
                dict(wrong_value=id, pattern=LOWER_CAMELCASE_WITH_DIGITS),
            )
        return id


class InputOTP(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) InputOTP component.

    Parameters:
    - `num_inputs` (`int`) - the length of the OTP. E.g., 6 = 6 input slots. Must be a minimum of `1`
    - `num_groups` (`int, optional`) - the number of slot groups. E.g., `InputOTP(num_inputs=6, num_groups=2)` -> 2 groups of 3 input slots. `1` by default
    - `pattern` (`string, optional`) - a regex pattern to limit the OTP input values. Options include: `['digits_only', 'chars_only', 'digits_n_chars_only']` ([official patterns](https://github.com/guilhermerodz/input-otp/blob/master/packages/input-otp/src/regexp.ts)) or a `custom` variant. `None` by default

    Examples:
    1. A basic OTP without a pattern.
    ```python
    input = InputOTP(num_inputs=6, num_groups=2)
    ```
    into ->
    ```jsx
    import { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator } from '../ui/input-otp'

    <InputOTP maxLength={6}>
        <InputOTPGroup>
            <InputOTPSlot index={0} />
            <InputOTPSlot index={1} />
            <InputOTPSlot index={2} />
        </InputOTPGroup>
        <InputOTPSeparator />
        <InputOTPGroup>
            <InputOTPSlot index={3} />
            <InputOTPSlot index={4} />
            <InputOTPSlot index={5} />
        </InputOTPGroup>
    </InputOTP>
    ```

    2. A basic OTP with an official pattern and single group.
    ```python
    input = InputOTP(num_inputs=6, pattern='digits_only')
    ```
    into ->
    ```jsx
    import { InputOTP, InputOTPGroup, InputOTPSlot } from '../ui/input-otp'
    import { REGEXP_ONLY_DIGITS } from "input-otp"

    <InputOTP
        maxLength={6}
        pattern={REGEXP_ONLY_DIGITS}
    >
        <InputOTPGroup>
            <InputOTPSlot index={0} />
            <InputOTPSlot index={1} />
            <InputOTPSlot index={2} />
            <InputOTPSlot index={3} />
            <InputOTPSlot index={4} />
            <InputOTPSlot index={5} />
        </InputOTPGroup>
    </InputOTP>
    ```

    3. An OTP with a custom pattern and 3 groups.
    ```python
    input = InputOTP(num_inputs=6, num_groups=3, pattern=r"([\^$.|?*+()\[\]{}])")
    ```
    into ->
    ```jsx
    import { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator } from '../ui/input-otp'

    <InputOTP
        maxLength={6}
        pattern="([\^$.|?*+()\[\]{}])"
    >
        <InputOTPGroup>
            <InputOTPSlot index={0} />
            <InputOTPSlot index={1} />
        </InputOTPGroup>
        <InputOTPSeparator />
        <InputOTPGroup>
            <InputOTPSlot index={2} />
            <InputOTPSlot index={3} />
        </InputOTPGroup>
        <InputOTPSeparator />
        <InputOTPGroup>
            <InputOTPSlot index={4} />
            <InputOTPSlot index={5} />
        </InputOTPGroup>
    </InputOTP>
    ```
    """

    num_inputs: int = Field(ge=1)
    num_groups: int = Field(default=1, ge=1)
    pattern: InputOTPPatterns | str = None

    @field_validator("num_groups")
    def validate_num_groups(num_groups: int, info: ValidationInfo) -> int:
        num_inputs = info.data.get("num_inputs")
        if num_groups > num_inputs:
            raise PydanticCustomError(
                "size_out_of_bounds",
                f"cannot have more groups ({num_groups}) than input slots ({num_inputs})\n",
                dict(wrong_value=num_groups, input_size=num_inputs),
            )
        return num_groups

    @field_validator("pattern")
    def validate_pattern(pattern: str) -> str:
        if pattern not in InputOTPPatterns:
            try:
                re.compile(pattern)
            except re.error:
                official_patterns = [pattern.value for pattern in InputOTPPatterns]
                raise PydanticCustomError(
                    "invalid_regex_pattern",
                    f"must be an official pattern option ({official_patterns}) or a valid regex string\n",
                    dict(wrong_value=pattern, official_patterns=official_patterns),
                )
        return pattern


class Label(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Label component.

    Parameters:
    - `name` (`string`) - an identifier for the component. Must be `lowercase` or `camelCase` and up to a maximum of `15` characters
    - `text` (`string`) - the descriptive text to put into the label
    """

    name: str = Field(min_length=1, max_length=15)
    text: str = Field(min_length=1)

    @field_validator("name")
    def validate_id(cls, name: str) -> str:
        if not has_valid_pattern(pattern=LOWER_CAMELCASE_WITH_DIGITS, value=name):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                "must be lowercase or camelCase",
                dict(wrong_value=name, pattern=LOWER_CAMELCASE_WITH_DIGITS),
            )
        return name


class RadioButton(Component, ShadcnUi):
    """
    A helper Zentra model for the [shadcn/ui](https://ui.shadcn.com/) RadioGroup component. Cannot be used on its own, must be used inside a `RadioGroup`.

    Parameters:
    - `id` (`string`) - an identifier for the component. Must be `lowercase` or `camelCase` and up to a maximum of `15` characters
    - `value` (`string`) - the value for the radio button. Up to a maximum of `30` characters. Must be `lowercase` and a `single word`
    - `text` (`string`) - the text to display for the radio button
    """

    id: str = Field(min_length=1, max_length=15)
    value: str = Field(min_length=1, max_length=30)
    text: str = Field(min_length=1)

    @field_validator("id")
    def validate_id(cls, id: str) -> str:
        if not has_valid_pattern(pattern=LOWER_CAMELCASE_WITH_DIGITS, value=id):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                "must be lowercase or camelCase",
                dict(wrong_value=id, pattern=LOWER_CAMELCASE_WITH_DIGITS),
            )
        return id

    @field_validator("value")
    def validate_value(cls, value: str) -> str:
        if not has_valid_pattern(pattern=LOWERCASE_SINGLE_WORD, value=value):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                "must be lowercase and a single word",
                dict(wrong_value=value, pattern=LOWERCASE_SINGLE_WORD),
            )
        return value


class RadioGroup(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) RadioGroup component.

    Parameters:
    - `items` (`list[RadioButton]`) - a list of `zentra.control.RadioButton`
    - `default_value` (`string`) - the default value of the radio group. Must be a `value` assigned to a `RadioButton` in the `items` list. Must be `lowercase` and a `single word` and Up to a maximum of `30` characters
    """

    items: list[RadioButton]
    default_value: str = Field(min_length=1, max_length=30)

    @field_validator("items")
    def validate_items(cls, items: list[RadioButton]) -> list[RadioButton]:
        if not items or len(items) == 0:
            raise PydanticCustomError(
                "missing_radio_button",
                "must have at least one 'RadioButton'",
                dict(wrong_value=items),
            )
        return items

    @field_validator("default_value")
    def validate_default_value(cls, default_value: str, info: ValidationInfo) -> str:
        if not has_valid_pattern(pattern=LOWERCASE_SINGLE_WORD, value=default_value):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                "must be lowercase and a single word",
                dict(wrong_value=default_value, pattern=LOWERCASE_SINGLE_WORD),
            )

        present = False
        radio_buttons: list[RadioButton] = info.data.get("items")
        if radio_buttons:
            for rb in radio_buttons:
                if rb.value == default_value:
                    present = True
                    break

            if not present:
                raise PydanticCustomError(
                    "default_value_missing",
                    f"""'value="{default_value}"' missing from 'items'. Provided -> \n    '{radio_buttons}'\n""",
                    dict(wrong_value=default_value, items=radio_buttons),
                )

        return default_value


class ScrollArea(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) ScrollArea component.

    Parameters:
    - `core_content` (`string`) - the core content of the `ScrollArea`. If `data` is specified, applies it to the `map` function. Defined as a multi-line string that can be as basic as a string of text or a set of complicated `JSX`. Always required for the component. Remember to add existing Zentra components! Refer to the examples below for more info
    - `content_container_styles` (`string, optional`) - an optional set of class tags to apply to a `div` container around the content inside the `ScrollArea` component. If present, adds a `div` tag automatically with the styles. `None` by default
    - `content_above_core` (`string, optional`) - an optional JSX string added above the `core_content`. Useful when you want to add additional `JSX`, such as a header, above the `map` function. `None` by default
    - `content_below_core` (`string, optional`) -an optional JSX string added below the `core_content`. Useful when you want to add additional `JSX` below the `map` function. `None` by default
    - `data` (`tuple[string, string, list[dict[string, Any]]], optional`) - `None` by default. A tuple of the following items:
      1. The name of the `data` object. E.g., 'works'. Must be `lowercase` or `camelCase` and a maximum of `30` characters
      2. The map `parameter` name. E.g., 'artwork'. Must be `lowercase` or `camelCase` and a maximum of `30` characters
      3. A list of dictionaries of information to pass into the scroll area that is iterated over using a `map` function. Each dictionary must have the same key values and values of the same type
    - `scroll_type` (`string, optional`) - the scroll axis. Valid options: `[horizontal, vertical]`. `vertical` by default
    """

    core_content: str = Field(min_length=1)
    content_container_styles: str = None
    content_above_core: str = None
    content_below_core: str = None
    data: tuple[str, str, list[dict[str, Any]]] = None
    scroll_type: ScrollType = "vertical"

    @field_validator("data")
    def validate_data(
        cls, data: tuple[str, str, list[dict[str, Any]]]
    ) -> tuple[str, str, list[dict[str, Any]]]:
        if data:
            name, parameter, data_dict_list = data

            def string_pattern_match(value: str, idx: int) -> bool:
                result = has_valid_pattern(
                    pattern=LOWER_CAMELCASE_SINGLE_WORD, value=value
                )

                if not result and len(value) <= 30:
                    raise PydanticCustomError(
                        "string_pattern_mismatch",
                        f"position: {idx} -> '{value}'. Must be 'lowercase' or 'camelCase', a single word and a maximum of '30' characters\n",
                        dict(wrong_value=value, pattern=LOWER_CAMELCASE_SINGLE_WORD),
                    )

                return value

            name = string_pattern_match(value=name, idx=0)
            parameter = string_pattern_match(value=parameter, idx=1)

            if len(data_dict_list) == 0 or len(data_dict_list[0]) == 0:
                raise PydanticCustomError(
                    "missing_data",
                    "No data exists in the list",
                    dict(wrong_value=data_dict_list),
                )
            else:
                reference_dict = data_dict_list[0]
                for idx, d in enumerate(data_dict_list[1:], start=1):
                    if set(d.keys()) != set(reference_dict.keys()):
                        raise PydanticCustomError(
                            "invalid_dictionary_keys",
                            f"position: 2.{idx} -> '{d.keys()} != {reference_dict.keys()}'\n",
                            dict(wrong_value=d, full_data=data_dict_list),
                        )

                    for key, value in reference_dict.items():
                        if type(d[key]) != type(value):
                            raise PydanticCustomError(
                                "invalid_value_type",
                                f"position: 2.{idx} -> '{type(d[key])} ({d[key]}) != {type(value)} ({value})'\n",
                                dict(wrong_value=d, full_data=data_dict_list),
                            )

        return data


class Select(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Select component.

    Parameters:
    - `name` (`string`) - the name of the component
    """


class Slider(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Slider component.

    Parameters:
    - `name` (`string`) - the name of the component
    """


class Switch(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Switch component.

    Parameters:
    - `disabled` (`boolean, optional`) - a flag for disabling the switch component. Default is `False`
    - `read_only` (`boolean, optional`) - a flag for making the switch read only. Default is `False`. Indicates that the element is not editable, but is otherwise operable. More information on [Read only](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-readonly)
    """

    disabled: bool = False
    read_only: bool = False


class Tabs(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Tabs component.

    Parameters:
    - `name` (`string`) - the name of the component
    """


class Textarea(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Textarea component.

    Parameters:
    - `name` (`string`) - the name of the component
    """


class Toggle(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) Toggle component.

    Parameters:
    - `name` (`string`) - the name of the component
    """


class ToggleGroup(Component, ShadcnUi):
    """
    A Zentra model for the [shadcn/ui](https://ui.shadcn.com/) ToggleGroup component.

    Parameters:
    - `name` (`string`) - the name of the component
    """
