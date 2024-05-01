from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError
import requests

from cli.conf.format import name_from_camel_case
from zentra.core.enums.ui import ButtonIconPosition


class LucideIcon(BaseModel):
    """
    A Zentra model dedicated to [Lucide React Icons](https://lucide.dev/icons).

    Parameters:
    - `name` (`string`) - the name of the [Lucide React Icon](https://lucide.dev/icons). Must be in React format (Capitalised camelCase). E.g., `CircleArrowDown` or `Loader`
    - `position` (`string, optional`) - the position of the icon. When set to `start`, icon appears before a components text. When `end`, it appears after the text.  Valid options: `['start', 'end']`. `start` by default
    - `text` (`string, optional`) - the text displayed alongside the icon. Can include parameter variables (indicated by starting the variable name with a `$`). `None` by default
    """

    name: str = Field(min_length=1)
    position: ButtonIconPosition = "start"
    text: str = None

    @field_validator("name")
    def validate_name(cls, name: str) -> str:
        icon_name = name_from_camel_case(name)
        response = requests.get(f"https://lucide.dev/icons/{icon_name}")

        if response.status_code != 200:
            raise PydanticCustomError(
                "invalid_icon",
                f"'{name}' at '{response.url}' does not exist",
                dict(wrong_value=name, error_code=response.status_code),
            )

        return name

    @property
    def import_str(self) -> str:
        """Returns the core import string for the icon."""
        return "import { " + self.name + ' } from "lucide-react"'
