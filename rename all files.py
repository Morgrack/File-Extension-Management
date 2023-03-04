import os

path = "D:/Stuff/Programming and Robotics/Raspberry Pi backup 31.10.2022/Bourbot Pi/training_data v2/Lilith Dataset/Smiling Lilith"
files = os.listdir(path)
name = "smiling_lilith"
no = 0
ext_length = 4

for file in files:
    os.rename(path + "/" + file, path + "/" + name + "_" + str(no) + file[-ext_length:])
    no = no + 1
