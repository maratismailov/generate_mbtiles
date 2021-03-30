import sys
sys.path.append('/usr/share/qgis/python')
sys.path.append('/usr/lib')
from qgis.core import *
from qgis.utils import iface
import os
import processing
from processing.core.Processing import Processing
# включение инструментов обработки
Processing.initialize()

# открытие проекта с уже загруженным слоем со спутниковой подложкой Microsoft Bing
project = QgsProject.instance()
project.read('/home/zav/mbtiles/main.qgz')

#  путь к уже сгенерированному шейп-файлу
path_to_shapefile = '/home/zav/mbtiles/block.shp'

# добавление шейп-файла в проект
block_layer = QgsVectorLayer(path_to_shapefile, "Block layer", "ogr")
project.addMapLayer(block_layer)
iface.setActiveLayer(block_layer)

# приближение к требуемой области (Zoom in to the selected area)
iface.zoomToActiveLayer()

# определение угловых точек области
e = iface.mapCanvas().extent()
x_min = e.xMinimum()
x_max = e.xMaximum()
y_min = e.yMinimum()
y_max = e.yMaximum()
extent = str(x_min) + ',' + str(x_max) + ',' + str(y_min) + ',' + str(y_max) + ' ' + '[EPSG:4326]'

# запуск генерации файла
result = processing.run("qgis:tilesxyzmbtiles", {'EXTENT':extent,'ZOOM_MIN':1,'ZOOM_MAX':17, 'OUTPUT_FILE':'/home/zav/mbtiles/main.mbtiles'})

# выход из программы
os._exit(0)