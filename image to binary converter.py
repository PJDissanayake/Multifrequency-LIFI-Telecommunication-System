from PIL import Image

def con_binary(image_path): 
    
    image = Image.open(image_path)
    
    # Convert the image to grayscale
    grayscale_image = image.convert('L')
    
    # Convert the image to a binary array
    binary_array = []
    pixels = grayscale_image.getdata()
    for pixel in pixels:
        if pixel < 128:  # Adjust the threshold 
            binary_array.append(0)
        else:
            binary_array.append(1)
    
    return binary_array

image_path = 'img.png'  
binary_array = con_binary(image_path)


part_1=[]
part_2=[]
part_3=[]
part_4=[]
part_5=[]
part_6=[]
part_7=[]
part_8=[]
part_9=[]
part_10=[]
part_11=[]
part_12=[]
part_13=[]
part_14=[]
part_15=[]
part_16=[]

i=0
for bit in binary_array:
    if i<len(binary_array)/16:
        part_1.append(binary_array[i])

    elif i<(len(binary_array)*2)/16:
        part_2.append(binary_array[i])

    elif i<(len(binary_array)*3)/16:
        part_3.append(binary_array[i])

    elif i<(len(binary_array)*4)/16:
        part_4.append(binary_array[i])

    elif i<(len(binary_array)*5)/16:
        part_5.append(binary_array[i])

    elif i<(len(binary_array)*6)/16:
        part_6.append(binary_array[i])

    elif i<(len(binary_array)*7)/16:
        part_7.append(binary_array[i])

    elif i<(len(binary_array)*8)/16:
        part_8.append(binary_array[i])

    elif i<(len(binary_array)*9)/16:
        part_9.append(binary_array[i])

    elif i<(len(binary_array)*10)/16:
        part_10.append(binary_array[i])

    elif i<(len(binary_array)*11)/16:
        part_11.append(binary_array[i])

    elif i<(len(binary_array)*12)/16:
        part_12.append(binary_array[i])

    elif i<(len(binary_array)*13)/16:
        part_13.append(binary_array[i])

    elif i<(len(binary_array)*14)/16:
        part_14.append(binary_array[i])

    elif i<(len(binary_array)*15)/16:
        part_15.append(binary_array[i])

    else:
        part_16.append(binary_array[i])
    i+=1

print('\n *** Below, the binary data of the image is divided into 16 Array.\n')

print('\n byte arr_1[]={',end="")
print(*part_1,'};',sep=",")
print('\n byte arr_2[]={',end="")
print(*part_2,'};',sep=",")
print('\n byte arr_3[]={',end="")
print(*part_3,'};',sep=",")
print('\n byte arr_4[]={',end="")
print(*part_4,'};',sep=",")
print('\n byte arr_5[]={',end="")
print(*part_5,'};',sep=",")
print('\n byte arr_6[]={',end="")
print(*part_6,'};',sep=",")
print('\n byte arr_7[]={',end="")
print(*part_7,'};',sep=",")
print('\n byte arr_8[]={',end="")
print(*part_8,'};',sep=",")
print('\n byte arr_9[]={',end="")
print(*part_9,'};',sep=",")
print('\n byte arr_10[]={',end="")
print(*part_10,'};',sep=",")
print('\n byte arr_11[]={',end="")
print(*part_11,'};',sep=",")
print('\n byte arr_12[]={',end="")
print(*part_12,'};',sep=",")
print('\n byte arr_13[]={',end="")
print(*part_13,'};',sep=",")
print('\n byte arr_14[]={',end="")
print(*part_14,'};',sep=",")
print('\n byte arr_15[]={',end="")
print(*part_15,'};',sep=",")
print('\n byte arr_16[]={',end="")
print(*part_16,'};',sep=",")
print('\n')


input("Press Enter to exit...")