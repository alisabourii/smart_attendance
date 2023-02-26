import take_foto_code
import found_faces
import time
from datetime import datetime

now = datetime.now()
clock =now.strftime("%d/%m/%Y %H:%M:%S")

take_foto_code.take_foto()
time.sleep(0.5)


for i in range(1,3):
    found_faces.found_face("filename{0}".format(i))
    time.sleep(0.5)
