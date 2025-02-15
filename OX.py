win_state = False
counter = 0
field = list(range(1, 10))
All_winn = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (2, 5, 8), (3, 5, 7), (1, 4, 7), (3, 6, 9))
while not win_state:
    for index in range(0, 7, 3):
        print(field[index], field[index + 1], field[index + 2])
    if counter % 2 == 0:
        player = "X"
    else:
        player = "O"
    print(f"Ход игрока {player}")

    position = int(input("Выберите клетку (1-9): ")) - 1

    if field[position] == "X" or field[position] == "O":
        print("Клетка уже занята, выберите другую.")
        counter -= 1
    else:
        field[position] = player
        for combo in All_winn:
            a, b, c = combo[0] - 1, combo[1] - 1, combo[2] - 1
            if field[a] == field[b] == field[c]:
                win_state = True
                print(f"Игрок {player} выиграл!")
                break
    counter += 1
    if counter == 9 and not win_state:
        win_state = True
        print("Ничья!")