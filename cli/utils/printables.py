from enum import Enum
from functools import partial
import textwrap

from cli.conf.constants import MAGIC
from cli.conf.checks import check_zentra_exists
from cli.conf.format import list_to_str, set_colour, name_to_plural, to_cc_from_pairs
from cli.conf.message import SETUP_COMPLETE_MSG
from cli.conf.storage import BasicNameStorage, ModelStorage

from pydantic import BaseModel
from rich.panel import Panel

from cli.conf.types import GenerateDataTuple


class Action(Enum):
    ADD = ("+", "green")
    REMOVE = ("-", "red")


class SetupPanelFormatter(BaseModel):
    """Handles the logic for creating completion panels for `zentra init`.

    Parameters:
    - storage (storage.BasicNameStorage) - the storage container with Zentra model names
    - action (Enum.Action) - a single Action Enum item to indicate an addition or subtraction string
    """

    storage: BasicNameStorage
    action: Action

    def title_str(
        self,
        name: str,
        title_colour: str,
        count: int,
    ) -> str:
        """Creates a title string for a set of models with the number of items at the front."""
        count_str = set_colour(count, self.action.value[1])
        formatted_name = set_colour(
            name_to_plural(name.capitalize(), count),
            title_colour,
        )
        return f"{count_str} {formatted_name}"


class GeneratePanelFormatter(BaseModel):
    """Handles the logic for creating completion panels for `zentra generate`.

    Parameters:
    - name (str) - a name to associate the formatter used in the title string (e.g., 'component' or 'page')
    - actions (Enum.Action) - an Action Enum class with an addition and subtraction value
    - storage (storage.ModelStorage) - the storage container with Zentra model names
    - data (GenerateDataTuple) - a tuple containing two lists of item information, one for addition and one for subtraction
    """

    name: str
    actions: type[Action]
    storage: ModelStorage
    data: GenerateDataTuple

    def data_str(self) -> str:
        """Creates a detailed string of information."""
        data_str = ""
        for item, action in zip(self.data, self.actions):
            data_str += f"{list_to_str(item, action)}\n"
        return data_str.rstrip()

    def title_str(self, counts: tuple[int, int], colour: str) -> str:
        """Creates a title string with the item name and its data counts."""
        count_str = ""
        headings = ("Added", "Removed")
        for count, heading, action in zip(counts, headings, self.actions):
            head_str = f"{count} {heading}"
            count_str += f"{set_colour(head_str, action.value[1])}, "

        formatted_name = set_colour(
            name_to_plural(self.name.capitalize(), sum(counts)),
            colour,
        )
        return f"{formatted_name} ({count_str.rstrip(', ')})"


def setup_first_run_panel() -> Panel:
    """Creates a printable panel after successfully running `zentra init` for the first time."""
    return Panel.fit(
        textwrap.dedent(f"""
    {MAGIC} [magenta]Zentra[/magenta] configured successfully! {MAGIC}
    """)
        + SETUP_COMPLETE_MSG,
        border_style="bright_green",
    )


def setup_complete_panel() -> Panel:
    """Creates a printable panel after successfully completing `zentra init`."""
    zentra = check_zentra_exists()
    storage = zentra.names
    add_formatter = SetupPanelFormatter(storage=storage, action=Action.ADD)

    component_str = list_to_str(storage.components, action=Action.ADD)
    page_str = list_to_str(storage.pages, action=Action.ADD)

    component_title = add_formatter.title_str(
        "component", "yellow", len(storage.components)
    )
    page_title = add_formatter.title_str("page", "dark_goldenrod", len(storage.pages))

    return Panel.fit(
        textwrap.dedent(f"""
    {MAGIC} [magenta]Zentra[/magenta] configured successfully! {MAGIC}

    Use [green]zentra generate[/green] to create your models.

    [bright_cyan]Models To Generate[/bright_cyan]
    """)
        + f"{component_title}\n{component_str}\n\n"
        + f"{page_title}\n{page_str}",
        border_style="bright_green",
    )


def generate_complete_panel(storage: ModelStorage) -> Panel:
    """Creates a printable panel after successfully completing `zentra generate`."""
    components = (
        to_cc_from_pairs(storage.components.generate),
        to_cc_from_pairs(storage.components.remove),
    )
    pages = (
        to_cc_from_pairs(storage.pages.generate),
        to_cc_from_pairs(storage.pages.remove),
    )

    formatter = partial(GeneratePanelFormatter, actions=Action, storage=storage)
    comp_formatter = formatter(name="component", data=components)
    page_formatter = formatter(name="page", data=pages)

    comp_totals = (
        storage.components.counts.generate,
        storage.components.counts.remove,
    )
    page_totals = (
        storage.pages.counts.generate,
        storage.pages.counts.remove,
    )

    comp_str = comp_formatter.data_str()
    page_str = page_formatter.data_str()

    component_title = comp_formatter.title_str(comp_totals, "yellow")
    page_title = page_formatter.title_str(page_totals, "dark_goldenrod")

    page_str = f"\n{page_title}\n{page_str}" if page_str.strip() != "" else ""

    return Panel.fit(
        textwrap.dedent(f"""
    {MAGIC} [magenta]Zentra[/magenta] → [bright_cyan]React[/bright_cyan] conversion successful! {MAGIC}
    
    Access them in [magenta]zentra/generated[/magenta].
    
    [bright_cyan]Model Updates[/bright_cyan]
    """)
        + f"{component_title}\n{comp_str}"
        + page_str,
        border_style="bright_green",
    )
