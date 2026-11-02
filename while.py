# # task 111111111111111111111111111111111
# i = 0
# for i in range (1, 11):
#     print(i)
# # task 22222222222222222222222222222222
# i = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
# # task 33333333333333333333333333333333333
# i = 0
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)
# # task 44444444444444444444444444444
# i = 0
# for i in range(1, 11):
#     print(f"5 * {i} = {i*5}")
#     i += 1
# # task 55555555555555555555555555555
# i = 1
# n = int(input("Too: "))
# while i < n:
#     i += 1
#     print(i)
# # task 6666666666666666666666666666
# i = 0
# n = int(input("Too: "))
# while i < n:
#     print(n)
#     n -= 1
# # task 777777777777777777777777777777
# i = 1
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i)
# # task 88888888888888888888888888
# i = 1
# for i in range(1, 51):
#     if i % 5 != 0:
#         print(i)
# # task 9999999999999999999999999999
# i  = 0
# count = 0
# for i in range(1, 101):
#     if i % 2 ==0:
#         count+=1
# print(count)
# # task 10
# i = 0 
# count = 0
# for i in range(1, 101):
#     if i % 7 == 0:
#         count += 1
# print(count)
# # task 11
# i = 0
# total = 0
# for i in range(1, 101):
#     total += i
#     print(total)
# # task 12
# i = 0
# total = 0
# for i in range(1, 101):
#     if i % 2 ==0:
#         total += i
#     print(total)
# # task 13
# i = 0
# while i < 10:
#     i += 1
#     print(i)
# # task 14
# i = 10
# while i >= 1:
#     i -= 1
#     print(i)
# # task 15
# i = 2
# while i <= 20:
#     print(i)
#     i += 2
# # task 16
# n = int(input("Too: "))
# i = 0
# total = 0
# while n > i:
#     i += 1
#     total += i
#     print(total)
# # task 17
# n = int(input("Too: "))
# count = 0
# while n > 0:
#     n //= 10
#     count += 1
# print(count)
# # task 18
# n = int(input("Too: "))
# total = 0
# a = 1
# while n > 0:
#     a = n % 10
#     total += a
#     n //= 10
# print(total)
# # task 19
# for i in range(1, 21):
#     if i == 7:
#         print(i)
#         break
# # task 20
# for i in range(10, 101):
#     if i % 7 == 0:
#         print(i)
#         break
# # task 21
# secret = 8
# n = int(input("Too: "))
# while n > 1:
#     if n != secret:
#         print("wrong")
#     too = int(input("Too: "))
#     if too == 8:
#         print("oldooshaasn")
#         break
# # task 22
# n = int(input("Too: "))
# while n > 0:
#     if n != 0:
#         print("try agian")
#     too = int(input("Too: "))
#     if too == 0:
#         print("oldooshaasn")
#         break
# # task 23
# total = 0
# too = int(input("Too: "))
# while True:
#     if too != 0:
#         total += too
#         print(f"\n\nTotal : {total}\n\n---\n")
#     too = int(input("Too: "))
#     if too == 0:
#         break
# print("niit oruulsan tooni niilber=", total)
# # task 24
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)
# # task 25
# i = 0
# while i < 20:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
# # task 26
# i = 0
# while i < 30:
#     i += 1
#     if i % 3 == 0:
#         continue
#     print(i)
# # task 27
# count = 0
# total = 0
# while count < 5:
#     n = int(input("Too: "))
#     count += 1
#     if n < 0:
#         continue
#     total += n
# print("Niilber =", total)
# # task 28]
# n = 1
# count = 0
# while 0 <= n:
#     n += 1
#     if n % 7 == 0:
#         count += 1
#         print(n)
#     if count == 5:
#         break
# # task 29
# while True:
#     n = int(input("Too: "))
#     if n == 0:
#         break
#     if n < 0:
#         continue
#     if n % 2 != 0:
#         continue
#     print(n)
# # task 30
# secret = 17
# while True:
#     n = int(input("Too: "))
#     if n < 0:
#         print("sorog too oruulahgui")
#         continue
#     if n < secret:
#         print("baga bnaa")
#     elif n > secret:
#         print("ih bainaa")
#     if n == secret:
#         print("Zow baina")
#         break