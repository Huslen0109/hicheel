# task1
# n = list(map(int, input("TOo: ").split()))
# n = list(set(n))
# n.sort()
# print(n[-2])
# # # task 2
# n = list(map(int, input("TOo: ").split()))
# n = list(set(n))
# n.sort(reverse=True)
# print(n[-2])
# # task 3
# n = list(map(int, input("TOo: ").split()))
# count = 0
# max_count = 0
# for i in n:
#     if i % 2 != 0:
#         count += 1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)
# task 4
# n = list(map(int, input("TOo: ").split()))
# # task5
# n = list(map(int, input("TOo: ").split()))
# ih_count = 0
# hariu = n[0]
# for i in n:
#     count = n.count(i)
#     if count > ih_count:
#         ih_count = count
#         hariu = i
#     elif count == ih_count and i < hariu:
#         hariu = i
# print(hariu)
# # task 6
# n = list(map(int, input("TOo: ").split()))
# baga_count = 10000
# hariu = n[0]
# for i in n:
#     count = n.count(i)
#     if count < baga_count:
#         baga_count = count
#         hariu = i
#     elif count == baga_count and i < hariu:
#         hariu = i
# print(hariu)
# # task 7
# n = list(map(int, input("1Too: ").split()))
# b = list(map(int, input("2Too: ").split()))
# print(set(n) & set(b))
# # task 8
# n = list(map(int, input("TOo: ").split()))
# n = list(set(n))
# n.sort(reverse=True)
# print(n[1] + n[0])
# ###################### task 9
# n = list(map(int, input("TOo: ").split()))
# target = int(input("targget: "))
# for i in n:
#     if i + (i + 1) == target:
#         print()
# # ##################task 10

# #task 11
# n = list(map(int, input("TOo: ").split()))
# *a, b = n
# print(b, *a)
# ################# task 12
# n = list(map(int, input("TOo: ").split()))
# b = int(input("K rotate: "))
# c = n.reverse
# a, *c[b] = c
# print(*c[b], a)


# ############### task 13
# n = list(map(int, input("Too: ").split()))
# b = int(input("to: "))
# m = []
# # for i in n:
# #     if i == b:
# #         m.append(i)
# #         print([n], m)
# c = len(n)
# n.remove(b)
# print()
# # task 14
# n = list(map(int, input("Too: ").split()))
# b = []
# for i in n:
#     if i not in b:
#         b.append(i)
# print(b)
# # task 15
# a = list(map(int, input("Too: ").split()))
# n = int(input("too: "))
# b = []
# for i in range(1, n+1):
#     if i not in a:
#         b.append(i)
# print(b)
# # task 16
# n = list(map(int, input("Too: ").split()))
# for i in n:
#     if n.count(i) == 1:
#         print(i)
# #task 17
# n = list(map(int, input().split()))
# max_sum = n[0] + n[1]
# index1 = 0
# index2 = 1
# for i in range(len(n) - 1):
#     niilber = n[i] + n[i + 1]
#     if niilber > max_sum:
#         max_sum = niilber
#         index1 = i
#         index2 = i + 1
# print("ihniilber: ", max_sum)
# print("Index: ", index1, index2)

# # task 18
# a = list(map(int, input("Too: ").split()))
# for i in range(1, len(a) - 1):
#     if a[i] > a[i - 1] and a[i] > a[i + 1]:
#         print(a[i])
# # task 19
# a = list(map(int, input("Too: ").split()))
# for i in range(1, len(a) + 1):
#     if a[i] < a[i - 1] and a[i] < a[i + 1]:
#         print(a[i])
# # task 20
# a = list(map(int, input("Too: ").split()))
# count = 0
# for i in range(1, len(a) - 1):
#     if a[i] > a[i - 1] and a[i] > a[i + 1]:
#         count += 1
# print(count)
# # task 21
# n = int(input("too: "))
# for i in range(1, n + 1):
#     print(str(i) * i)
# # task 22
# n = int(input("TOo: "))
# for i in range(n, 0, -1):
#     print(str(i) * i)
# # task 23
# n = int(input("too: "))
# too = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(too, end=" ")
#         too += 1
#     print()