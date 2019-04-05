import os
import shutil

source = ""
dest_empty = ""
dest_occ = ""

for dirname, dirnames, filenames in os.walk(source):
    for subdirname in dirnames:
        if(subdirname == "Empty"):
            for file_name in os.listdir(os.path.join(dirname, subdirname)):
                shutil.copy(os.path.join(dirname, subdirname,file_name), dest_empty)
        if(subdirname == "Occupied"):
            for file_name in os.listdir(os.path.join(dirname, subdirname)):
                shutil.copy(os.path.join(dirname, subdirname,file_name), dest_occ)            

        
            
        
            
        
