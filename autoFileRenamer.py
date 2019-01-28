
import os

path = "FOLDER CONTAINING THE FILES TO BE RENAMED"
for i, filename in enumerate(os.listdir(path)):
    os.rename("FOLDER CONTAINING THE FILES TO BE RENAMED" + filename, "FOLDER CONTAINING THE FILES TO BE RENAMED" + str(i) + ".jpeg")



