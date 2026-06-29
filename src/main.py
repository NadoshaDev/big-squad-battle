# Big Squad Battle
# Initial game core

player_squads = [10, 8, 7, 9, 6]
computer_squads = [11, 13, 10, 1, 5]

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
    print("Увы, в следующий раз повезёт, компьютер победил со счётом", computer_score)
else:
    print("Боевая ничья")
