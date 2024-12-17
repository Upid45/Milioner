import time
import string

color_name_black = "\u001b[30m"
color_name_red = "\u001b[31m"
color_name_green = "\u001b[32m"
color_name_yellow = "\u001b[33m"
color_name_blue = "\u001b[34m"
color_name_white = "\u001b[37m"

colorized_txt = input("""
                   Select one of the colors from the list
                   Type it exactly as it will be written below:
                   Green
                   Blue
                   Red
                   White
                   Yellow
                   Black
                   """)
if colorized_txt == "Green":
    color_name = color_name_green
    print(f"{color_name_green} Done")
elif colorized_txt == "Blue":
    color_name = color_name_blue
    print(f"{color_name_blue} Done")
elif colorized_txt == "Red":
    color_name = color_name_red
    print(f"{color_name_red} Done")
elif colorized_txt == "White":
    color_name = color_name_white
    print(f"{color_name_white} Done")
elif colorized_txt == "Yellow":
    color_name = color_name_yellow
    print(f"{color_name_yellow} Done")
elif colorized_txt == "Black":
    color_name = color_name_black
    print(f"{color_name_black} Done")
else:
    color_name = "\u001b[232m"
print(f"\u001b[0m")
original_txt = input("Введите сообщение: ")
length = len(original_txt)
print(length)
print(original_txt[-3:])
print(original_txt[:3])
color_start = int(input("Введите число после которого начнётся покраска \n"))
color_end = int(input("Введите второе число на котором закончится покраста \n"))
colorized_text = color_name + original_txt[color_start:color_end] + "\033[0m"
print(f"{original_txt[:color_start]}{colorized_text}{original_txt[color_end:]}")
old_char = input("Введите символ которую вы хотите заменить\n")
new_char = input(f"Введите символ на которую вы хотите заменить '{old_char}'\n")
moded_txt = original_txt.replace(f"{old_char}", f"{new_char}")
print(f"Заменённый текст :{moded_txt}")
# even_chars = (2, 4, 6, 8, 10, 12,)
# odd_chars = (1, 3, 5, 7, 9, 11,)
time.sleep(1)
print(f"Чётные символы:{original_txt[0::2]}")
print(f"Нечётные символы:{original_txt[1::2]}")
time.sleep(1)
print(original_txt[::-1])
time.sleep(1)
mid_index = int(length / 2)
swapped_txt = original_txt[mid_index: -mid_index]
print(original_txt[mid_index:], original_txt[:-mid_index])