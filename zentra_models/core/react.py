from typing import Optional

from pydantic import Field, PrivateAttr, field_validator

from zentra_models.base import ZentraModel
from zentra_models.base.library import Lucide
from zentra_models.core.enums.ui import ButtonIconPosition
from zentra_models.core.html import HTMLContent
from zentra_models.core.utils import name_to_pascal_case
from zentra_models.core.validation import icon_name_validation


class LucideIcon(ZentraModel, Lucide):
    """
    A Zentra model dedicated to [Lucide React Icons](https://lucide.dev/icons) based on the [Lucide React Package](https://lucide.dev/guide/packages/lucide-react).

    Parameters:
    - `name` (`string`) - the name of the [Lucide React Icon](https://lucide.dev/icons). Must be in kebab-case format. E.g., `circle-arrow-down` or `loader`
    - `text` (`string | zentra.models.core.html.HTMLContent, optional`) - the text displayed alongside the icon. `None` by default. Can be either:
      1. A string of text. Can include parameter variables (indicated by starting the variable name with a `$.`)
      2. A `HTMLContent` model, such as a HTML `span` tag
    - `styles` (`string, optional`) - a set of custom CSS classes to apply to the icon. Automatically adds them to `className`. `mr-2 h-4 w-4` by default
    - `size` (`integer, optional`) - a custom size for the icon. `None` by default
    - `color` (`string, optional`) - a custom colour for the icon. `None` by default
    - `stroke_width` (`integer, optional`) - a custom stroke width for the icon. `None` by default

    """

    name: str = Field(min_length=1)
    text: Optional[str | HTMLContent] = None
    styles: Optional[str] = "mr-2 h-4 w-4"
    size: Optional[int] = None
    color: Optional[str] = None
    stroke_width: Optional[int] = None

    _content_attr = PrivateAttr(default="text")
    _custom_common_attrs = PrivateAttr(default=["name"])

    @property
    def container_name(self) -> str:
        return name_to_pascal_case(self.name, char="-")

    @field_validator("name")
    def validate_name(cls, name: str) -> str:
        return icon_name_validation(name)

    @property
    def import_str(self) -> str:
        """Returns the core import string for the icon."""
        return "import { " + self.name + ' } from "lucide-react"'

    @property
    def content_str(self) -> str:
        """Returns the primary content string for the icon."""
        return f'<{self.name} className="{self.styles}" />'


class LucideIconWithText(LucideIcon):
    """
    A Zentra model dedicated to [Lucide React Icons](https://lucide.dev/icons) with text, based on the [Lucide React Package](https://lucide.dev/guide/packages/lucide-react).

    Parameters:
    - `name` (`string`) - the name of the [Lucide React Icon](https://lucide.dev/icons). Must be in kebab-case format. E.g., `circle-arrow-down` or `loader`
    - `position` (`string, optional`) - the position of the icon. When set to `start`, icon appears before a components text. When `end`, it appears after the text.  Valid options: `['start', 'end']`. `start` by default
    - `text` (`string, optional`) - the text displayed alongside the icon. Can include parameter variables (indicated by starting the variable name with a `$.`). `None` by default
    - `styles` (`string, optional`) - a set of custom CSS classes to apply to the icon. Automatically adds them to `className`. `mr-2 h-4 w-4` by default
    - `size` (`integer, optional`) - a custom size for the icon. `None` by default
    - `color` (`string, optional`) - a custom colour for the icon. `None` by default
    - `stroke_width` (`integer, optional`) - a custom stroke width for the icon. `None` by default
    """

    position: ButtonIconPosition = "start"
    text: Optional[str] = None
