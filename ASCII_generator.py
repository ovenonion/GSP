art = []

def convert_num(avg_brightness,col_on,R,G,B):
  char = ['@','$','%','#','o','*','+','=','~','-',':',',','.']
  if col_on == False:
      if avg_brightness < 20:
            art.append(char[0])
      elif 40>=avg_brightness>20:
            art.append(char[1])
      elif 60>=avg_brightness>40:
            art.append(char[2])
      elif 80>=avg_brightness>60:
            art.append(char[3])
      elif 100>=avg_brightness>80:
            art.append(char[4])
      elif 120>=avg_brightness>100:
            art.append(char[5])
      elif 140>=avg_brightness>120:
            art.append(char[6])
      elif 160>=avg_brightness>140:
            art.append(char[7])
      elif 180>=avg_brightness>160:
            art.append(char[8])
      elif 200>=avg_brightness>180:
            art.append(char[9])
      elif 220>=avg_brightness>200:
            art.append(char[10])
      elif 240>=avg_brightness>220:
            art.append(char[11])
      else:
            art.append(char[12])
  if col_on == True:
      if avg_brightness < 20:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[0])
            art.append(letter)
      elif 40>=avg_brightness>20:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[1])
            art.append(letter)
      elif 60>=avg_brightness>40:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[2])
            art.append(letter)
      elif 80>=avg_brightness>60:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[3])
            art.append(letter)
      elif 100>=avg_brightness>80:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[4])
            art.append(letter)
      elif 120>=avg_brightness>100:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[5])
            art.append(letter)
      elif 140>=avg_brightness>120:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[6])
            art.append(letter)
      elif 160>=avg_brightness>140:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[7])
            art.append(letter)
      elif 180>=avg_brightness>160:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[8])
            art.append(letter)
      elif 200>=avg_brightness>180:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[9])
            art.append(letter)
      elif 220>=avg_brightness>200:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[10])
            art.append(letter)
      elif 240>=avg_brightness>220:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[11])
            art.append(letter)
      else:
            letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,char[12])
            art.append(letter)

def convert_num2(R,G,B):

  letter = "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R,G,B,'■')
  art.append(letter)






