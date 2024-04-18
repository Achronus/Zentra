import os
from enum import Enum

from cli.conf.extract import local_path
from rich.console import Console


console = Console()

# Library versions
NEXTJS_VERSION = "14.1.4"
SHADCN_UI_VERSION = "0.8.0"

# Request package URLs
GITHUB_ROOT = "https://github.com/Achronus/Zentra"
BRANCH = "main"
GITHUB_URL_CORE = f"{GITHUB_ROOT}/tree/{BRANCH}"

GITHUB_COMPONENTS_DIR = f"{GITHUB_URL_CORE}/components"
GITHUB_INIT_ASSETS_DIR = f"{GITHUB_URL_CORE}/init"


class CommonErrorCodes(Enum):
    TEST_ERROR = -1
    CONFIG_MISSING = 1
    INVALID_CONFIG = 2
    CONFIG_EMPTY = 3
    ZENTRA_MISSING = 4
    MODELS_DIR_MISSING = 5
    REQUEST_FAILED = 900
    UNKNOWN_ERROR = 1000


class SetupSuccessCodes(Enum):
    COMPLETE = 10
    ALREADY_CONFIGURED = 11


class SetupErrorCodes(Enum):
    NO_COMPONENTS = 12
    IMPORT_ERROR = 13


class GenerateSuccessCodes(Enum):
    COMPLETE = 20
    NO_NEW_COMPONENTS = 21


class GenerateErrorCodes(Enum):
    NO_COMPONENTS = 22
    GENERATE_DIR_MISSING = 23


# Custom print emoji's
PASS = "[green]\u2713[/green]"
FAIL = "[red]\u274c[/red]"
PARTY = ":party_popper:"
MAGIC = ":sparkles:"


# TODO: update URLS
# Core folder names and URLS
FOLDER_NAME = "zentra"
GETTING_STARTED_URL = "#"
ERROR_GUIDE_URL = "#"
GITHUB_ISSUES_URL = "https://github.com/Astrum-AI/Zentra/issues"


class ZentaFilepaths:
    """A storage container for the core filepaths in the `zentra` folder."""

    ROOT = os.path.join(os.getcwd(), FOLDER_NAME)  # (cwd)/zentra
    MODELS = os.path.join(ROOT, "models")  # (cwd)/zentra/models
    GENERATED = os.path.join(ROOT, "generated")  # (cwd)/zentra/generated

    DEMO = os.path.join(MODELS, "_demo")  # (cwd)/zentra/models/_demo

    SETUP_FILENAME = "__init__.py"


class ZentraGeneratedFilepaths:
    """A storage container for the core filepaths in the `zentra/generated` folder."""

    # (cwd)/zentra/generated
    ROOT = ZentaFilepaths.GENERATED
    PAGES = os.path.join(ROOT, "pages")  # generated/pages
    COMPONENTS = os.path.join(ROOT, "components")  # generated/components
    LIB = os.path.join(ROOT, "lib")  # generated/lib

    ZENTRA = os.path.join(COMPONENTS, "zentra")  # generated/components/zentra


# Util filepaths
MODELS_FILEPATH = f"[magenta]{local_path(ZentaFilepaths.MODELS)}[/magenta]"
CONFIG_URL = os.path.join(ZentaFilepaths.MODELS, ZentaFilepaths.SETUP_FILENAME)
