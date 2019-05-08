import os
import shutil

filename_txt = 'C:\\Users\\Arbeitslaptop\\Desktop\\Fotos\\CNR\\CNR-EXT-PATCHES-150x150\\PATCHES\\all.txt'
copy_path = "C:\\Users\Arbeitslaptop\\Desktop\\CNR\\test"


empty = os.path.join(copy_path,"empty")
occupied = os.path.join(copy_path,"occupied")
filename_dir = os.path.dirname(filename_txt)
with open(filename_txt) as f:
    for x in f:
        split = x.rstrip().split(" ")
        copy_file = os.path.join(filename_dir,split[0])
        if(split[1] == "1"):
            shutil.copy(copy_file,occupied)
        else:
            shutil.copy(copy_file,empty)
        