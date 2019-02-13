import pytest
import glob
import os
import scripts as s


@pytest.fixture()
def set_test_folder():
    s.temporary_file_paths = ["tempfile/*"]
    [os.remove(f) for f in glob.glob("tempfile/*")]


@pytest.fixture()
def create_tmp_file():
    with open("tempfile/test.txt", "w"):
        pass


def test_empty_count_temp_files(set_test_folder):
    assert s.count_temp_files() == 0


def test_create_count_temp_files(set_test_folder, create_tmp_file):
    assert s.count_temp_files() == 1
    os.remove("tempfile/test.txt")


def test_clean_directory(set_test_folder, create_tmp_file):
    assert s.count_temp_files() == 1
    s.clean()
    assert s.count_temp_files() == 0
