
import os

path = "C:/Phishing_site_detection/images/google/"
for i, filename in enumerate(os.listdir(path)):
    os.rename("C:/Phishing_site_detection/images/google/" + filename, "C:/Phishing_site_detection/images/google/" + str(i) + ".jpeg")



