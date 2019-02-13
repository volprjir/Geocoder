import pytest
import pandas as pd
import os
import glob
from webmap import Webmap

sample_file = "samples/sample.csv"


@pytest.fixture()
def webmap_instance():
    df = pd.read_csv(sample_file)
    return Webmap(df)


def test_save_map(webmap_instance):
    assert "test.html" not in glob.glob("templates/*")
    webmap_instance.save_map("test.html")
    assert "test.html" in glob.glob("templates/*")[0]
    os.remove("templates/test.html")


def test_get_location(webmap_instance):
    df = pd.read_csv(sample_file)
    assert len(webmap_instance.longitude) == len(df["Longitude"])
    assert len(webmap_instance.latitude) == len(df["Latitude"])
    assert len(webmap_instance.longitude) == len(webmap_instance.latitude)
