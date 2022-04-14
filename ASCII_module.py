from PIL import Image
import ASCII_generator as ascii
import sys
import cv2

new_limit = 1000000
sys.setrecursionlimit(new_limit)


def convert_ascii(image, imgx, col):

    error = False

    imag = Image.open(image)

    imag = imag.convert('RGBA')

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
                r, g, b, a = pixelrgb

                brightness = sum([r, g, b]) / 3

                xpos = x + 1
                ypos = y
                ascii.convert_num(brightness, col, r, g, b)
                pixel_check(xpos, ypos, imgx, imgy)
            elif x == imag1.width and y <= imag1.height:
                pixelrgb = imag.getpixel((x, y))
                r, g, b, a = pixelrgb

                brightness = sum([r, g, b]) / 3

                xpos = 0
                ypos = y + 1

                ascii.convert_num(brightness, col, r, g, b)
                if col:
                    print_chars_c()
                else:
                    print_chars_bw()
                pixel_check(xpos, ypos, imgx, imgy)
            elif y > imag1.height:
                print("")
        else:
            print('')

    def print_chars_bw():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print(" ".join(ascii.art))
        ascii.art.clear()

    def print_chars_c():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print("".join(ascii.art))
        ascii.art.clear()

    if not error:
        if imgx * imgy > 29070:
            print("Can't have more than 29070 pixels")
        else:
            pixel_check(0, 0, imgx, imgy)
    else:
        print('')


def convert_photo(image, imgx):

    error = False

    imag = Image.open(image)

    imag = imag.convert('RGBA')

    try:
        imgx = int(imgx)
        imgy = (int(imag.size[1])) * (int(imgx) / (int(imag.size[0])))
        imag1 = imag.resize((imgx, int(imgy)))
    except ValueError:
        error = True
        print('')
        print('Error')
        print('')
        print('Please input only numbers')

    def pixel_check(x, y, imgx, imgy):
        col = True
        if y < imag1.height:
            if x < imag1.width:
                pixelrgb = imag1.getpixel((x, y))
                r, g, b, a = pixelrgb

                brightness = sum([r, g, b]) / 3

                xpos = x + 1
                ypos = y
                # print(x,y)
                ascii.convert_num2(r, g, b)
                pixel_check(xpos, ypos, imgx, imgy)
            elif x == imag1.width and y <= imag1.height:
                pixelrgb = imag.getpixel((x, y))
                r, g, b, a = pixelrgb

                brightness = sum([r, g, b]) / 3

                xpos = 0
                ypos = y + 1
                # print(y)
                ascii.convert_num2(r, g, b)
                if col:
                    print_chars_c()
                else:
                    print_chars_bw()
                pixel_check(xpos, ypos, imgx, imgy)
            elif y > imag1.height:
                print("")
            else:
                print("")
        else:
            print("")

    def print_chars_bw():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print(" ".join(ascii.art))
        ascii.art.clear()

    def print_chars_c():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print("".join(ascii.art))
        ascii.art.clear()

    if not error:
        if imgx * imgy > 29070:
            print("Can't have more than 29070 pixels")
        else:
            pixel_check(0, 0, imgx, imgy)
    else:
        print('')


def convert_cam(imgx, col, type):
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        cam_convert(imgx, col, type)
        break

    cam.release()

    cv2.destroyAllWindows()


def cam_convert(imgx, col, type):

    error = False

    image = "opencv_frame_0.png"
    imag = Image.open(image)

    imag = imag.convert('RGBA')

    try:
        imgx = int(imgx)
        imgy = (int(imag.size[1])) * (int(imgx) / (int(imag.size[0])))
        imag1 = imag.resize((imgx, int(imgy)))
    except ValueError:
        error = True
        print('')
        print('Error')
        print('')
        print('Please input only numbers')

    def pixel_check2(x, y, imgx, imgy, type):
        if y < imag1.height:
            if x < imag1.width:
                pixelrgb = imag1.getpixel((x, y))

                r, g, b, a = pixelrgb

                brightness = sum([r, g, b]) / 3

                xpos = x + 1
                ypos = y

                if type:
                    ascii.convert_num(brightness, col, r, g, b)
                else:
                    ascii.convert_num2(r, g, b)
                pixel_check2(xpos, ypos, imgx, imgy, type)
            elif x == imag1.width and y <= imag1.height:
                pixelrgb = imag.getpixel((x, y))
                r, g, b, a = pixelrgb

                brightness = sum([r, g, b]) / 3

                xpos = 0
                ypos = y + 1

                if type:
                    ascii.convert_num(brightness, col, r, g, b)
                else:
                    ascii.convert_num2(r, g, b)
                if col:
                    print_chars_c()
                else:
                    print_chars_bw()
                pixel_check2(xpos, ypos, imgx, imgy, type)
            elif y > imag1.height:
                print("")
            else:
                print('')
        else:
            print("")

    def print_chars_bw():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print(" ".join(ascii.art))
        ascii.art.clear()

    def print_chars_c():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print("".join(ascii.art))
        ascii.art.clear()

    if not error:
        if imgx * imgy > 29070:
            print("Can't have more than 29070 pixels")
        else:
            pixel_check2(0, 0, imgx, imgy, type)
    else:
        print('')
