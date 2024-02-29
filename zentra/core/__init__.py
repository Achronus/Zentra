from pydantic import BaseModel


class Component(BaseModel):
    """
    A Zentra model for all React components.

    Parameters:
    - name (str) - the name of the component.
    """

    name: str


class Page(BaseModel):
    """A Zentra model for a single webpage of React components."""

    components: list[Component]


class Icon(BaseModel):
    """A Zentra model for [Radix Ui Icons](https://www.radix-ui.com/icons)."""

    name: str
