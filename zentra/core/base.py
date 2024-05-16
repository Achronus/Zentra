from typing import Optional
from pydantic import BaseModel, ConfigDict, field_validator, Field
from pydantic_core import PydanticCustomError

from zentra.core import LOWER_CAMELCASE_SINGLE_WORD, has_valid_pattern


class HTMLTag(BaseModel):
    """
    A parent model for all HTML tags.

    Parameters:
    - `styles` (`string, optional`) - a set of custom CSS classes to apply to the tag. Automatically adds them to `className`. `None` by default
    """

    styles: Optional[str] = None

    model_config = ConfigDict(use_enum_values=True)

    @property
    def classname(self) -> str:
        """Stores the classname for the JSX builder."""
        return self.__class__.__name__.lower()

    @property
    def custom_common_content(self) -> list[str]:
        """Returns a list of the content that use the same name as a common content, but act differently with this specific model."""
        return []


class JSIterable(BaseModel):
    """
    A parent model for all JavaScript iterable functions.

    - `obj_name` (`string`) - the name of the data object array to iterate over. Must be `lowercase` or `camelCase`, a `single word`, and up to a maximum of `20` characters
    - `param_name` (`string`) - the name of the parameter to iterate over inside the map. Must be `lowercase` or `camelCase`, a `single word`, and up to a maximum of `20` characters
    """

    obj_name: str = Field(min_length=1, max_length=20)
    param_name: str = Field(min_length=1, max_length=20)

    model_config = ConfigDict(use_enum_values=True)

    @property
    def classname(self) -> str:
        """Stores the classname for the JSX builder."""
        return self.__class__.__name__.lower()

    @field_validator("obj_name", "param_name")
    def validate_name(cls, v: str) -> str:
        result = has_valid_pattern(pattern=LOWER_CAMELCASE_SINGLE_WORD, value=v)

        if not result:
            raise PydanticCustomError(
                "string_pattern_mismatch",
                f"'{v}'. Must be 'lowercase' or 'camelCase', a single word and a maximum of '20' characters\n",
                dict(wrong_value=v, pattern=LOWER_CAMELCASE_SINGLE_WORD),
            )

        return v
