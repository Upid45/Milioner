win = False
secret_word = input("Введите слово для игры: ")
print("\033[2J")
true_letters = []
all_letters = []
point = [0, 0, 0]
counter = 0
while win == False:
    current_word = "".join([letter if letter in true_letters else "*" for letter in secret_word])
    print(f"Слово: {current_word}")
    if "*" not in current_word:
        print("Winner, Winner, chicken dinner.")
        win = True
        continue
    print(f"Ход игрока {counter + 1}. Очки: {point}")
    letter = input("Введите букву: ")
    if letter in all_letters:
        print("Вы уже вводили эту букву")
    else:
        all_letters.append(letter)
        if letter in secret_word:
            print("Буква была отгадана.")
            true_letters.append(letter)
            point[counter] += 10 
        else:
            print("Буква не отгадана")
    counter = (counter + 1) % 3
print(f"""Финальные очки: Игрок 1 = {point[0]}
                Игрок 2 = {point[1]}
                Игрок 3 = {point[2]}""")