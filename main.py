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

#imag = imag.convert('L')
imag = imag.convert('RGBA')

#coordinates of the pixel
imgx = int(input("Please enter the value for the length of the image. "))
imgy= (int(imag.size[1]))*(int(imgx)/(int(imag.size[0])))
imag1 = imag.resize((imgx,int(imgy)))
inp = input("Press '1' if you want the image to print in black and white, or '2' if you want it to print in colour")
if inp == '1':
    col = False
elif inp == '2':
    col = True
print(imag.size)
print(imag1.size)
#imag1.show()

def pixel_check(X,Y,imgx,imgy):

    if Y < imag1.height:
        if X < imag1.width:
            pixelRGB = imag1.getpixel((X, Y))
            #print(imag.getpixel((X,Y)))
            R, G, B, A = pixelRGB

            brightness = sum([R, G, B]) / 3

            x = X + 1
            y = Y
            #print(x,y)
            ascii.convert_num3(brightness,col,R,G,B)
            pixel_check(x,y,imgx,imgy)
        elif X == imag1.width and Y <= imag1.height:
            pixelRGB = imag.getpixel((X, Y))
            R, G, B, A = pixelRGB

            brightness = sum([R, G, B]) / 3

            x = 0
            y = Y+1
            #print(y)
            ascii.convert_num3(brightness,col,R,G,B)
            if col == True:
                print_chars_C()
            else:
                print_chars_BW()
            pixel_check(x,y,imgx,imgy)
        elif Y > imag1.height:
            print("")
    else:
        save = input("Do you want to save your image to a database?(y/n)")
        if save == 'y':
            insert_UI()
        else:
            print("")

def pixel_check_db(X,Y,imgx,imgy):

    if Y < imag1.height:
        if X < imag1.width:
            pixelRGB = imag1.getpixel((X, Y))
            #print(imag.getpixel((X,Y)))
            R, G, B, A = pixelRGB

            brightness = sum([R, G, B]) / 3

            x = X + 1
            y = Y
            #print(x,y)
            ascii.convert_num3(brightness,col,R,G,B)
            pixel_check_db(x,y,imgx,imgy)
        elif X == imag1.width and Y <= imag1.height:
            pixelRGB = imag.getpixel((X, Y))
            R, G, B, A = pixelRGB

            brightness = sum([R, G, B]) / 3

            x = 0
            y = Y+1
            #print(y)
            ascii.convert_num3(brightness,col,R,G,B)
            if col:
                print_chars_C()
            else:
                print_chars_BW()
            pixel_check_db(x,y,imgx,imgy)
    else:
        print("")

def print_chars_BW():
    if len(ascii.art) > imgx:
        del(ascii.art[-1])
    print(" ".join(ascii.art))
    ascii.art.clear()

def print_chars_C():
    if len(ascii.art) > imgx:
        del(ascii.art[-1])
    print("".join(ascii.art))
    ascii.art.clear()

def insert_data(values):

    with sqlite3.connect("ASCII.db") as db:
        cursor = db.cursor()
        sql = "insert into ASCII_Art (Name, Art) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

def insert_UI():

    product_name = input("Please enter name of new product.\n")
    art = image
    print(art)
    product = (product_name, art)
    #print(product)
    print("Adding %s to Products" % product_name)
    time.sleep(1.0)
    print(".")
    time.sleep(1.0)
    print(".")
    time.sleep(1.0)
    print(".")
    time.sleep(1.0)
    print("%s added to products"% product_name)
    time.sleep(1.0)
    insert_data(product)


if imgx > 215:
    print("Can't have image bigger than 215")
else:
    pixel_check(0,0,imgx,imgy)

