alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
alphabet_en = "abcdefghijklmnopqrstuvwxyz "
ru_en = int(input("Choise the language: \n 1. Ru \n 2. En \n"))
if ru_en == 1:
    ru_en = alphabet_ru
elif ru_en == 2:
    ru_en = alphabet_en
else:
    ru_en = alphabet_ru
word = input("Введите слово которое хотите зашифровать: ").lower()
step = int(input("Введите число на которое хотите сделать сдвиг: "))
chipher = [ru_en.find(char) + step for char in word] 
print(chipher)
result = "".join(ru_en[index - step] for index in chipher)
print(result)