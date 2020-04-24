import random
name = input("Введите свое имя: ")
print(name + ", добро пожаловать в рулетку!")
def game():
    option = input("Вы хотите поставить на число или цвет? ")
    if option == "число":
        bet = int(input("На какое число вы хотите поставить? "))
        if 1 <= bet <= 36:
            numb = random.randint(1, 37)
            print("Выпало число " + str(numb))
            if numb == bet:
                print("Поздравляем, вы выиграли!")
            else:
                print("Вы проиграли")
        else:
            print("Такое число нельзя указать")
    elif option == "цвет":
        color = input("На какой цвет вы хотите поставить? ")
        if color == 'красный' or color == "черный":
            col = random.choice(['красный', 'черный'])
            print("Выпал цвет " + str(col))
            if color == col:
                print("Поздравляем, вы выиграли!")
            else:
                print("Вы проиграли")
        else:
            print("Такой цвет нельзя указать")
    game()
game()


