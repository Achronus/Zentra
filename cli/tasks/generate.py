import ast
import typer

from cli.conf.checks import (
    CheckConfigFileValid,
    check_file_exists,
    check_folder_exists,
    check_zentra_exists,
)

from cli.conf.constants import CommonErrorCodes, GenerateErrorCodes
from cli.conf.extract import get_file_content
from cli.conf.storage import PathStorage
from cli.tasks.controllers.generate import GenerateController
from cli.utils.printables import component_count_panel

from rich.console import Console

console = Console()


class Generate:
    """A class for handling the logic for the `zentra generate` command."""

    def __init__(self, paths: PathStorage) -> None:
        self.paths = paths

    def init_checks(self) -> None:
        """Performs various checks to immediately provide feedback to the user regarding missing files."""
        if not check_folder_exists(self.paths.models):
            raise typer.Exit(code=CommonErrorCodes.MODELS_DIR_MISSING)

        if not check_file_exists(self.paths.config):
            raise typer.Exit(code=CommonErrorCodes.CONFIG_MISSING)

    def check_config_valid(self) -> None:
        """Checks if the config file is valid. Raises an error if False."""
        check_config = CheckConfigFileValid()
        file_content_tree = ast.parse(get_file_content(self.paths.config))
        check_config.visit(file_content_tree)

        valid_content = check_config.is_valid()

        if not valid_content:
            raise typer.Exit(code=CommonErrorCodes.INVALID_CONFIG)

    def create_components(self) -> None:
        """Generates the react components based on the `zentra/models` folder."""
        self.check_config_valid()
        zentra = check_zentra_exists()

        if len(zentra.component_names) == 0:
            raise typer.Exit(code=GenerateErrorCodes.NO_COMPONENTS)

        console.print(component_count_panel(zentra, text_start="Generating "))

        controller = GenerateController(zentra, self.paths)
        controller.run()
