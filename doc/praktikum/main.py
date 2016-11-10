#!/bin/python

import shapefile

sf = shapefile.Reader("/home/ali/tentri/doc/praktikum/negara.shp")
print sf
shapes = sf.shapes()
print len(shapes)

#for name in dir(shapes[3]):
#		if not name.startswitch('__'):
#				print name
