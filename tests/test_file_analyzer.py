import pytest
import glob
import os
from file_analyzer import FileAnalyzer


@pytest.fixture()
def fa_instance():
    if len(glob.glob("tempfile/*")) > 0:
        [os.remove(f) for f in glob.glob("tempfile/*")]
    return FileAnalyzer("samples/sample.csv")


@pytest.fixture()
def fa_address():
    return FileAnalyzer("samples/sample_address.csv")


@pytest.fixture()
def fa_no_address():
    return FileAnalyzer("samples/sample_no_address.csv")


def test_validate_columns(fa_instance):
    assert fa_instance.validate_columns() is True


def test_lowercase_validate_columns(fa_address):
    assert fa_address.validate_columns() is True
    assert 'Address' in fa_address.df


def test_no_address_validate_columns(fa_no_address):
    assert fa_no_address.validate_columns() is False


def test_save_file(fa_instance):
    fa_instance.filename = "tempfile/test.csv"
    assert len(glob.glob("tempfile/*")) == 0
    fa_instance.save_file()
    assert fa_instance.filename.split("/")[1] in glob.glob("tempfile/*")[0]
    os.remove(fa_instance.filename)
