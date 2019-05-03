import random
import os
import shutil

rootdir = "C:\\Users\\Arbeitslaptop\\Desktop\\Fotos\\PKLot\\PKLotSegmented\\UFPR05"
train_empty ="C:\\Users\\Arbeitslaptop\\Desktop\\Test_Packete\\UFPR05\\train\\Empty"
train_occupied ="C:\\Users\\Arbeitslaptop\\Desktop\\Test_Packete\\UFPR05\\train\\Occupied"

test_empty ="C:\\Users\\Arbeitslaptop\\Desktop\\Test_Packete\\UFPR05\\test\\Empty"
test_occupied ="C:\\Users\\Arbeitslaptop\\Desktop\\Test_Packete\\UFPR05\\test\\Occupied"



i = 0
empty_path = []
occupied_path = []

for subdir, dirs, files in os.walk(rootdir):
    temp = os.path.basename(os.path.normpath(subdir))
    if temp == "Empty":
        for file in files:
            empty_path.append(os.path.join(subdir, file))
    if temp == "Occupied":
        for file in files:
            occupied_path.append(os.path.join(subdir, file))    
        
random.shuffle(empty_path)
random.shuffle(occupied_path)

length_empty = int(len(empty_path))
length_occupied = int(len(occupied_path))



for x in range(0,int(length_empty/2)):
    shutil.copy(empty_path[x],train_empty)
    
print("First done")
    
for x in range(int(length_empty/2),int(length_empty)):
    shutil.copy(empty_path[x],test_empty)

print("Second done")
    
for x in range(0,int(length_occupied/2)):
    shutil.copy(occupied_path[x],train_occupied)
    
print("Third done")
    
for x in range(int(length_occupied/2),int(length_occupied)):
    shutil.copy(occupied_path[x],test_occupied)    

    
