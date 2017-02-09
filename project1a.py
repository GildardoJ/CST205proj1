from PIL import Image
im1 = Image.open("images/1.png")
im2 = Image.open("images/2.png")
im3 = Image.open("images/3.png")
im4 = Image.open("images/4.png")
im5 = Image.open("images/5.png")
im6 = Image.open("images/6.png")
im7 = Image.open("images/7.png")
im8 = Image.open("images/8.png")
im9 = Image.open("images/9.png")


imgages =[im1,im2,im3,im4,im5,im6,im8,im9]

Image.blend(im1 ,im2 , .5).save("images/blended1.png")
blended = Image.open("images/blended1.png")

for x in range(3,10):
    name = Image.open("images/%s.png" % x)
    Image.blend(blended ,name , .5).save("images/blended1.png")
    blended = Image.open("images/blended1.png")
    print "image %s" % x
    
#blended = Image.open("images/blended1.png")
print "0th"
for x in range(1,10):
    name = Image.open("images/%s.png" % x)
    Image.blend(blended ,name , .4).save("images/blended1.png")
    blended = Image.open("images/blended1.png")
    print "image %s" % x

print "1st"
for x in range(1,10):
    name = Image.open("images/%s.png" % x)
    Image.blend(blended ,name , .3).save("images/blended1.png")
    blended = Image.open("images/blended1.png")
    print "image %s" % x
    
print "2nd"
for x in range(1,10):
    name = Image.open("images/%s.png" % x)
    Image.blend(blended ,name , .25).save("images/blended1.png")
    blended = Image.open("images/blended1.png")
    print "image %s" % x   
    
print "3rd"

for y in range(1,5):    
    for x in range(1,10):
        name = Image.open("images/%s.png" % x)
        Image.blend(blended ,name , .20).save("images/blended1.png")
        blended = Image.open("images/blended1.png")
        print "image %s" % x
        
    print "%sth" % y
    
print "done"
