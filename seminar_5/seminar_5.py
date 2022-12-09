# with open('text.txt', 'r', encoding='utf8')as file:
#     text = file.readline().lower()
#
# while 'абв' in text:
#     text = text.replace('абв', '')
# print(text)
# ==================================================
# map = [1, 2, 3,
#        4, 5, 6,
#        7, 8, 9]
#
# vic = [[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8],
#        [0, 3, 6],
#        [1, 4, 7],
#        [2, 5, 8],
#        [0, 4, 8],
#        [2, 4, 6]]
#
# def print_maps():
#     print(map[0], end=" ")
#     print(map[1], end=" ")
#     print(map[2])
#
#     print(map[3], end=" ")
#     print(map[4], end=" ")
#     print(map[5])
#
#     print(map[6], end=" ")
#     print(map[7], end=" ")
#     print(map[8])
#
# def step_maps(step, symbol):
#     ind = map.index(step)
#     map[ind] = symbol
#
# def result():
#     win = ""
#
#     for i in vic:
#         if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
#             win = "X"
#         if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
#             win = "O"
#
#     return win
#
# game_over = False
# player1 = True
#
# while game_over == False:
#     print_maps()
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Игрок 1, ставь крестик: "))
#     else:
#         symbol = "O"
#         step = int(input("Игрок 2, ставь нолик: "))
#
#     step_maps(step, symbol)
#     win = result()
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
#
#     player1 = not (player1)
#
# print_maps()
# print("Молодец, ты выиграл", win)
# ===================================================
# def code(message):
#     st = ""
#     i = 0
#     while i <= len(message) - 1:
#         count = 1
#         ch = message[i]
#         j = i
#         while j < len(message) - 1:
#             if message[j] == message[j + 1]:
#                 count = count + 1
#                 j = j + 1
#             else:
#                 break
#         st = st + str(count) + ch
#         i = j + 1
#     return st
#
# print(code('AuuBBBCCCCCCcccccCCGGGGGgggggqqqqqqqqqqqqqqaaaaaaaCCA'))
# ==================================================================