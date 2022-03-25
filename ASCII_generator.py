art = []

def test():
    print("The code works")

def convert_num2(avg_brightness):
    char = ['Ñ','@','#','W','$','9','8','7','6','5','4','3','2','1','0','?','!','a','b','c', ';',':','+','=','-',',','.']
    if avg_brightness < 10:
        art.append(char[0])
    elif 20>=avg_brightness>10:
        art.append(char[1])
    elif 30>=avg_brightness>20:
        art.append(char[2])
    elif 40>=avg_brightness>30:
        art.append(char[3])
    elif 50>=avg_brightness>40:
        art.append(char[4])
    elif 60>=avg_brightness>50:
        art.append(char[5])
    elif 70>=avg_brightness>60:
        art.append(char[6])
    elif 80>=avg_brightness>70:
        art.append(char[7])
    elif 90>=avg_brightness>80:
        art.append(char[8])
    elif 100>=avg_brightness>90:
        art.append(char[9])
    elif 110>=avg_brightness>100:
        art.append(char[10])
    elif 120>=avg_brightness>110:
        art.append(char[11])
    elif 130>=avg_brightness>120:
        art.append(char[12])
    elif 140>=avg_brightness>130:
        art.append(char[13])
    elif 150>=avg_brightness>140:
        art.append(char[14])
    elif 160>=avg_brightness>150:
        art.append(char[15])
    elif 170>=avg_brightness>160:
        art.append(char[16])
    elif 180>=avg_brightness>170:
        art.append(char[17])
    elif 190>=avg_brightness>180:
        art.append(char[18])
    elif 200>=avg_brightness>190:
        art.append(char[19])
    elif 210>=avg_brightness>200:
        art.append(char[20])
    elif 220>=avg_brightness>210:
        art.append(char[21])
    elif 230>=avg_brightness>220:
        art.append(char[22])
    elif 240>=avg_brightness>230:
        art.append(char[23])
    elif 254>=avg_brightness>240:
        art.append(char[24])
    elif avg_brightness == 255:
        art.append(" ")
    elif 260>=avg_brightness>255:
        art.append(char[25])
    elif 270>=avg_brightness>260:
        art.append(char[26])

def convert_num(avg_brightness):
    char = ['Ñ','@','8','&','W','#','o','a','h','k','b','d','p','q','w','m', '/','|','(','1','{','[','-',',','.']
    if avg_brightness < 10:
        art.append(char[0])
    elif 20>=avg_brightness>10:
        art.append(char[1])
    elif 30>=avg_brightness>20:
        art.append(char[2])
    elif 40>=avg_brightness>30:
        art.append(char[3])
    elif 50>=avg_brightness>40:
        art.append(char[4])
    elif 60>=avg_brightness>50:
        art.append(char[5])
    elif 70>=avg_brightness>60:
        art.append(char[6])
    elif 80>=avg_brightness>70:
        art.append(char[7])
    elif 90>=avg_brightness>80:
        art.append(char[8])
    elif 100>=avg_brightness>90:
        art.append(char[9])
    elif 110>=avg_brightness>100:
        art.append(char[10])
    elif 120>=avg_brightness>110:
        art.append(char[11])
    elif 130>=avg_brightness>120:
        art.append(char[12])
    elif 140>=avg_brightness>130:
        art.append(char[13])
    elif 150>=avg_brightness>140:
        art.append(char[14])
    elif 160>=avg_brightness>150:
        art.append(char[15])
    elif 170>=avg_brightness>160:
        art.append(char[16])
    elif 180>=avg_brightness>170:
        art.append(char[17])
    elif 190>=avg_brightness>180:
        art.append(char[18])
    elif 200>=avg_brightness>190:
        art.append(char[19])
    elif 210>=avg_brightness>200:
        art.append(char[20])
    elif 220>=avg_brightness>210:
        art.append(char[21])
    elif 230>=avg_brightness>220:
        art.append(char[22])
    elif 240>=avg_brightness>230:
        art.append(char[23])
    elif 250>=avg_brightness>240:
        art.append(char[24])
    elif avg_brightness == 255:
        art.append(" ")


def print_chars():
    print("  ".join(art))
    art.clear()
