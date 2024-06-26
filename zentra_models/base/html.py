from typing import Optional

from pydantic import PrivateAttr

from zentra_models.base import ZentraModel
from zentra_models.base.library import HTML


class HTMLTag(ZentraModel, HTML):
    """
    A parent model for all HTML tags.

    Parameters:
    - `styles` (`string, optional`) - a set of custom CSS classes to apply to the tag. Automatically adds them to `className`. `None` by default
    """

    styles: Optional[str] = None

    _no_container = PrivateAttr(default=True)

    @property
    def classname(self) -> str:
        """Stores the classname for the JSX builder."""
        return self.__class__.__name__.lower()
