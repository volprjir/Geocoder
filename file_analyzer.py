"""
Author: Jiri Volprecht
"""
import pandas
from geopy.geocoders import ArcGIS
from _datetime import datetime


class FileAnalyzer:
    """ Class to process input file """

    def __init__(self, file):
        self.file = file
        self.filename = \
            datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-%S-%f" + ".csv")
        self.df = pandas.read_csv(file)
        self.df = self.df.set_index("ID")
        self.nom = ArcGIS()

    def validate_columns(self):
        """ Validates columns format for addresses. """
        if "Address" in self.df.columns:
            return True
        if "address" in self.df.columns:
            self.df["Address"] = self.df["address"]
            return True
        else:
            return False

    def get_position(self):
        """ Creates Longitude and Latitude columns from the address """
        self.df["Coordinates"] = self.df["Address"].apply(self.nom.geocode)
        self.df["Latitude"] = self.df["Coordinates"].apply(
            lambda x: x.latitude if x is not None else None)
        self.df["Longitude"] = self.df["Coordinates"].apply(
            lambda x: x.longitude if x is not None else None)

        # Cleaning
        self.df = self.df.drop("Coordinates", axis=1)
        self.save_file()

    def save_file(self):
        """ Save the result to csv file """
        self.df.to_csv(self.filename)
