"""
Author: Jiri Volprecht
"""

import folium


class Webmap:
    """ Class to handle creating webmap from the data frame """

    def __init__(self, data_frame):
        self._get_location(data_frame)
        self.map_obj = folium.Map(
            location=[self.latitude.iloc[0], self.longitude.iloc[0]],
            zoom_start=12
        )

    def _get_location(self, df):
        """ Parsing necessary columns from data frame """
        self.names = df["Name"] if not None else None
        self.longitude = df["Longitude"]
        self.latitude = df["Latitude"]

    def create_webmap(self):
        """ Putting points from CSV to the map """
        fgv = folium.FeatureGroup(name="Points")
        for lt, ln, name in zip(self.latitude, self.longitude, self.names):
            fgv.add_child(folium.Marker(
                location=[lt, ln],
                popup=name,
                icon=folium.Icon(color='green'))
            )
        self.map_obj.add_child(fgv)

    def save_map(self, filename):
        """ Saves the html file with the map """
        self.filepath = filename
        self.map_obj.save(f"templates/{self.filepath}")
