# Standard imports
import argparse
import glob
import os

def get_files(folder):
    """[summary]

    Args:
        folder (str): folder path

    Returns:
        (list): list of file paths
    """
    files_i_care_about = []
    for root, dirs, files in os.walk(folder, topdown=True):
        if not root.endswith("editorial"):
            continue
        for name in files:
            if name.startswith("."):
                continue
            if name.lower().endswith(".mov"):
                files_i_care_about.append(name)

    return files_i_care_about


def folder_tree_data(source_dir):
    """Get folders on user input directory and their files.

    Args:
        source_dir (str): input directory
    """
    # get root (shot) folders
    root_dirs = glob.glob("{}/*".format(source_dir))
    # for each root folder, get dir and files
    for root_dir in root_dirs:
        if os.path.isfile(root_dir):
            continue
        print ''
        print os.path.basename(root_dir)
        print "\n".join(get_files(root_dir))


def _parse_args():
    """Parcer and help definition.

    Returns:
        Parser: The command-line parser object
    """
    parser = argparse.ArgumentParser(
        description="Get text with folder context structure.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "root",
        help=(
            "The path to the root folder"
        )
    )

    return parser.parse_args()


def main():
    """Get user input and passes it to the required function."""
    args = _parse_args()
    # run function
    folder_tree_data(args.root)


if __name__ == "__main__":
    exit(main())
