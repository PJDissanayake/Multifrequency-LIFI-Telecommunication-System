from PIL import Image

def con_binary(image_path): 
    
    image = Image.open(image_path)
    
    # Convert the image to grayscale
    grayscale_image = image.convert('L')
    
    # Convert the image to a binary array
    binary_array = []
    pixels = grayscale_image.getdata()
    for pixel in pixels:
        if pixel < 128:  # Adjust the threshold as needed
            binary_array.append(0)
        else:
            binary_array.append(1)
    
    return binary_array

image_path = 'img.png'  # Replace with the path to your image
binary_array = con_binary(image_path)


part_1=[]
part_2=[]
part_3=[]
part_4=[]
part_5=[]
part_6=[]
i=0
for bit in binary_array:
    if i<len(binary_array)/6:
        part_1.append(binary_array[i])

    elif i<(len(binary_array)*2)/6:
        part_2.append(binary_array[i])

    elif i<(len(binary_array)*3)/6:
        part_3.append(binary_array[i])

    elif i<(len(binary_array)*4)/6:
        part_4.append(binary_array[i])

    elif i<(len(binary_array)*5)/6:
        part_5.append(binary_array[i])

    elif i<len(binary_array):
        part_6.append(binary_array[i])
    i+=1

print('\n arr_1={',*part_1,'} \n')
print('arr_2={',*part_2,'} \n')
print('arr_3={',*part_3,'} \n')
print('arr_4={',*part_4,'} \n')
print('arr_5={',*part_5,'} \n')
print('arr_6={',*part_6,'} \n')

