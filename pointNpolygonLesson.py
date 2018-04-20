# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:59:47 2018
AutoGIS Lesson 3
Point in Polygon
@author: harrisab2
"""
# import modules
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon, MultiLineString
import matplotlib.pyplot as plt

# create point objects
p1 = Point(24.9522, 60.1699)
p2 = Point(25.3243, 61.3433)

# create polygon
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)

# check if p1 is within the polygon using within function
p1.within(poly)

# check if polygon contains point
poly.contains(p1)

# create linestrings
line_a = LineString([(0, 0), (1, 1)])
line_b = LineString([(1, 1), (0, 2)])

# check to see if intersect
line_a.intersects(line_b)

# do they touch
line_a.touches(line_b)

# create multilinestring
multi_line = MultiLineString([line_a, line_b])

# read in addresses from shapefile saved earlier
fp = r'F:\GS\harrisab2\S18\GeoViz\autoGIS_3\lesson_address.shp'
data = gpd.read_file(fp)

# enable read and write functions for kml-driver passing 'rw' 
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

# read data from KML file
kmlfp = r'F:\GS\harrisab2\S18\GeoViz\autoGIS_3\PKS_suuralue.kml'
polys = gpd.read_file(kmlfp, driver='KML')

# select southern district 'Etelainen"
southern = polys.loc[polys['Name']=='Eteläinen']

# clean data and plot
southern.reset_index(drop=True, inplace=True)
fix, ax = plt.subplots()
polys.plot(ax=ax, facecolor='gray');
southern.plot(ax=ax, facecolor='red');
data.plot(ax=ax, color='blue', markersize=5);
plt.tight_layout();
