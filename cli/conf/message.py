from enum import Enum
import textwrap
import typer

from rich.console import Console
from rich.panel import Panel


from cli.conf.constants import (
    CONFIG_URL,
    ERROR_GUIDE_URL,
    GETTING_STARTED_URL,
    GITHUB_ISSUES_URL,
    MAGIC,
    FAIL,
    MODELS_FILEPATH,
    CommonErrorCodes,
    GenerateSuccessCodes,
    SetupErrorCodes,
    GenerateErrorCodes,
    SetupSuccessCodes,
)


MORE_HELP_INFO = f"""
[dark_goldenrod]Need more help?[/dark_goldenrod] 
  Check our [bright_blue][link={ERROR_GUIDE_URL}]Error Message Guide[/link][/bright_blue].

[red]Really stuck?[/red] 
  Report the issue [bright_blue][link={GITHUB_ISSUES_URL}]on GitHub[/link][/bright_blue].
"""

UNKNOWN_ERROR = f"""
{FAIL} 🥴 Well this is awkward... We didn't account for this! 🥴 {FAIL}

You've encountered something unexpected 🤯. Please report this issue on [bright_blue][link={GITHUB_ISSUES_URL}]GitHub[/link][/bright_blue].
"""

COMPONENTS_EXIST_MSG = """
[dark_goldenrod]Next Steps[/dark_goldenrod]
  1. [yellow]Move[/yellow] your [magenta]zentra/generated[/magenta] components
  2. Or, [green]add[/green] new ones to [magenta]zentra/models[/magenta]
"""


MISSING_FILES_CHECKS = """
Things to check:
  1. You are in the [yellow]correct directory[/yellow]
  2. You have [yellow]configured[/yellow] your project with [green]zentra init[/green]  
"""

CONFIG_URL_STR = f"[yellow][link={CONFIG_URL}]config[/link][/yellow]"
ACCESS_CONFIG_STR = f"\nAccess the {CONFIG_URL_STR} file.\n"

INVALID_CONFIG_CHECKS = (
    ACCESS_CONFIG_STR
    + """
Then, check if:
  1. [magenta]zentra[/magenta] = [yellow]Zentra[/yellow]() is initalised
  2. [magenta]Zentra[/magenta] models are registered with [magenta]zentra[/magenta].[yellow]register[/yellow]() with   
    a list of [magenta]Zentra[/magenta] [yellow]Pages[/yellow] or [yellow]Components[/yellow]

For example:
  [magenta]zentra[/magenta].[yellow]register[/yellow]([cyan][[/cyan][yellow]Page[/yellow](...), [yellow]Page[/yellow](...)[cyan]][/cyan])
  [magenta]zentra[/magenta].[yellow]register[/yellow]([cyan][[/cyan][yellow]Accordion[/yellow](...), [yellow]Button[/yellow](...)[cyan]][/cyan])
  [magenta]zentra[/magenta].[yellow]register[/yellow]([cyan][[/cyan][yellow]Page[/yellow](...), [yellow]Accordion[/yellow](...)[cyan]][/cyan])
"""
)

VALID_CONFIG_NO_COMPONENTS = (
    ACCESS_CONFIG_STR
    + """
Then, check if:
  1. You've [magenta]imported[/magenta] your created models
  2. You've [green]added[/green] them to [magenta]zentra[/magenta].[yellow]register[/yellow]()
"""
)

IMPORT_ERROR_CHECKS = (
    ACCESS_CONFIG_STR
    + """
Then, check if:
  1. You've [magenta]imported[/magenta] your created models
  2. [magenta]from[/magenta] [green]zentra[/green].[green]core[/green] [magenta]import[/magenta] [green]Zentra[/green] - is present
  3. [magenta]zentra[/magenta] = [yellow]Zentra[/yellow]() - is set
"""
)

BUG_MSG = f"""
This is a bug, please report this as an issue [bright_blue][link={GITHUB_ISSUES_URL}]on GitHub[/link][/bright_blue].
"""

SETUP_COMPLETE_MSG = f"""
[yellow]Next Steps[/yellow]
  1. Create your models in the {MODELS_FILEPATH} folder
  2. Then, add your models to the {CONFIG_URL_STR} file

[dark_goldenrod]Need help?[/dark_goldenrod]
Check our [bright_blue][link={GETTING_STARTED_URL}]Getting Started Guide[/link][/bright_blue]!
"""


def error_msg_with_checks(title: str, checks: str) -> str:
    """Formats error messages that have a title and a list of checks."""
    return textwrap.dedent(f"\n{FAIL} {title} {FAIL}\n") + checks


def success_msg_with_checks(title: str, checks: str, icon: str = MAGIC) -> str:
    """Formats success messages that have a title and a list of checks."""
    return textwrap.dedent(f"\n{icon} {title} {icon}\n") + checks


SUCCESS_MSG_MAP = {
    SetupSuccessCodes.COMPLETE: "",
    SetupSuccessCodes.ALREADY_CONFIGURED: "",
    GenerateSuccessCodes.COMPLETE: "",
    GenerateSuccessCodes.NO_NEW_COMPONENTS: success_msg_with_checks(
        "No new [yellow]Components[/yellow] or [yellow]Pages[/yellow] to add!",
        checks=COMPONENTS_EXIST_MSG,
    ),
}


COMMON_ERROR_MAP = {
    CommonErrorCodes.TEST_ERROR: "Test",
    CommonErrorCodes.CONFIG_MISSING: error_msg_with_checks(
        f"{MODELS_FILEPATH} [yellow]config[/yellow] file [red]missing[/red]!",
        checks=MISSING_FILES_CHECKS,
    ),
    CommonErrorCodes.INVALID_CONFIG: error_msg_with_checks(
        "[red]Invalid[/red] [yellow]config[/yellow] file [green]detected[/green]!",
        checks=INVALID_CONFIG_CHECKS,
    ),
    CommonErrorCodes.CONFIG_EMPTY: error_msg_with_checks(
        "[yellow]Config[/yellow] file is [red]empty[/red]!",
        checks="\nRun [green]zentra init[/green] to get started!\n",
    ),
    CommonErrorCodes.ZENTRA_MISSING: error_msg_with_checks(
        title="The [magenta]zentra[/magenta] folder is [red]missing[/red]!",
        checks=MISSING_FILES_CHECKS,
    ),
    CommonErrorCodes.MODELS_DIR_MISSING: error_msg_with_checks(
        f"{MODELS_FILEPATH} is missing!",
        checks=MISSING_FILES_CHECKS,
    ),
}

SETUP_ERROR_MAP = {
    SetupErrorCodes.NO_COMPONENTS: error_msg_with_checks(
        "Config [green]valid[/green] but [red]no components found[/red]!",
        checks=VALID_CONFIG_NO_COMPONENTS,
    ),
    SetupErrorCodes.IMPORT_ERROR: error_msg_with_checks(
        "[red]Cannot[/red] find or access the [magenta]Zentra[/magenta] app!",
        checks=IMPORT_ERROR_CHECKS,
    ),
}

GENERATE_ERROR_MAP = {
    GenerateErrorCodes.NO_COMPONENTS: error_msg_with_checks(
        "[red]No components found[/red] in [yellow]config[/yellow] file!",
        checks=INVALID_CONFIG_CHECKS,
    ),
    GenerateErrorCodes.GENERATE_DIR_MISSING: error_msg_with_checks(
        title="The [magenta]zentra/generated[/magenta] folder is [red]missing[/red]!",
        checks=BUG_MSG,
    ),
}

MSG_MAPPER = {
    **SUCCESS_MSG_MAP,
    **COMMON_ERROR_MAP,
    **SETUP_ERROR_MAP,
    **GENERATE_ERROR_MAP,
}


class MessageHandler:
    """Handles all the messages of the CLI."""

    def __init__(self, console: Console, msg_mapper: dict[Enum, str]) -> None:
        self.console = console
        self.msg_mapper = msg_mapper

    @staticmethod
    def __error_msg(msg: str, e: typer.Exit) -> Panel:
        """Handles error messages and returns a panel with their information."""
        err_str = "[cyan]Error code[/cyan]"
        error_code = f"\n{err_str}: {e.exit_code.value}\n"

        return Panel(
            msg + MORE_HELP_INFO + error_code,
            expand=False,
            border_style="bright_red",
        )

    @staticmethod
    def __success_msg(msg: str, e: typer.Exit) -> Panel:
        """Handles success messages and returns a panel with their information."""
        if msg != "":
            return Panel(msg, expand=False, border_style="bright_green")
        else:
            return ""

    def msg(self, e: typer.Exit) -> None:
        """Assigns a success or error message depending on the code received."""
        try:
            msg = textwrap.dedent(self.msg_mapper.get(e.exit_code, UNKNOWN_ERROR))
        except AttributeError:
            e.exit_code = CommonErrorCodes.UNKNOWN_ERROR

        msg_type = e.exit_code.__class__.__name__

        panel = (
            self.__error_msg(msg, e)
            if "Error" in msg_type
            else self.__success_msg(msg, e)
        )

        self.console.print(panel)
