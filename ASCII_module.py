from PIL import Image
import ASCII_generator as ascii
import sys
import cv2

new_limit = 1000000
sys.setrecursionlimit(new_limit)

clearConsole = lambda: print('\n' * 150)

def convert_ASCII(image, imgx, col):

    imag = Image.open(image)

    imag = imag.convert('RGBA')

    # coordinates of the pixel
    imgy = (int(imag.size[1])) * (int(imgx) / (int(imag.size[0])))
    imag1 = imag.resize((imgx, int(imgy)))

    def pixel_check(X, Y, imgx, imgy):
        if Y < imag1.height:
            if X < imag1.width:
                pixelRGB = imag1.getpixel((X, Y))
                # print(imag.getpixel((X,Y)))
                R, G, B, A = pixelRGB

                brightness = sum([R, G, B]) / 3

                x = X + 1
                y = Y
                # print(x,y)
                ascii.convert_num(brightness, col, R, G, B)
                pixel_check(x, y, imgx, imgy)
            elif X == imag1.width and Y <= imag1.height:
                pixelRGB = imag.getpixel((X, Y))
                R, G, B, A = pixelRGB

                brightness = sum([R, G, B]) / 3

                x = 0
                y = Y + 1

                ascii.convert_num(brightness, col, R, G, B)
                if col:
                    print_chars_C()
                else:
                    print_chars_BW()
                pixel_check(x, y, imgx, imgy)
            elif Y > imag1.height:
                print("")
        else:
            print('')

    def print_chars_BW():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print(" ".join(ascii.art))
        ascii.art.clear()


    def print_chars_C():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print("".join(ascii.art))
        ascii.art.clear()

    if imgx > 215:
        print("Can't have image bigger than 215")
    else:
        pixel_check(0, 0, imgx, imgy)


def convert_photo(image, imgx):

    imag = Image.open(image)

    imag = imag.convert('RGBA')

    # coordinates of the pixel
    imgy = (int(imag.size[1])) * (int(imgx) / (int(imag.size[0])))
    imag1 = imag.resize((imgx, int(imgy)))
    print(imag.size)
    print(imag1.size)

    def pixel_check(X, Y, imgx, imgy):
        col = True
        if Y < imag1.height:
            if X < imag1.width:
                pixelRGB = imag1.getpixel((X, Y))
                # print(imag.getpixel((X,Y)))
                R, G, B, A = pixelRGB

                brightness = sum([R, G, B]) / 3

                x = X + 1
                y = Y
                # print(x,y)
                ascii.convert_num2(R, G, B)
                pixel_check(x, y, imgx, imgy)
            elif X == imag1.width and Y <= imag1.height:
                pixelRGB = imag.getpixel((X, Y))
                R, G, B, A = pixelRGB

                brightness = sum([R, G, B]) / 3

                x = 0
                y = Y + 1
                # print(y)
                ascii.convert_num2(R, G, B)
                if col:
                    print_chars_C()
                else:
                    print_chars_BW()
                pixel_check(x, y, imgx, imgy)
            elif Y > imag1.height:
                print("")
            else:
                print("")
        else:
            print("")

    def print_chars_BW():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print(" ".join(ascii.art))
        ascii.art.clear()


    def print_chars_C():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print("".join(ascii.art))
        ascii.art.clear()


    if imgx > 215:
        print("Can't have image bigger than 215")
    else:
        pixel_check(0, 0, imgx, imgy)


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

    image = "opencv_frame_0.png"
    imag = Image.open(image)

    imag = imag.convert('RGBA')

    imgy = (int(imag.size[1])) * (int(imgx) / (int(imag.size[0])))
    imag1 = imag.resize((imgx, int(imgy)))

    def pixel_check2(X, Y, imgx, imgy, type):
        if Y < imag1.height:
            if X < imag1.width:
                pixelRGB = imag1.getpixel((X, Y))

                R, G, B, A = pixelRGB

                brightness = sum([R, G, B]) / 3

                x = X + 1
                y = Y

                if type:
                    ascii.convert_num(brightness, col, R, G, B)
                else:
                    ascii.convert_num2(R, G, B)
                pixel_check2(x, y, imgx, imgy,type)
            elif X == imag1.width and Y <= imag1.height:
                pixelRGB = imag.getpixel((X, Y))
                R, G, B, A = pixelRGB

                brightness = sum([R, G, B]) / 3

                x = 0
                y = Y + 1

                if type:
                    ascii.convert_num(brightness, col, R, G, B)
                else:
                    ascii.convert_num2(R, G, B)
                if col:
                    print_chars_C()
                else:
                    print_chars_BW()
                pixel_check2(x, y, imgx, imgy,type)
            elif Y > imag1.height:
                print("")
            else:
                print('')
        else:
            print("")

    def print_chars_BW():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print(" ".join(ascii.art))
        ascii.art.clear()

    def print_chars_C():
        if len(ascii.art) > imgx:
            del (ascii.art[-1])
        print("".join(ascii.art))
        ascii.art.clear()

    if imgx > 215:
        print("Can't have image bigger than 215")
    else:
        pixel_check2(0, 0, imgx, imgy,type)
