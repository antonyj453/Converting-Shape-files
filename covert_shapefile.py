import geopandas as gpd
import matplotlib.pyplot as plt

# Filepaths
grid_fp = r"C:/Users/Antony/Downloads/dataE5/dataE5/TravelTimes_to_5975375_RailwayStation.shp"
roads_fp = r"C:/Users/Antony/Downloads/dataE5/dataE5/roads.shp"
metro_fp = r"C:/Users/Antony/Downloads/dataE5/dataE5/metro.shp"
address_fp = r"C:/Users/Antony/Downloads/dataE5/dataE5/addresses.shp"
# Read files
grid = gpd.read_file(grid_fp)
roads = gpd.read_file(roads_fp)
metro = gpd.read_file(metro_fp)
address=gpd.read_file(address_fp)
