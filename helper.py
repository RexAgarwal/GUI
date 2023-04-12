from PIL import Image

# Read the image file
image1 = Image.open('Images/1.jpg')
image2 = Image.open('Images/2.jpg')

for i in range(1,101):
    # Save the image as a new file
    if i%2 ==0:
        image1.save("Images/"+str(i)+'.jpg')
    else:
        image2.save("Images/"+str(i)+'.jpg')
