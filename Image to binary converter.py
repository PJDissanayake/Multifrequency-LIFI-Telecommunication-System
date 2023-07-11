
#  Read the EPD bitmap image
image_path = "img1.bmp"
image_data = open(image_path, "rb").read()

#  Convert the image data to binary
binary_data = ""
for byte in image_data:
    binary_data += format(byte, '08b')

arr = []

for bit in binary_data:
    if bit == '0':
        pass
    else:
       pass
    arr.append(int(bit))
print(arr,']')
