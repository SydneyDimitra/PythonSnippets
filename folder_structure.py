# Standart imports
import os
FILE_PATH = "" # add args function

def parse_folder(directory, recursive=True):
    """Parse the directory or the directory tree if recursive is set to True.
    Returns:
        The specified files in the given directory or directory tree
    Notes:
        Ignores hidden files.
    """
    file_list = []

    for root, dirs, files in os.walk(directory):
        files = [
            os.path.join(root, current_file) for current_file in files if
            (current_file.endswith('.abc') and not current_file.startswith('APKG'))
        ]
        file_list.extend(files)

        if not recursive:
            dirs[:] = []

        return file_list


file_list = parse_folder(FILE_PATH)
print file_list
