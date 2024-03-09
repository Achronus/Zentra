import ast
import typer
from pydantic import BaseModel

from cli.conf.checks import (
    CheckConfigFileValid,
    check_file_exists,
    check_folder_exists,
    check_models_registered,
)
from cli.conf.format import name_from_camel_case
from cli.conf.move import copy_zentra_files
from cli.tasks.controllers.base import BaseController, PathStorage, status
from cli.conf.constants import (
    LocalUIComponentFilepaths,
    LocalUploadthingFilepaths,
    CommonErrorCodes,
)
from cli.conf.extract import get_file_content, get_filenames_in_subdir

from zentra.core import Zentra

# TODO: add --nextjs flag
NEXTJS_PROJECT = False


class NameStorage(BaseModel):
    """A storage container for Zentra model filenames."""

    UI_BASE: list[str] = get_filenames_in_subdir(LocalUIComponentFilepaths.BASE)
    UI_TO_GENERATE: list[str] = []

    UPLOADTHING: list[str] = get_filenames_in_subdir(
        LocalUploadthingFilepaths.BASE_NEXTJS
        if NEXTJS_PROJECT
        else LocalUploadthingFilepaths.BASE_BASIC
    )
    UT_TO_GENERATE: list[str] = []


class GenerateController(BaseController):
    """
    A controller for handling tasks that generate the Zentra components.

    Parameters:
    - zentra (zentra.core.Zentra) - the Zentra application containing components to generate
    """

    def __init__(self, zentra: Zentra, paths: PathStorage) -> None:
        react_str = "[cyan]React[/cyan]"
        zentra_str = "[magenta]Zentra[/magenta]"

        tasks = [
            (self.check_config, f"Checking {zentra_str} configured correctly"),
            (self.extract_models, f"Retrieving {zentra_str} models"),
            (self.create_files, f"Creating {react_str} component files"),
            (self.update_template_files, f"Configuring {react_str} components"),
        ]

        super().__init__(tasks)

        self.storage = NameStorage()
        self.paths = paths
        self.zentra = zentra

    @staticmethod
    def _model_folder_exists(filepath: str) -> None:
        """Helper function to check if the model folder exists. Raises an error if False."""
        if not check_folder_exists(filepath):
            raise typer.Exit(code=CommonErrorCodes.MODELS_DIR_MISSING)

    @staticmethod
    def _config_file_exists(filepath: str) -> None:
        """Helper function to check if the config file exists. Raises an error if False."""
        if not check_file_exists(filepath):
            raise typer.Exit(code=CommonErrorCodes.CONFIG_MISSING)

    @staticmethod
    def _config_file_valid(filepath: str) -> None:
        """A helper function to check if the config file is valid. Raises an error if False."""
        check_config = CheckConfigFileValid()
        file_content_tree = ast.parse(get_file_content(filepath))
        check_config.visit(file_content_tree)

        valid_content = check_config.is_valid()

        if not valid_content:
            raise typer.Exit(code=CommonErrorCodes.INVALID_CONFIG)

    @status
    def check_config(self) -> None:
        """Checks that the config files are setup correctly. Raises errors if files exist."""
        self._model_folder_exists(self.paths.models)
        self._config_file_exists(self.paths.config)
        self._config_file_valid(self.paths.config)

    @status
    def extract_models(self) -> None:
        """Extracts the Zentra models and prepares them for file generation."""
        formatted_names = [
            f"{name_from_camel_case(name)}.tsx" for name in self.zentra.component_names
        ]

        self.storage.UT_TO_GENERATE = list(
            set(formatted_names) - set(self.storage.UI_BASE)
        )

        self.storage.UI_TO_GENERATE = list(
            set(formatted_names) - set(self.storage.UT_TO_GENERATE)
        )

    @status
    def create_files(self) -> None:
        """Creates the React components based on the extracting models."""
        # Steps 4 and 5
        copy_zentra_files(
            self.paths.local_ui_base,
            self.paths.generated_ui_base,
            self.storage.UI_TO_GENERATE,
        )

    @status
    def update_template_files(self) -> None:
        """Updates the React components based on the Zentra model attributes."""
        pass
        # Steps 6 to 8
