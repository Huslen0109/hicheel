# # task1
# n = tuple(input("txt: ").split(", "))
# print(n)
# # task2
# n = tuple(input("Txt: ").split(", "))
# print(n[0])
# print(n[2])
# print(n[-1])
# # task3
# n = tuple(input("txt: "))
# print(type(n))
# # task4
# n = tuple(input("txt: ").split(", "))
# print(n[0])
# print(n[2])
# print(n[-1])
# # task5
# n = tuple(map(int, input("too: ").split()))
# print(n[:3])
# # task6
# n = tuple(map(int, input("too: ").split()))
# print(n[-3:])
# # task7
# n = input("txt: ").split()
# b = list(n)
# print(len(b))
# # task8
# n = tuple(input("txt: ").split())
# print(max(n),min(n))
# # task9
# n = tuple(map(int, input("txt: ").split()))
# print(sum(n), sum(n)/len(n))
# # task10
# n = tuple(map(int, input("txt: ").split()))
# b = sorted(n)
# print(b)
# # task11
# total = 0
# n = tuple(map(int, input("Too: ").split()))
# b = int(input("too: "))
# print(n.count(b))
# # task12
# n = tuple(input().split())
# print(n.index("жүрж"))
# # task13
# n = tuple(input("txt: ").split())
# b = input("find: ")
# if b in n:
#     print("yes")
# else: 
#     print("no")
# # task 14
# n = tuple(input("txt: ").split())
# a = n[0]
# b = n[1]
# c = n[2]
# print(a)
# print(b)
# print(c)
# # task 15
# n = tuple(input("txt: ").split())
# x = n[0]
# y = n[1]
# print(f"x = {x}")
# print(f"y = {y}")
# # task 16
# n = tuple(input("txt: ").split(", "))
# a, b, c = n
# print(a)
# print(b)
# print(c)
# # task 17
# a, b = tuple(map(int, input("txt: ").split()))
# a, b = b, a
# print(a, b)
# # task 18
# n = tuple(map(int, input("too: ").split()))
# first, *other = n
# print(first)
# print(other)
# # task 19
# numbers = tuple(map(int, input("Too: ").split()))
# first, *middle, last = numbers
# print( first)
# print( middle)
# print( last)
# # task 20
# n = input("txt: ").split()
# a, *b = n
# print(a)
# print([*b])
# # task 21
# n = input("txt: ").split()
# a, b, c = n
# q = int(b) * int(c)
# print(a)
# print(b)
# print(c)
# print(q)
# # task 22
# n = int(input("Сурагчдын тоо: "))
# students = ()
# for i in range(n):
#     name, score = input("Нэр оноо: ").split()
#     students += ((name, int(score)))
# for name, score in students:
#     print(name , ":", score)
# # task 23
# n, b = tuple(input("txt: ").split())
# c = int(b)
# if c > 80:
#     print("yes")
# else: 
#     print("no")
# # task 24
# n = input("txt: ").split()
# b = list(n)
# b.append("shar")
# n = tuple(b)
# print(n)
# # task22
# n = int(input("heden suracgh: "))
# ners = []
# scores = []
# for i in range(n):
#     ner, dun = tuple(input("txt: ").split())
#     if ner not in ners:
#         ners += ner
#     if dun not in scores:
#         scores += dun
# for ii in range(n):
#     print(ners[ii]," : ",scores[ii])
# text = input()
# reverse = ""
# for i in range(len(text)-1, -1, -1):
#     reverse += text[i]
# if text == reverse:
#     print("YES")
# else:
#     print("NO")
