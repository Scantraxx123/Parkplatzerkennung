import os
import shutil
from PIL import Image
from xml.dom import minidom
import numpy as np


class xmlAuslesen:
    frei = 0
    besetzt = 0
    insgesamt = 0
    undefiniert = 0
    i = 0
    coordinates_x = []
    coordinates_y = [] 
    labels = []
    xml_picture_path = "C:\\Users\\Arbeitslaptop\\Desktop\\Teamprojekt\\2012-09-16"
    cut_picture_path = "C:\\Users\\Arbeitslaptop\\Desktop\\Teamprojekt\\Parkplaetze_"
    
    for filename in os.listdir(xml_picture_path):
        if not filename.endswith('.jpg'): continue
        new_path = cut_picture_path + os.path.splitext(filename)[0]
        if(os.path.exists(new_path)):
            shutil.rmtree(new_path)
           
        os.makedirs(new_path)
        im = Image.open(xml_picture_path + "\\" + filename)
        xmlFileName = filename[0:(len(filename)-3)] + "xml"
   
        for filenameXml in os.listdir(xml_picture_path):
            if not filenameXml.endswith(xmlFileName): continue
            filepath = os.path.join(xml_picture_path, filenameXml)
            mydoc = minidom.parse(filepath)
            i=0
            
            items = mydoc.getElementsByTagName('point')
                        
            for elem in items:  
                coordinates_x.append(int(elem.attributes['x'].value))
                coordinates_y.append(int(elem.attributes['y'].value))
                if(len(coordinates_x) == 4):      
                    cropbox = (min(coordinates_x),min(coordinates_y),max(coordinates_x),max(coordinates_y))
                    print(cropbox)
                    zuschnitt = im.crop(cropbox)
                    coordinates_x = []
                    coordinates_y = []
                    try:
                        zuschnitt.save(new_path + "\\Parkplatz_" + str(i)+".jpg")
                    except SystemError:
                        print("Jpg existiert bereits")
                    i = i+1
              


    for filename in os.listdir(xml_picture_path):
        if not filename.endswith('.xml'): continue
        filepath = os.path.join(xml_picture_path, filename)
        document = minidom.parse(filepath)
        
        print("File: " + filepath)
        f = open(xml_picture_path + "\\" + os.path.splitext(filename)[0] + ".txt", 'w')
        
        items = mydoc.getElementsByTagName('space')
        for elem in items:
            occupied = int(elem.attributes['occupied'].value)
            try:
                insgesamt += 1
                if occupied == 1:
                    besetzt += 1
                    labels.append(1)
                elif occupied == 0:
                    frei += 1
                    labels.append(0)
                else:
                    undefiniert += 1
            except KeyError:
                print("Ein Fehler ist aufgetreten! :(")
                print("Datei: " + filepath)
                undefiniert += 1

        f.write("insgesamt: " + str(insgesamt) + "; ")
        f.write("besetzt: " + str(besetzt) + "; ")
        f.write("frei: " + str(frei) + "; ")
        f.write("undefiniert: " + str(undefiniert))
        f.close()
        np.save(os.path.join(xml_picture_path,'labels.npy'), labels)
        frei = 0
        besetzt = 0
        insgesamt = 0
        undefiniert = 0

