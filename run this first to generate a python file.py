import base64

# Read the image file in binary mode
with open('input_image.png', 'rb') as img_file:
    encoded_string = base64.b64encode(img_file.read()).decode()

# Write the base64 encoded string to a Python file
with open('image_data.py', 'w') as out_file:
    out_file.write(f'image_data = "{encoded_string}"\n')
