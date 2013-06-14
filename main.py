#!/usr/bin/python

import Image
import sys
filename = "IMG_9435"
image = Image.open(filename+".JPG")
tile_width = 100
tile_height = 80
zoom_level = 0
count = 1
currentx = 0
currenty = 0
while currenty < image.size[1]:
	while currentx < image.size[0]:
		print currentx,",",currenty
		tile = image.crop((currentx,currenty,currentx + tile_width,currenty + tile_height))
		tile.save(filename+ "_"+str(count) + ".png","PNG")
		currentx += tile_width
	currenty += tile_height
	currentx = 0
	count += 1
