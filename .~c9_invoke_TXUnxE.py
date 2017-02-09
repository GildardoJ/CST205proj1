from PIL import Image
im1 = Image.open("images/1.png")
im2 = Image.open("images/2.png")
im4 = Image.open("images/4.png")
im5 = Image.open("images/5.png")
im6 = Image.open("images/6.png")
Image.blend(im1, im2, .5).save("blended1.png")
im8 = Image.open("images/8.png")
im9 = Image.open("images/9.png")
i

for 
Image.blend(im1, im2, .5).save("blended1.png")


blended = Image.open("blended1.png")

Image.blend(blended , im3, .5).save("blended1.png")