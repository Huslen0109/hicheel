# def linear(l, target):
#     for i in range(len(l)):
#         if l[i] ==  target:
#             return i
#     return -1
# l = list(map(int, input("TOo: ").split()))
# target = 21
# print(linear(l, target))
#########################################################
# def linear(l, t):
#     for x, i in enumerate(l):
#         if i == t:
#             return x
# l = list(map(int, input("Toonuud: ").split()))
# t = int(input("Find: "))
# print(linear(l, t))
# # task 3
# def linear(l, t):
#     for x, i in enumerate(l):
#         if i == t:
#             return x
# l = list(map(int, input("Toonuud: ").split()))
# t = int(input("find: "))
# print(linear(l, t))
# # task 4
# def linear(l, t):
#     count = 0
#     for i in l:
#         if i == t:
#             count += 1
#     return count
# l = list(map(int, input("Toonuud: ").split()))
# t = int(input("find: "))
# print(linear(l, t))
# # task 5
# def linear(l, t):
#     last = "zail"
#     for i in range(len(l)):
#         if l[i] == t:
#             last = i
#     return last
# l = list(map(int, input("Toonuud: ").split()))
# t = int(input("Find: "))
# print(linear(l, t))
# # task 6
# def linear(l, t):
#     for x, i in enumerate(l):
#         if str(i) == str(t):
#             return x
#     return "obso"        
# l = input("ners: ").split()
# t = input("target: ")
# print(linear(l, t))
# # task 7
# def linear(l):
#     for x, i in enumerate(l):
#         if i > 0:
#             return x
# l = list(map(int, input("Too: ").split()))
# print(linear(l))
# # task 8
# def linear(l, t):
#     for i in l:
#         if i > t:
#             return i
#     return -1
# l = list(map(int, input("Toonuud: ").split()))
# t = int(input("Haih too: "))
# print(linear(l, t))
# # task 9
# def linear(students, name):
#     for i in students:
#         if i[0] == name:
#             return i[1]
#     return -1
# students = []
# n = int(input("Heden suragch: "))
# for i in range(n):
#     name = input("Ner: ")
#     age = int(input("Nas: "))
#     students.append([name, age])
# find = input("Haih ner: ")
# print(linear(students, find))
###########################################################
# # task 1
# def linear(l):
#     for i in l:
#         if i % 2 != 0:
#             return i
# l = list(map(int, input("too: ").split()))
# print(linear(l))
# # task 2
# def linear(l):
#     for i in l:
#         if i > 10:
#             return "oldloo"
#     return "obso"
# l = list(map(int, input("too: ").split()))
# print(linear(l))
# # task 3
# def linear(l):
#     for x, i in enumerate(l):
#         if i == 0:
#             return x
# l = list(map(int, input("too: ").split()))
# print(linear(l))
# # task 4
# def linear(l, t):
#     for i in l:
#         if i > t:
#             return i
# l = list(map(int, input("too: ").split(", ")))
# t = int(input("zxc: "))
# print(linear(l, t))
# # task 5
# def linear(l):
#     count = 0
#     for i in l:
#         if i < 0:
#             count += 1
#     return count
# l = list(map(int, input("Toonuud: ").split()))
# print(linear(l))
# # task 6
# def linear(n, t):
#     result = 0
#     found = False
#     for i in n:
#         if i < t:
#             if not found or i > result:
#                 result = i
#                 found = True
#     if found:
#         return result
#     return "obso"
# n = list(map(int, input("toonud: ").split()))
# t = int(input("t: "))
# print(linear(n, t))
# # task 7
# def linear(l):
#     for i in l:
#         if i % 2 == 0:
#             return i
# l = list(map(int, input("toonuud: ").split(", ")))
# print(linear(l))
# # task 8
# def linear(n, m):
#     for i in range(len(n)):
#         if n[i] > m and n[i] % 2 != 0:
#             return i
# n = list(map(int, input("Toonuud: ").split(", ")))
# m = int(input("Haih too: "))
# print(linear(n, m))
# # task 9
# def linear(n, s):
#     for i in n:
#         if i[1] > s:
#             return i[0]
# n = []
# a = int(input("heden suragch: "))
# for j in range(a):
#     ner = input("ner: ")
#     dvn = int(input("dvn: "))
#     n.append([ner, dvn])
# s = int(input("taget: "))
# print(linear(n, s))
# task 10
# def linear(n):
#     last = -1
#     for x, i in enumerate(n):
#         if i % 2 != 0:
#             last = x
#     return last
# n = list(map(int, input("Toonuud: ").split(",")))
# print(linear(n))
# # task 11
# def linear(n, m):
#     a = []
#     for x, i in enumerate(n):
#         if i == m:
#             a.append(x)
#     return a
# n = list(map(int, input("Too: ").split(", ")))
# m = int(input("too: "))
# print(linear(n, m))
# # task 12
# def linear(n, find):
#     for i in n:
#         if i[0] == find:
#             if i[1] >= 60:
#                 return "Тэнцсэн"
#             else:
#                 return "Тэнцээгүй"
#     return "Олдсонгүй"
# n = []
# a = int(input("Хэдэн сурагч: "))
# for i in range(a):
#     ner = input("Нэр: ")
#     dvn = int(input("Дүн: "))
#     n.append([ner, dvn])
# find = input("Олох нэр: ")
# print(linear(n, find))
