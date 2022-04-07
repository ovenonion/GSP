from PIL import Image
import ASCII_generator as ascii
import sys

col = False
error = False

new_limit = 1000000
sys.setrecursionlimit(new_limit)

image = "contrast.jpg"
imag = Image.open(image)

imag = imag.convert('RGBA')

# coordinates of the pixel
imgx = input("Please enter the value for the length of the image. ")

try:
    imgx = int(imgx)
    imgy = (int(imag.size[1])) * (int(imgx) / (int(imag.size[0])))
    imag1 = imag.resize((imgx, int(imgy)))
    inp = input("Do you want the image in colour? y/n")
    if inp == 'y':
        col = True
    else:
        col = False
except ValueError:
    error = True
    print('')
    print('Error')
    print('')
    print('Please input only numbers')


def pixel_check(x, y, imgx, imgy):

    if y < imag1.height:
        if x < imag1.width:
            pixelrgb = imag1.getpixel((x, y))

            R, G, B, A = pixelrgb

            brightness = sum([R, G, B]) / 3

            xpos = x + 1
            ypos = y

            ascii.convert_num(brightness, col, R, G, B)
            pixel_check(xpos, ypos, imgx, imgy)
        elif x == imag1.width and y <= imag1.height:
            pixelrgb = imag.getpixel((x, y))
            R, G, B, A = pixelrgb

            brightness = sum([R, G, B]) / 3

            xpos = 0
            ypos = y+1

            ascii.convert_num(brightness, col, R, G, B)
            if col:
                print_chars_c()
            else:
                print_chars_bw()
            pixel_check(xpos, ypos, imgx, imgy)
        elif y > imag1.height:
            print('')
    else:
        print('')


def print_chars_bw():
    if len(ascii.art) > imgx:
        del(ascii.art[-1])
    print(" ".join(ascii.art))
    ascii.art.clear()


def print_chars_c():
    if len(ascii.art) > imgx:
        del(ascii.art[-1])
    print("".join(ascii.art))
    ascii.art.clear()


if not error:
    if imgx * imgy > 29070:
        print("Can't have more than 29070 pixels")
    else:
        pixel_check(0, 0, imgx, imgy)
else:
    print('')
