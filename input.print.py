# # task 1


a = int(input("Sekund: "))
b = a // 60
ts = b // 60
minn = b - (ts * 60)
sek = a % 60
print(ts, "tsag")
print(minn, "min")
print(sek, "sekund")


# # task 2


# ts = int(input("tsag: "))
# min = int(input("min: "))
# sec = int(input("sekund: "))
# a = ts *60 * 60
# b = min * 60
# d = a + b +sec
# print(d, "sekund")


# # task 3


# ts = int(input("Tsag: "))
# min = int(input("Minute: "))
# a = ts * 60
# b = a + min
# print(b, "minute")


# # task 4


# a = int(input("Too: "))
# eo = a // 100
# so = a % 10
# do1 = a % 100
# do2 = do1 // 10
# print(so*100+do2*10+eo)


# # task 5


# a = int(input("Too: "))
# eo = a // 100
# so = a % 10
# do1 = a % 100
# do2 = do1 // 10
# print(eo*so*do2)


# # task 6


# a = int(input("Too: "))
# do1 = a % 100
# do2 = do1 // 10
# print(do2)


# # task 7


# a = int(input("Too: "))
# eo = a // 100
# so = a % 10
# total = eo * so
# print(total)


# # task 8


# a = int(input("Too: "))
# eo = a // 100
# so = a % 10
# do1 = a % 100
# do2 = do1 // 10
# print(eo, do2, so)


# # task 9


# a = int(input("Too: "))
# eo = a // 1000
# ho1 = a // 100
# ho2 = ho1 % 10
# go1 = a % 100
# go2 = go1 // 10
# do = a % 10
# print(eo+ho2+go2+do)


# # task 10


# n = int(input("Too: "))
# a = n // 1000
# n = n % 1000
# b = n // 500
# n = n % 500
# c = n // 100
# print(a, b, c)


# # task 11


# a, b = map(int, input("Too: ").split())
# print(b, a)


# # task 12


# a = int(input("Too: "))
# b = a // 10
# c = a % 10
# print(c*10+b)


# # task 13


# n = int(input("Cm: "))
# a = n // 100
# b = n % 100
# print(a, b)


# # task 14


# n = int(input())
# day = n // 1440
# n = n % 1440
# hour = n // 60
# minute = n % 60
# print(day, hour, minute)


# # task 15


# n = int(input())
# myangat = n // 1000
# zuut = (n // 100) % 10
# aravt = (n // 10) % 10
# negj = n % 10
# print(myangat, zuut, aravt, negj)

# # task 1

# y = int(input("Jil: "))
# if y % 400 == 0 or (y % 4 == 0 and y % 100 > 0):
#     print("YES")
# else:
#     print("NO")

# # task 2

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a + b <= c or a + c <= b or b + c <= a:
#     print("NOT A TRIANGLE")
# elif a == b and b == c:
#     print("Equilateral")
# elif a == b or a == c or b == c:
#     print("Isosceles")
# else:
#     print("Scalene")

# # task3

# age = int(input("Nas: "))
# day = input("Odor: ")
# if age < 12 or age > 60:
#     print(5000)
# elif day == "weekend":
#     print(12000)
# else:
#     print(10000)

# # task 4
 
# name = input("Ner: ")
# password = input("Nuuts ug: ")
# status = input("Tolow: ")
# if name == "admin" and password == "1234":
#     if status == "blocked":
#         print("ACCOUNT BLOCKED")
#     else:
#         print("WELCOME")
# else:
#     print("LOGIN FAILED")

# # task 5

# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# x = int(input("x: "))
# y = int(input("y: "))
# if x1 <= x <= x2 and y1 <= y <= y2:
#     print("INSIDE")
# else:
#     print("OUTSIDE")

# # task 6

# a1 = int(input("a1: "))
# b1 = int(input("b1: "))
# a2 = int(input("a2: "))
# b2 = int(input("b2: "))
# if a1 <= b2 and a2 <= b1:
#     print("YES")
# else:
#     print("NO")

# # task 7


# d = int(input("Odor: "))
# m = int(input("Sar: "))
# y = int(input("Jil: "))
# if y < 1 or m < 1 or m > 12 or d < 1:
#     print("INVALID")
# elif m == 2:
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 > 0):
#         if d <= 29:
#             print("VALID")
#         else:
#             print("INVALID")
#     elif d <= 28:
#         print("VALID")
#     else:
#         print("INVALID")
# elif m == 4 or m == 6 or m == 9 or m == 11:
#     if d <= 30:
#         print("VALID")
#     else:
#         print("INVALID")
# else:
#     if d <= 31:
#         print("VALID")
#     else:
#         print("INVALID")

# # task 8

# r = int(input("Mor: "))
# c = int(input("Bagana: "))
# if r < 1 or r > 8 or c < 1 or c > 8:
#     print("INVALID")
# elif (r + c) % 2 == 0:
#     print("Black")
# else:
#     print("White")
# # task 9

# score = int(input("Dun: "))
# attendance = int(input("Irts: "))
# violation = int(input("Zorchil: "))
# if score >= 90 and attendance >= 95 and violation == 0:
#     print("FULL")
# elif score >= 80 and attendance >= 90 and violation <= 1:
#     print("HALF")
# else:
#     print("NONE")
# # task 10
# a = input("Player 1: ")
# b = input("Player 2: ")
# if a == b:
#     print("Draw")
# elif a == "rock" and b == "scissors":
#     print("Player 1")
# elif a == "paper" and b == "rock":
#     print("Player 1")
# elif a == "scissors" and b == "paper":
#     print("Player 1")
# else:
#     print("Player 2")




# # task 1

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
# print(a, b, c)

# # task 2

# h1 = int(input("Ehnii tsag: "))
# m1 = int(input("Ehnii minut: "))
# h2 = int(input("Suuliin tsag: "))
# m2 = int(input("Suuliin minut: "))
# a = h1 * 60 + m1
# b = h2 * 60 + m2
# if b < a:
#     b = b + 1440
# d = b - a
# h = d // 60
# m = d % 60
# print(h, m)

# # task 3

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a + b <= c or a + c <= b or b + c <= a:
#     print("NOT A TRIANGLE")
# else:
#     if a > c:
#         a, c = c, a
#     if b > c:
#         b, c = c, b
#     if a*a + b*b == c*c:
#         print("Right")
#     elif a*a + b*b > c*c:
#         print("Acute")
#     else:
#         print("Obtuse")

# # task 4

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a == 0:
#     if b == 0:
#         if c == 0:
#             print("INF")
#         else:
#             print("NO ROOTS")
#     else:
#         print("ONE ROOT")
# else:
#     d = b*b - 4*a*c
#     if d > 0:
#         print("TWO ROOTS")
#     elif d == 0:
#         print("ONE ROOT")
#     else:
#         print("NO ROOTS")

# # task 5

# d = int(input("Odor: "))
# m = int(input("Sar: "))
# y = int(input("Jil: "))
# if m == 2:
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 > 0):
#         days = 29
#     else:
#         days = 28
# elif m == 4 or m == 6 or m == 9 or m == 11:
#     days = 30
# else:
#     days = 31
# d = d + 1
# if d > days:
#     d = 1
#     m = m + 1
# if m > 12:
#     m = 1
#     y = y + 1
# print(d, m, y)

# # tasdk 6

# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# x3 = int(input("x3: "))
# y3 = int(input("y3: "))
# x4 = int(input("x4: "))
# y4 = int(input("y4: "))
# if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
#     print("NO")
# else:
#     print("YES")

# # task 7

# h = int(input("Tsag: "))
# m = int(input("Minut: "))
# d = int(input("Zoruu: "))
# h = h + d
# if h >= 24:
#     h = h - 24
#     day = "Tomorrow"
# elif h < 0:
#     h = h + 24
#     day = "Yesterday"
# else:
#     day = "Today"
# print(h, m)
# print(day)

# # task 8

# a = int(input("Bag 1: "))
# b = int(input("Bag 2: "))
# if a == 25 and b <= 23:
#     print("Player 1")
# elif b == 25 and a <= 23:
#     print("Player 2")
# elif a >= 26 and b >= 24 and a - b == 2:
#     print("Player 1")
# elif b >= 26 and a >= 24 and b - a == 2:
#     print("Player 2")
# elif a <= 24 and b <= 24:
#     print("Not finished")
# elif a >= 24 and b >= 24 and a - b <= 1 and b - a <= 1:
#     print("Not finished")
# else:
#     print("Invalid")

# # task 9

# piece = input("Huu: ")
# r1 = int(input("r1: "))
# c1 = int(input("c1: "))
# r2 = int(input("r2: "))
# c2 = int(input("c2: "))
# if r1 < 1 or r1 > 8 or c1 < 1 or c1 > 8 or r2 < 1 or r2 > 8 or c2 < 1 or c2 > 8:
#     print("INVALID")
# elif r1 == r2 and c1 == c2:
#     print("NO")
# else:
#     dr = r2 - r1
#     dc = c2 - c1
#     if dr < 0:
#         dr = 0 - dr
#     if dc < 0:
#         dc = 0 - dc
#     if piece == "king" and dr <= 1 and dc <= 1:
#         print("YES")
#     elif piece == "rook" and (dr == 0 or dc == 0):
#         print("YES")
#     elif piece == "bishop" and dr == dc:
#         print("YES")
#     elif piece == "queen" and (dr == 0 or dc == 0 or dr == dc):
#         print("YES")
#     elif piece == "knight" and ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
#         print("YES")
#     else:
#         print("NO")

# # task 10

# a1, a2, a3 = input("Mor 1: ").split()
# b1, b2, b3 = input("Mor 2: ").split()
# c1, c2, c3 = input("Mor 3: ").split()
# if (a1 == a2 == a3 == "X" or b1 == b2 == b3 == "X" or c1 == c2 == c3 == "X" or a1 == b1 == c1 == "X" or a2 == b2 == c2 == "X" or a3 == b3 == c3 == "X" or a1 == b2 == c3 == "X" or a3 == b2 == c1 == "X"):
#     print("X wins")
# elif (a1 == a2 == a3 == "O" or b1 == b2 == b3 == "O" or c1 == c2 == c3 == "O" or a1 == b1 == c1 == "O" or a2 == b2 == c2 == "O" or a3 == b3 == c3 == "O" or a1 == b2 == c3 == "O" or a3 == b2 == c1 == "O"):
#     print("O wins")
# elif (a1 == "." or a2 == "." or a3 == "." or b1 == "." or b2 == "." or b3 == "." or c1 == "." or c2 == "." or c3 == "."):
#     print("Not finished")
# else:
#     print("Draw")
















