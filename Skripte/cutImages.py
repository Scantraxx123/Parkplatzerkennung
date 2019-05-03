import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import xml.etree.ElementTree as ET 

def main():

	# Path für die Bilder
	XML_IMAGE_PATH = "F:/Machine Learning Data/PKLot/PKLot/UFPR04/Sunny/2012-12-13/"
	# Output-Path der segmentierten Bilder
	XML_IMAGE_OUTPUT = "C:/Users/FredeR/Desktop/Ausgabe/"
	
	for data in os.listdir(XML_IMAGE_PATH):
		if data.endswith('.jpg'):
			img = cv2.imread(os.path.join(XML_IMAGE_PATH, data))
			newPath = XML_IMAGE_OUTPUT + '/' + data[:-3] + '/'
			occupiedPath = newPath + '/' + "occupied" + '/'
			emptyPath = newPath + '/' + "empty" + '/'
			directories = [newPath, occupiedPath, emptyPath]
			for dir in directories:
				os.mkdir(dir)
			tree = ET.parse(XML_IMAGE_PATH + '/' + data[:-3] + 'xml')
			root = tree.getroot()
			for space in tree.iter('space'):
				id = space.get('id')
				occupied = space.get('occupied')
				points = []
				for point in space.iter('point'):
					points.append(point.get('x'))
					points.append(point.get('y'))
				cnt = np.array([
						[[int(points[0]), int(points[1])]],
						[[int(points[2]), int(points[3])]],
						[[int(points[4]), int(points[5])]],
						[[int(points[6]), int(points[7])]]
					])
				rect = cv2.minAreaRect(cnt)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				width = int(rect[1][0])
				height = int(rect[1][1])
				src_pts = box.astype("float32")
				dst_pts = np.array([[0, height-1],
									[0, 0],
									[width-1, 0],
									[width-1, height-1]], dtype="float32")
				M = cv2.getPerspectiveTransform(src_pts, dst_pts)
				finalImage = cv2.warpPerspective(img, M, (width, height))
				if width > height:
					finalImage =cv2.rotate(finalImage, cv2.ROTATE_90_CLOCKWISE)
				if occupied =='1':
					cv2.imwrite(occupiedPath + data[:-3] + id + ".jpg", finalImage)
				else: 
					cv2.imwrite(emptyPath + data[:-3] + id + ".jpg", finalImage)


if __name__ == "__main__":
    main()