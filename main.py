from PIL import Image
import ASCII_generator as ascii
import sys
import sqlite3
import time

col = False

new_limit = 1000000
sys.setrecursionlimit(new_limit)


image = "opencv_frame_2.png"
imag = Image.open(image)

imag = imag.convert('RGBA')

# coordinates of the pixel
imgx = int(input("Please enter the value for the length of the image. "))
imgy = (int(imag.size[1]))*(int(imgx)/(int(imag.size[0])))
imag1 = imag.resize((imgx, int(imgy)))
inp = input("Press '1' if you want the image to print in black and white, or '2' if you want it to print in colour")
if inp == '1':
    col = False
elif inp == '2':
    col = True
print(imag.size)
print(imag1.size)


def pixel_check(x, y, imgx, imgy):

    if y < imag1.height:
        if x < imag1.width:
            pixelrgb = imag1.getpixel((x, y))
            r, g, b, a = pixelrgb

            brightness = sum([r, g, b]) / 3

            xpos = x + 1
            ypos = y
            ascii.convert_num3(brightness, col, r, g, b)
            pixel_check(xpos, ypos, imgx, imgy)
        elif x == imag1.width and y <= imag1.height:
            pixelrgb = imag.getpixel((x, y))
            r, g, b, a = pixelrgb

            brightness = sum([r, g, b]) / 3

            xpos = 0
            ypos = y + 1
            ascii.convert_num3(brightness, col, r, g, b)
            if not col:
                print_chars_c()
            else:
                print_chars_bw()
            pixel_check(xpos, ypos, imgx, imgy)
        elif y > imag1.height:
            print("")
    else:
        save = input("Do you want to save your image to a database?(y/n)")
        if save == 'y':
            insert_ui()
        else:
            print("")


def pixel_check_db(x, y, imgx, imgy):

    if y < imag1.height:
        if x < imag1.width:
            pixelrgb = imag1.getpixel((x, y))
            r, g, b, a = pixelrgb

            brightness = sum([r, g, b]) / 3

            xpos = x + 1
            ypos = y
            ascii.convert_num3(brightness, col, r, g, b)
            pixel_check_db(xpos, ypos, imgx, imgy)
        elif x == imag1.width and y <= imag1.height:
            pixelrgb = imag.getpixel((x, y))
            r, g, b, a = pixelrgb

            brightness = sum([r, g, b]) / 3

            xpos = 0
            ypos = y + 1
            ascii.convert_num3(brightness, col, r, g, b)
            if col:
                print_chars_c()
            else:
                print_chars_bw()
            pixel_check_db(xpos, ypos, imgx, imgy)
    else:
        print("")


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


def insert_data(values):

    with sqlite3.connect("ASCII.db") as db:
        cursor = db.cursor()
        sql = "insert into ASCII_Art (Name, Art) values (?,?)"
        cursor.execute(sql, values)
        db.commit()


def insert_ui():

    product_name = input("Please enter name of new product.\n")
    art = image
    print(art)
    product = (product_name, art)
    print("Adding %s to Products" % product_name)
    time.sleep(1.0)
    print(".")
    time.sleep(1.0)
    print(".")
    time.sleep(1.0)
    print(".")
    time.sleep(1.0)
    print("%s added to products" % product_name)
    time.sleep(1.0)
    insert_data(product)


if imgx > 215:
    print("Can't have image bigger than 215")
else:
    pixel_check(0, 0, imgx, imgy)
    
