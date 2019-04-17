import os
import shutil
from PIL import Image
import numpy as np
import csv

# CSV und Bild sollten den gleichen Namen zurzeit haben, sonst funtkioniert es nicht
# Pfade anpassen!

class csvAuslesen:
    i = 0
    org_img_width = 2592
    org_img_height = 1944
    new_img_width = 1000
    new_img_height = 750
    csv_picture_path = "C:\\Users\\Arbeitslaptop\\Desktop\\CSV_Teamprojekt\\2015-11-16"
    cut_picture_path = "C:\\Users\\Arbeitslaptop\\Desktop\\CSV_Teamprojekt\\Parkplatz_"
    
    for filename in os.listdir(csv_picture_path):
        if not filename.endswith('.jpg'): continue
        new_path = cut_picture_path + os.path.splitext(filename)[0]
        if(os.path.exists(new_path)):
            shutil.rmtree(new_path)
        os.makedirs(new_path)
        
        im = Image.open(csv_picture_path + "\\" + filename)
        csvFileName = filename[0:(len(filename)-3)] + "csv"

        filepath = os.path.join(csv_picture_path, csvFileName)
        with open(filepath, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if (row[0] == "SlotId"): continue
                x = int(row[1])
                y = int(row[2])
                w = int(row[3])
                h = int(row[4])
                newX = (x/org_img_width)*new_img_width
                newY = (y/org_img_height)*new_img_height
                newW = (w/org_img_width)*new_img_width
                newH = (h/org_img_height)*new_img_height
                cropbox = (newX,newY,newX+newW,newY+newH)
                print(cropbox)
                zuschnitt = im.crop(cropbox)
                try:
                    zuschnitt.save(new_path + "\\Parkplatz_" + str(i)+".jpg")
                except SystemError:
                    print("Jpg existiert bereits")
                i = i+1                    
        i=0