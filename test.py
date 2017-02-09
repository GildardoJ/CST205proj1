#Gildardo Orozco
#CST205_02
#Avner Biblarz
#2-8-2017

from PIL import Image   #python brings in Pillow library 

im1 = Image.open("images/1.png")   #images opened and stored to a variable
im2 = Image.open("images/2.png")
im3 = Image.open("images/3.png")
im4 = Image.open("images/4.png")
im5 = Image.open("images/5.png")
im6 = Image.open("images/6.png")
im7 = Image.open("images/7.png")
im8 = Image.open("images/8.png")
im9 = Image.open("images/9.png")

images = [im1,im2,im3,im4,im5,im6,im8,im9]; #array with all the images in it. An Array to make it easier to use the for loops. 

#Median function copied from PDF
def medianOdd(myList):   
    listLength = len(myList)
    sortedValues = sorted(myList)
    middleIndex = ((listLength + 1)/2) - 1
    return ((sortedValues[middleIndex] + sortedValues[middleIndex+1])/2)

num =  len(images)  #number of images in list stored in num
w,h = im2.size      #size of image, width and Height

#new image file to copy pixels to
final = Image.new('RGBA',(w,h))  #blank image

#nested loop
for y in range(h): #loops through the height of the images
    for x in range(w): #loops through the width of the images
        medianR = []
        medianG = []
        medianB = []
        for i in range(0,num): #loops through the 8 images to get the RGB value of each 
            current = images[i]
            r,g,b = current.getpixel((x,y))
            
            #appending each color value to its own array
            medianR.append(r)
            medianG.append(g)
            medianB.append(b)
            
        #median value for each color
        r = medianOdd(medianR)
        g = medianOdd(medianG)
        b = medianOdd(medianB)
        
        final.putpixel((x,y), (r,g,b))  # The median value of each color is put into the new image.
        
        #empty out variables so it can start again from blank
        del medianR[:]
        del medianG[:]
        del medianB[:]

#save final image 
final.save('images/finalImg.png')  

print "done"   #print out to show that something happend. 



