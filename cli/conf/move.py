import os
import shutil

from rich.console import Console


console = Console()


def transfer_folder_file_pairs(
    folder_file_pairs: list[tuple[str, str]],
    src_dir: str,
    dest_dir: str,
    src_sub_dir: str = "",
) -> None:
    """Copies a set filenames from one directory to another using a list of `folder, filename)` pairs. Additionally, accepts an optional `src_sub_dir` for more refinement."""
    for folder, filename in folder_file_pairs:
        src_path = os.path.join(src_dir, folder, src_sub_dir, filename)
        dest_path = os.path.join(dest_dir, folder, filename)

        shutil.copy(src_path, dest_path)


def copy_file(filepath: str, dest_dir: str) -> None:
    """Copies a single file from one directory to another."""
    shutil.copy(filepath, dest_dir)


def copy_dir_files(filepath: str, dest_dir: str) -> None:
    """Copies a directory and its files to a new location."""
    shutil.copytree(filepath, dest_dir, dirs_exist_ok=True)
