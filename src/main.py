import random

player_squads = []
player_remaining = 40


for i in range(4):
    number_squad = i + 1
    print(f"Формируется {number_squad} отряд")
    
    while True:

        user_input = input(f"Введите количество воинов (от 0 до {player_remaining}):")
        try:    
            quantity_warrior = int(user_input)

            if quantity_warrior < 0:
                print("Ошибка! Количество воинов не может быть отрицательным.")
                continue

            if quantity_warrior > player_remaining:
                print(f"Ошибка! Можно распределить не более {player_remaining} воинов.")
                continue
            
            break

        except ValueError:
            print("Ошибка ввода! Введите целое число.")                       
    player_squads.append(quantity_warrior)
    player_remaining -= quantity_warrior
    print(f"В {number_squad} отряд добавлено {quantity_warrior} воинов.")
        

print(f"В 5 отряд автоматически добавлено {player_remaining} воинов.")
player_squads.append(player_remaining)

computer_squads = []
computer_remaining = 40
for _ in range(4):
    random_number = random.randint(0, computer_remaining)
    computer_squads.append(random_number)
    computer_remaining -= random_number

computer_squads.append(computer_remaining)

player_score = 0
computer_score = 0

for i in range(len(player_squads)):
    if player_squads[i] > computer_squads[i]:
        player_score += 1
    elif player_squads[i] < computer_squads[i]:
        computer_score += 1

if player_score > computer_score:
    print("Игрок победил со счётом", player_score)
elif player_score < computer_score:
   print("Компьютер победил со счётом", computer_score)
   print("Удачи в следующей игре!")
else:
    print("Боевая ничья")
