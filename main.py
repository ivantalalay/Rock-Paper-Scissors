#02.02.2023
import random

count=0
for number in range(10):
    player=int(input('''Сделайте ход - 1-камень, 2-ножницы, 3-бумага 
'''))
    if player==1:
        print("Ваш ход - Камень")
    elif player==2:
        print("Ваш ход - ножницы")
    elif player==3:
        print("Ваш ход -  бумага")
    else:
        print("Выберите варианты выше перечисленных")
    comp=random.randint(1, 3)
    if comp==1:
        print("Ход компьютера - Камень")
    elif comp==2:
        print("Ход компьютера - Ножницы")
    elif comp==3:
        print("Ход компьютера -  Бумага")
    if player==1 and comp==1:
        print("Ничья")
    elif player==2 and comp==2:
        print("Ничья!")
    elif player==3 and comp==3:
        print("Ничья!")
    elif player==1 and comp==2:
        count+=1
        print("Вы победили!")
    elif player==1 and comp==3:
        print("Победил компьютер!")
    elif player==2 and comp==1:
        print("Победил компьютер!")
    elif player==2 and comp==3:
        count+=1
        print("Вы победили!")
    elif player==3 and comp==1:
        count+=1
        print("Вы победили!")
    elif player==3 and comp==2:
        print("Победил компьютер!")
    print("Ваши победы", count)
    if count==3:
        break
