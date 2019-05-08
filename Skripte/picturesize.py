from PIL import Image
import os


dir_pictures = "C:\\Users\\Arbeitslaptop\\Desktop\\Neuer Ordner\\PUC_UFPR05_04_50_50"
d = dict()
width_count = 0
height_count = 0
picture_count = 0

for root, dirs, files in os.walk(dir_pictures):
    for file in files:
        if file.endswith(".jpg"):
            with Image.open(os.path.join(root, file)) as img:
                picture_count += 1
                width, height = img.size
                width_count += width
                height_count += height
                key = "{} {}".format(height,width)
                if key in d:
                    d[key] += 1
                else:
                    d[key] = 1



with open("Output.txt", "w") as text_file:
    text_file.write("Height Width\n")
    text_file.write("Average: {} {}\n".format(height_count/picture_count,width_count/picture_count))
    for key, value in d.items():
        text_file.write("{}: {}x\n".format(key,value))
