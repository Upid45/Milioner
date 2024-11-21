# (Created) 14.11.2024 | (Updated) 20.11.2024
name_bot = "Darius"
print(f"Привет меня завут {name_bot}")
name_user = input("Как вас зовут? ")
print(f"Привет {name_user} приятно познакомиться!")
age_user = int(input("Сколько вам лет? "))
print(f"Представляешь через 10 лет тебе будет {age_user + 10}")
rise_user = float(input("Каков ваш рост? "))
print(f"Мой рост равен 0.63 метра, ты выше меня на {rise_user - 0.63}м")
print(f"""Теперь я знаю твой рост равный {rise_user}м, а так же как тебя зовут {name_user}.
      И ещё твой возраст {age_user}""")
answer = input("""Мои функции:
               1 - Рассказать анекдот.
               2 - Сказать сколько раз в день кормить питомца. 
               3 - Рассказать про лучшее место на земле. 
               Ваш выбор: """)
if answer == "1":  
    print("Колобок вышел на ринг и говорит: По голове не бить!")
elif answer == "2":   
    animal = input("""Это:
                   1. Собака
                   2. Кот
                   Ответ: """)
    if animal == "1":
        first = input("""Какого возроста ваша собака:
                      1. Менее года.
                      2. Более года.
                      Выберите одно: """)
        if first == "1":
            print("Рекомендуется 5-6 раз в день")
        elif first == "2":
            print("Нужно 2-3 раза в день, но можно и больше)")
        else:
            print("ERROR 400 Bad Request")
    elif animal == "2":
        second = input("""Какого возроста ваш кот:
                       1. Менее 7 месяцев.
                       2. Более года.
                       Ваш выбор: """)
        if second == "1":
            print("5-6 раз в день")
        elif second == "2":
            print("3-4 раза в день")
        else:
            print("ERROR 400 Bad Request")
    else:
        print("ERROR 400 Bad Request")
elif answer == "3":
    print("Оно дома. А вы не знали?")
else:
    print("ERROR 400 Bad Request")