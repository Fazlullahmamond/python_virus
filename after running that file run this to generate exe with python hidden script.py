import base64
import os
import subprocess
from tempfile import NamedTemporaryFile

# This imports the base64-encoded image data from the generated file
from image_data import image_data

# Decode the image data
img_data = base64.b64decode(image_data)

# Write the image data to a temporary file
with NamedTemporaryFile(delete=False, suffix=".png") as img_file:
    img_file.write(img_data)
    img_path = img_file.name

# Open the image using the default image viewer
subprocess.Popen(['start', img_path], shell=True)

# Lock the computer on Windows
os.system('rundll32.exe user32.dll,LockWorkStation')

#run this in cmd: pyinstaller --onefile open_image_and_cmd.py
