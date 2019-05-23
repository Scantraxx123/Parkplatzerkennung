import os
import shutil
import sys

filename_txt = 'C:\\Users\\Arbeitslaptop\\Desktop\\Fotos\\CNR\\CNR-EXT-PATCHES-150x150\\PATCHES\\all.txt'
copy_path = "C:\\Users\\Arbeitslaptop\\Desktop\\50k_All_Parking_Spaces\\test"

counter = 0
empty = os.path.join(copy_path,"Empty")
occupied = os.path.join(copy_path,"Occupied")
filename_dir = os.path.dirname(filename_txt)
with open(filename_txt) as f:
    for x in f:
        counter += 1
        if counter == 10000:
            sys.exit()            
        split = x.rstrip().split(" ")
        copy_file = os.path.join(filename_dir,split[0])
        if(split[1] == "1"):
            shutil.copy(copy_file,occupied)
        else:
            shutil.copy(copy_file,empty)
        