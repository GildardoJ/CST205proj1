from PIL import Image, ImageFilter
#Read image
im = Image.open( '1.png' )   #you want "images/1.png" it's a folder away..
#Display image
im.show()                   #im.show() doesn't work because of the cloud.

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
im_sharp.save( 'image_sharpened.png', 'png' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

#Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data

print("hello Here here")   #comment added ...
