# # task 1
# i = 1
# n = int(input("Too: "))
# while i <= n:
#     print(i)
#     i += 1
# # task 2
# i = 1
# n = int(input("Too: "))
# while n >= i:
#     print(n)
#     n -= 1
# # task 3
# i = 0
# n = int(input("Too: "))
# while i <= n:
#      i += 2
#      print(i)
# # task 4 
# i = 1
# n = int(input("Too: "))
# while i <= n:
#     print(i)
#     i += 2
# # task 5
# i = 1
# total = 0
# n = int(input("Too: "))
# while i <= n:
#     total += i
#     i += 1
# print(total)
# # task 6
# i = 1
# total = 0
# n = int(input("Too: "))
# while i <= n:
#     i += 1
#     if i % 2 == 0:
#         total += i
#         print(total)
# # task 7
# i = 1
# n = int(input("Too: "))
# while i <= n:
#     i += 1
#     if i % 3 == 0:
#         print(i)
# # task 8
# n = int(input("Heden too oruulah: "))
# i = 0
# eyreg = 0
# sorog = 0
# zero = 0
# while i < 4:
#     too = int(input("Too: "))
#     if n > 0:
#         eyreg += 1
#     elif n == 0:
#         zero += 1
#     elif n < 0:
#         sorog +=1
#     i += 1
# print("eyreg too: ", eyreg)
# print("sorog too: ", sorog)
# print("0 tei tentsuu: ", zero)
# # task 9
# n = int(input("heden too awah we:" ))
# i = 0
# total = 0
# while i < n:
#     too = int(input("Too: "))
#     if too > 0:
#         total += too
#         i += 1
# print("Eyreg tooni niilber: ", total)
# # task 10
# n = int(input("heden too oruulah we: "))
# i = 0
# ih = 0
# while i < n:
#     too = int(input("Too: "))
#     if too > ih:
#         ih = too
#         i += 1
# print("hamgiin ih utga", ih)
# # task 11
# n = int(input("heden too awah we?: "))
# i = 1
# baga = int(input("Too: "))
# while i < n:
#     too = int(input("Too: "))
#     if too < baga:
#         baga = too
#     i += 1
# print("hamgiin baga too:", baga)
# # task 12
# n = int(input("hden too awh we?: "))
# i = 0
# yes = 0
# while i < n:
#     too = int(input("Too: "))
#     if too % 5 == 0 or too % 3 == 0:
#         yes = too
#     i += 1
# print("3, 5 huwagdah toonud", yes)
# # task 13
# n = int(input("Too: "))
# count = 0
# while n != 0:
#     n = n // 10
#     count += 1
# print("Tsifriin too:", count)
# # task 14
# n = int(input("Too: "))
# total = 0
# i = 0
# if n < 0:
#     n = -n 
# while n > 0:
#     i = n % 10
#     total += i
#     n //= 10
# print(total)
# # task 15
# n = int(input("Too: "))
# reverse = 0
# too = 0
# while n > 0:
#     too = n % 10
#     reverse = reverse * 10 + too
#     n //= 10
# print(reverse)
# # task 16
# n = int(input("Too: "))
# pln = n
# too = 0
# while n > 0:
#     jj = n % 10
#     too = too * 10 + jj
#     n //= 10
# if pln == too:
#     print("Palindrom")
# else:
#     print("hud")
# ######################
# # task 17
# n = int(input("Too: "))
# i = 2
# atoo = True
# while i < n:
#     if n % i == 0:
#         atoo = False
#     i += 1
# if n < 2:
#     atoo = False
# if atoo:
#     print("Anhnii too")
# else:
#     print("Anhnii too bish")
# # task 18
# qwe = 0
# n = int(input("Too: "))
# for qwe in range(2, n + 1):
#     atoo = True
#     for i in range(2, qwe):
#         if qwe % i == 0:
#             atoo = False
#     if atoo:
#         print(qwe)
# # task 19
# n = int(input("Too: "))
# i = 1
# while i <= 10:
#     print(n, "*", i, "=", i)
#     i += 1
# # task 20
# correct = "python1234"
# n = input("Password: ")
# while True:
#     password = input("Try agian: ")
#     if password != "python1234":
#         print("wrong password")
#     else:
#         print("Correct password")
#         break 