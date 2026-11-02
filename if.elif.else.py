# # task 2


# a, b, c = map(int , input("C: ").split())
# if a*a + b*b <= c*c:
#     print("not trangle")
# if a == b == c:
#     print("equilateral")
# if a == b or b == c or a == c:
#     print("isosceles")
# if a != b or a != c or b != c:
#     print("scelene")


# # task 3


# nas = int(input("Nas: "))
# odor = input("Odriin torol: ")
# if nas < 12 or nas > 60:
#     print(5000)
# elif odor == "weekend":
#     print(12000)
# elif odor == "weekday":
#     print(10000)


# # task 4


# ner = input("Username: ")
# password = input("Password: ")
# tolow = input("tolow: ")
# if ner == "admin" and password == "1234":
#     if tolow == "blocked":
#         print("Acount blocked")
#     else:
#         print("wellcome")
# else:
#     print("LOGIN FAILED")        


# # task 5


# x1, y1, x2, y2 = map(int, input("Too: ").split())
# x, y = map(int, input("Too: ").split())
# if x1 <= x < x2 and y1 <= y <=y2:
#     print("inside")
# else:
#     print("outside")   


# # task 6


# a1, b1, a2, b2 = map(int, input("Too: ").split())
# if a1 <= b2 and a2 <= b1:
#     print("yes")
# else:
#     print("no")


# # task 7


# day, month, year = map(int, input("Date: ").split())
# if month < 1 or month > 12 or day < 1:
#     print("invalid")
# elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     if day <= 31:
#         print("valid")
#     else:
#         print("invalid")
# elif month == 4 or month == 11 or month == 6 or month == 9:
#     if day <=30:
#         print("valid")
#     else:
#         print("invalid")
# elif month == 2:
#     if year % 400 == 0 or year % 4 == 0 or year %100 != 0:
#         if day <= 29:
#             print("valid")
#         else:
#             print("invalid")
#     else:
#         if day <= 28:
#             print("valid")
#         else:
#             print("invalid")


# # task 8


# r, c = map(int, input("Too: ").split())
# if r < 1 or r > 8 or c < 1 or c > 8:
#     print("invalid")
# elif r + c % 2 == 0:
#     print("black")
# else:
#     print("white")    


# # task 9


# dun, irts, sahilga = map(int, input("too: ").split())
# if dun > 90 and irts > 95 and sahilga == 0:
#     print("full")
# elif dun > 80 and irts > 90 and sahilga <= 1:
#     print("half")
# else:
#     print("none")     
# 
#    
# # task 10


# p1 = input("p1: ")
# p2 = input("p2: ")
# if p1 == p2:
#     print("draw")
# elif p1 == "scissors" and p2 == "rock":
#     print("p2")
# elif p2 == "scissors" and p1 == "rock":
#     print("p1")
# elif p1 == "scissors" and p2 == "paper":
#     print("p1")
# elif p2 == "scissors" and p1 == "paper":
#     print("p2")
# elif p1 == "paper" and p2 == "rock":
#     print("p1")   
# elif p2 == "paper" and p1 == "rock":
#     print("p2") 
