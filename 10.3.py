 #Задача 3
# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то,что есть разные выигрышные варианты и программа должна их распознавать.




Doska = [
    ['o', 'o', 'x'],
    ['x', 'o', 'o'],
    ['x', 'x', 'o']
]

n = 0

for i, i_value in enumerate(Doska):
    V = 0   #hod vas
    P = 0   #hod pet

    for j, j_value in enumerate(i_value):
        if str(Doska[i][j]) == 'x':
            V += 1
        elif str(Doska[i][j]) == 'o':  #
            V -= 1
        if str(Doska[j][i]) == 'x':
            P += 1
        elif str(Doska[j][i]) == 'o':
            P -= 1

        if str(Doska[0][0]) == str(Doska[1][1]) == str(Doska[2][2]) == 'x' or str(Doska[0][2]) == str(Doska[2][0]) == str(Doska[1][1]) == 'x':
            n += 1
        if str(Doska[0][0]) == str(Doska[1][1]) == str(Doska[2][2]) == 'o' or str(Doska[0][2]) == str(Doska[2][0]) == str(Doska[1][1]) == 'o':
            n -= 1

        if V == 3 or P == 3 or n == 3: #
            print("x win")
            exit()

        elif V == -3 or P == -3 or n == -3:#
            print("o win")
            exit()


else:

    print("Ничья")



