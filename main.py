from PIL import Image
import ASCII_generator as ascii
import sys

new_limit = 10000
sys.setrecursionlimit(new_limit)

imag = Image.open("flag1.png")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert('L')
imag = imag.convert('RGBA')

#coordinates of the pixel
imgx = 30
imgy= 30
imag1 = imag.resize((imgx,imgy))
print(imag.size)
print(imag1.size)
imag1.show()

def pixel_check(X,Y,imgx,imgy):

    if X < imgx:
        pixelRGB = imag.getpixel((X, Y))
        print(imag.getpixel((X,Y)))
        R, G, B, A = pixelRGB
        #print(pixelRGB)

        brightness = sum([R, G, B]) / 3

        x = X + 1
        y = Y
        #print(x,y)
        ascii.convert_num(brightness)
        pixel_check(x,y,imgx,imgy)
    elif X >= imgx and Y <= imgy:
        pixelRGB = imag.getpixel((X, Y))
        R, G, B, A = pixelRGB

        brightness = sum([R, G, B]) / 3

        x = 0
        y = Y+1
        #print(y)
        ascii.convert_num(brightness)
        ascii.print_chars()
        pixel_check(x,y,imgx,imgy)
    else:
        print("Done")

pixel_check(0,0,imgx,imgy)

