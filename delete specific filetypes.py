import os

path = "D:/Stuff/Programming and Robotics/Python and Robotics/Projects/Agricultural Robotics/object detection/fruit/orange"
extension = ".xml"
count = len(extension)

files = os.listdir(path)

for file in files:
    if file[-count:] == extension:
        os.remove(path + "/" + file)

