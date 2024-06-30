import os

from zentra_models.cli.conf.types import LibraryNamePairs


def get_filename_dir_pairs(parent_dir: str, sub_dir: str = "") -> LibraryNamePairs:
    """Retrieves a list of all filenames in a parent directory and its sub-directory. Outputs them as a list of tuples with: `(parent_dir, filename)`.

    Example output:
    ```python
    ALL_BASE_FILES = get_filename_dir_pairs(parent_dir="components", sub_dir="base")
    -> [
        ("ui", "accordion.tsx"),
        ("ui", "button.tsx"),
        ...
        ("uploadthing", "core.ts"),
        ("uploadthing", "route.ts"),
        ...
       ]
    ```
    """
    all_files = []
    seen_files = set()

    if os.path.exists(parent_dir):
        search_dirs = [folder for folder in os.listdir(parent_dir)]

        for folder in search_dirs:
            search_path = os.path.join(parent_dir, folder, sub_dir)
            for file in os.listdir(search_path):
                file_tuple = (folder, file)

                if file_tuple not in seen_files:
                    all_files.append(file_tuple)
                    seen_files.add(file_tuple)

    return all_files


def get_file_content(filepath: str) -> str:
    """Reads a file and returns it as a string."""
    with open(filepath, "r") as f:
        return f.read()


def get_file_content_lines(filepath: str) -> list[str]:
    """Reads a file and returns its lines as a list of strings."""
    with open(filepath, "r") as f:
        return f.readlines()


def local_path(folder_path: str) -> str:
    """Extracts the last two directories from a `folder_path`."""
    head, tail = os.path.split(folder_path)
    root = os.path.basename(head)
    return "/".join([root, tail])
