#!/usr/bin/env python
"""
Visualisation - geolocation mapping.

"""
import pandas
import folium


# read data from a CSV file
data = pandas.read_csv("libraries.csv")

# find geometrical center
location = data.Latitude.mean(), data.Longitude.mean()

# draw a map using tiles from the Open Street Map project
osm = folium.Map(location, zoom_start=13)
osm.save("map.html")


# mark libraries on the map, use name as the popup information
for info in zip(data.Latitude, data.Longitude, data.Library):
	folium.Marker(info[:2], popup=info[2]).add_to(osm)

osm.save("map.html")


osm = folium.Map(location, zoom_start=15)

# mark libraries as circles with size proportional to number of computers
for info in zip(data.Latitude, data.Longitude, data.Library, data["No of PCs"]):
	folium.CircleMarker(info[:2], popup=info[2], radius=info[3],
		color="red", fill_color="green").add_to(osm)

osm.save("map_circles.html")
