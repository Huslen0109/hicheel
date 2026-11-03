# # task 1
# n = int(input("Too: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1
# # task2
# n = int(input("Too: "))
# while n >= 1:
#     print(n)
#     n -= 1
# # task 3
# n = int(input("Too: "))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# # task 4
# n = int(input("Too: "))
# i = 1
# while i <= n:
#     if i % 2 == 1:
#         print(i)
#     i += 1
# # task 5
# n = int(input("Too: "))
# i = 1
# total = 0
# while i <= n:
#     total += i
#     i += 1
# print(total)

# # task 6
# n = int(input("Too: "))
# i = 1
# total = 0
# while i <= n:
#     if i % 2 == 0:
#         total += i
#     i += 1
# print(total)
# # task7
# n = int(input("Too: "))
# i = 1
# while i <= n:
#     if i % 3 == 0:
#         print(i)
#     i += 1
# # task 8
# n = int(input("Heden too: "))
# i = 0
# positive = 0
# negative = 0
# zero = 0
# while i < n:
#     a = int(input("Too: "))
#     if a > 0:
#         positive += 1
#     elif a < 0:
#         negative += 1
#     else:
#         zero += 1
#     i += 1
# print("Eyreg:", positive)
# print("Sorog:", negative)
# print("Teg:", zero)
# # task 9
# n = int(input("Heden too: "))
# i = 0
# total = 0
# while i < n:
#     a = int(input("Too: "))
#     if a > 0:
#         total += a
#     i += 1
# print(total)
# # task10
# n = int(input("Heden too: "))
# a = int(input("Too: "))
# big = a
# i = 1
# while i < n:
#     a = int(input("Too: "))
#     if a > big:
#         big = a
#     i += 1
# print(big)
# # task11
# n = int(input("Heden too: "))
# a = int(input("Too: "))
# small = a
# i = 1
# while i < n:
#     a = int(input("Too: "))
#     if a < small:
#         small = a
#     i += 1
# print(small)
# # task 12
# n = int(input("Too: "))
# i = 1
# while i <= n:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1
# # task 13
# n = int(input("Too: "))
# if n < 0:
#     n = 0 - n
# count = 1
# while n >= 10:
#     n //= 10
#     count += 1
# print(count)
# # task 14
# n = int(input("Too: "))
# total = 0
# while n > 0:
#     a = n % 10
#     total += a
#     n //= 10
# print(total)
# # task 15
# n = int(input("Too: "))
# reverse = 0
# while n > 0:
#     a = n % 10
#     reverse = reverse * 10 + a
#     n //= 10
# print(reverse)
# # task 16
# n = int(input("Too: "))
# a = n
# reverse = 0
# while a > 0:
#     digit = a % 10
#     reverse = reverse * 10 + digit
#     a //= 10
# if n >= 0 and n == reverse:
#     print("YES")
# else:
#     print("NO")
# # task `17`

# n = int(input("Too: "))
# i = 2
# count = 0
# while i < n:
#     if n % i == 0:
#         count += 1
#     i += 1
# if n > 1 and count == 0:
#     print("YES")
# else:
#     print("NO")
# # task 18
# n = int(input("Too: "))
# a = 2
# while a <= n:
#     i = 2
#     count = 0
#     while i < a:
#         if a % i == 0:
#             count += 1
#         i += 1
#     if count == 0:
#         print(a)
#     a += 1
# # task 19
# n = int(input("Too: "))
# i = 1
# while i <= 10:
#     print(n, "*", i, "=", n * i)
#     i += 1
# # task 20
# password = input("Nuuts ug: ")
# while password != "python123":
#     print("Buruu nuuts ug")
#     password = input("Nuuts ug: ")
# print("WELCOME")


#  # task 111111111111111111111111111111111
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