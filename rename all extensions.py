import os

path = "D:/Stuff/Programming and Robotics/Raspberry Pi backup 31.10.2022/Bourbot Pi/training_data v2/Lilith Dataset/Standard Lilith"
files = os.listdir(path)
ext = ".JPEG"
ext_length = 4

for file in files:
    os.rename(path + "/" + file, path + "/" + file[:-ext_length] + ext)
