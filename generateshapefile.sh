#!/bin/bash
ogr2ogr -f "ESRI Shapefile" block.shp PG:"host=192.168.20.78 user=postgres dbname=forest_bd" -sql "SELECT the_geom FROM forest.block WHERE gid = $1"
