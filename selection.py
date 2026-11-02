# # task 1
# n = list(map(int, input("Toonuud: ").split(", ")))
# for i in range(len(n) - 1):
#     min_index = i
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
# print(n)
# # task 2
# count = 0
# n = list(map(int, input("Toonuud: ").split(", ")))
# for i in range(len(n) - 1):
#     min_index = i
#     count += 1
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
#     if count == 3:
#         print(n)
# # task 3
# n = list(map(int, input("Toonuud: ").split(", ")))
# for i in range(len(n) - 1):
#     min_index = i
#     for j in range(i + 1, len(n)):
#         if n[j] > n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
# print(n)
# # task 4
# n = list(map(int, input("Toonuud: ").split(", ")))
# for i in range(len(n) - 1):
#     min_index = i
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
# print(n)
# # task 5
# n = list(map(int, input("Toonuud: ").split(", ")))
# a = []
# for i in range(len(n) - 1):
#     min_index = i
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
# for k in n:
#     if k not in a:
#         a.append(k)
# print(a)
# # task 6
# n = list(map(int, input("Toonuud: ").split(", ")))
# count = 0
# for i in range(len(n) - 1):
#     min_index = i
#     count += 1
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
#     if count == 1:
#         print(n)
# # task 7
# n = list(map(int, input("Toonuud: ").split(", ")))
# count = 0
# for i in range(len(n) - 1):
#     min_index = i
#     count += 1
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
#     if count == 1:
#         print(n)
# # task 8
# n = list(map(int, input("Toonuud: ").split(", ")))
# count = 0
# for i in range(len(n) - 1):
#     min_index = i
#     count += 1
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
#     if count == 1:
#         print(n)
# # task 9
# n = list(map(int, input("Toonuud: ").split(", ")))
# count = 0
# for i in range(len(n) - 1):
#     min_index = i
#     count += 1
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
# print(count)
# # task 10
# def is_sorted(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
#     return True
# a = list(map(int, input("toonuud: ").split()))
# b = list(map(int, input("toonuud: ").split()))
# c = list(map(int, input("toonuud: ").split()))
# print("a:", is_sorted(a))   # False
# print("b:", is_sorted(b))   # True
# print("c:", is_sorted(c))   # False
# # task 11
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < n[min_index]:
#                 min_index = j
#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#         return arr
# n = list(map(int, input("toonuud: ").split()))
# print(selection_sort(n))
# # task 12
# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[min_index]:
#                 min_index = j
#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#     return arr
# n = list(map(int, input("toonuud: ").split()))
# print(selection_sort(n))
# # task 13
# n = list(map(int, input("Toonuud: ").split()))
# print(n.index(min(n)))
# # task 14
# n = list(map(int, input("Toonuud: ").split(", ")))
# for i in range(len(n) - 1):
#     min_index = i
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
#     print(n)
# TASK 15

#######    selection    ########

# n = list(map(int, input("Toonuud: ").split(", ")))
# for i in range(len(n) - 1):
#     min_index = i
#     for j in range(i + 1, len(n)):
#         if n[j] < n[min_index]:
#             min_index = j
#     temp = n[i]
#     n[i] = n[min_index]
#     n[min_index] = temp
#     print("selection", n)

#######     bubble     ########

# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
#     print("bubble", n)
