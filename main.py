#!/usr/bin/python
import Image
import sys
filename = "IMG_89"
image = Image.open(filename+".jpg")
tile_width = 180
tile_height = 120
zoom_level = 0
count = 1
currentx = 0
currenty = 0
while currenty < image.size[1]:
	while currentx < image.size[0]:
		print currentx,",",currenty, ",", currentx + tile_width, "," , currenty + tile_height
        	tile = image.crop((currentx,currenty,currentx + tile_width,currenty + tile_height))
		tile.save(filename+ "_"+str(count) + ".png","PNG")
		currentx += tile_width
                count += 1
	currenty += tile_height
	currentx = 0
	count += 1
