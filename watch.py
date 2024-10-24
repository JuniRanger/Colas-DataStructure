#Este es un script para compilar conforme los cambios el archivo

import os
import time
import subprocess

script = "main.py"

lastModifiedTime = os.path.getmtime(script)

while True:
    time.sleep(1)
    currentModifedTime = os.path.getmtime(script)
    if currentModifedTime != lastModifiedTime:
        lastModifiedTime = currentModifedTime
        subprocess.run(["python", script])