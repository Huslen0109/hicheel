# # task 1
# for i in range(5):
#     print("sainuu")
# # task 2
# for i in range(0, 10):
#     print(i)
# # task 3
# for i in range (1, 11):
#     print(i)
# # task 4
# for i in range(10 , 0, -1):
#     print(i)
# # task 5
# a = "bat"
# for i in range(5):
#     print(a)
# # task 6
# a = 0
# for i in range(1, 11):
#     a += i 
#     print(a)
# # task 7
# a = 0
# for i in range(1, 101):
#      a += i 
# print(a)
# # task 8
# a = 0
# for i in range (1, 21):
#     if i % 2 == 0:
#         a += i
# print(a)
# # task 9
# a = 0
# for i in range(1, 31):
#     if i % 3 == 0:
#         a += i
# print(a)
# # task 10
# n = int(input("Too: "))
# a = 0
# for i in range(1, n+1):
#     a += i
# print(a) 
# # task 11
# shirheg = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         shirheg += 1
# print(shirheg)
# # task 12
# a = 0
# for i in range(1, 101):
#     if i % 5 == 0:
#         a += 1
# print(a)
# # task 13
# a = 0
# for i in range(1, 51):
#     if i % 3 == 0:
#         a += 1
# print(a) 
# # task 14
# a = 0
# b = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         a += 1
#     else:
#         b += 1
# print(a, b)
# # task 15
# a = int(input("Too: "))
# b = 0
# for i in range(1, a+1):
#     if i % 7 == 0:
#         b += 1
# print(b)
# # task 16
# count = 0
# niilber = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         count += 1
#         niilber += i
# print("niilber:", niilber)
# print("count:", count)
# # task 17
# count = 0
# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         count += 1
# print(count)
# # task 18
# count = 0
# total = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         total += i
# print(total)
# # task 19
# N = int(input("Suragchiin too: "))

# niilber = 0
# deesh = 0

# for i in range(N):
#     dun = int(input("dun: "))
#     niilber += dun
#     if dun > 80:
#         deesh += 1

# dundaj = niilber / N   
# print("Buh dungiin niilber:", niilber)
# print("dundaj dun:", dundaj)
# print("80+ dun:", deesh)
# # task 20
# n = int(input("Heden dun: "))
# high= 0
# for i in range(n): 
#     score = int(input("Dun: "))
#     if score > high:
#         high = score
# print("hamgiin ondor dun:", high)
# # task 21
# n = int(input("heden too: "))
# minum = int(input("too: "))
# for i in range(n - 1):
#     score = int(input("Too: "))
#     if score < minum:
#         minum == score
# print("hamgiin baga too: ",minum)
# # task 23
# n = int(input("too: "))
# total = 1
# for i in range(1, n+1):
#     total *= i
#     print(total)
# # task 24
# n = int(input("too: "))
# total = 0
# for i in range(1, n):
#     if n % i == 0:
#         total += 1
# if total == n:
#     print("yes")
# else:
#     print("no")
# # task 21
# for i in range(10, 51):
#     if i % 3 == 0:
#         print(i)
# # task 22
# n = int(input("Too: "))
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)
# # task 23
# total = 0
# for i in range(1, 51):
#     if i % 2 != 0:
#         total += i
# print(total)
# # task 24
# count = 0
# for i in range(1, 101):
#     if i % 4 == 0:
#         count += 1
# print(count)
# # task 25
# count = 0
# total = 0
# for i in range(10):
#     count = int(input("Too: "))
#     if count > 0:
#         total += count
# print(total)
# # task 26
# count = 0
# total = 0
# for i in range(10, 101):
#     if i % 5 == 0:
#         count += i
# print(count)
# # task 27
# n = input("Too: ")
# total = 0
# for i in n:
#     total = total + int(i)
# print("niilber: ", total)
# # task 28
# count = 0
# for i in range(1, 101):
#     if i % 7 == 0 and count < 5:
#         count += 1
#         print(i)
# # task 29
# last = 0
# for i in range(1, 50):
#     if i % 2 == 0 :
#         last = i
# print(last)
# # task 30
# minum = 0
# for i in range(5):
#     too = int(input("Too: "))
#     if too > 0:
#         if minum == 0 or too < minum:
#             minum = too
# print(minum)

################################################################

# # task 1
# for i in range(10, 51):
#     if i % 3 == 0:
#         print(i, end=" ")
# #  task 2

# n = int(input("N: "))
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i, end=" ")
# # task 3

# s = 0
# for i in range(1, 51):
#     if i % 2 == 1:
#         s = s + i
# print(s)

# # task 4

# count = 0
# for i in range(1, 101):
#     if i % 4 == 0:
#         count = count + 1
# print(count)

# # task 5

# s = 0
# for i in range(10):
#     a = int(input("Too: "))
#     if a > 0:
#         s = s + a
# print(s)

# # task 6

# s = 0
# for i in range(10, 101):
#     if i % 5 == 0:
#         s = s + i
# print(s)

# # task 7

# n = input("Too: ")
# s = 0
# for i in n:
#     if i >= "0" and i <= "9":
#         s = s + int(i)
# print(s)

# # task 8

# count = 0
# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i, end=" ")
#         count = count + 1
#         if count == 5:
#             break

# # task 9

# a = 0
# for i in range(1, 50):
#     if i % 2 == 0:
#         a = i
# print(a)

# # task 10

# small = 0
# for i in range(10):
#     a = int(input("Too: "))
#     if a > 0:
#         if small == 0 or a < small:
#             small = a
# print(small)





