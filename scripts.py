"""
Author: Jiri Volprecht
"""

import glob
import os

temporary_file_paths = ["templates/20*", "uploads/*"]


def clean():
    """ Removes temporary files when they are no longer needed """
    if len(temporary_file_paths) > 0:
        [os.remove(tmp_file) for f in temporary_file_paths for tmp_file in glob.glob(f)]
    return False


def count_temp_files():
    """ Counts temporary files which could be deleted """
    to_remove = []
    [to_remove.extend(glob.glob(f)) for f in temporary_file_paths]
    return len(to_remove)
