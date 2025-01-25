from string import printable
import random

status = False
while True:
    password_length = int(input("Введите введите длинну пароля которую хотите: "))
    if password_length >= 64:
        print("Это слишком длинный пароль")
    elif password_length <= 4:
        print("Это слишком короткий пароль")
    else:
        break
while status == False:
    all_characters = list(printable)[:-6]
    password = "".join(random.choice(all_characters) for password in range(password_length))
    print(password)
    answer = int(input("""Данный пароль вас удовлетворяет?
                    1. Да
                    2. Нет
                    """))
    if answer == 1:
        print(f"Ваш пароль теперь: {password}")
        status = True
    elif answer == 2:
        print("Вот новая версия пароля: \n")
    else:
        break
