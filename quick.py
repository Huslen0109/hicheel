#############################################################
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = list(map(int, input("Too: ").split()))
# print(quick_sort(numbers))

##############################################################

# # task 1
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#         median = len(quick_sort(left) + middle + quick_sort(right))//2
#     return median
# numbers = list(map(int, input("Too: ").split(", ")))
# print(quick_sort(numbers))
# # task 2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if i > pivot:
#             left.append(i)
#         elif i == pivot:
#             mid.append(i)
#         else:
#             right.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# arr = list(map(int, input("too: ").split(", ")))
# print(quick_sort(arr))
# # task 3
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i == pivot:
#             mid.append(i)
#         else:
#             right.append(i)
#         median = len(quick_sort(left) + mid + quick_sort(right))//2
#     return arr[median]
# arr = list(map(int, input("too: ").split(", ")))
# print(quick_sort(arr))
# # task 4
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i == pivot:
#             mid.append(i)
#         else:
#             right.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# arr = list(map(int, input("too: ").split(", ")))
# print(quick_sort(arr))
# # task 5
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i == pivot:
#             mid.append(i)
#         else:
#             right.append(i)
#     return quick_sort(left) + mid + quick_sort(right)[:2]
# arr = list(map(int, input("too: ").split(", ")))
# print(quick_sort(arr))
# # task 6
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i == pivot:
#             mid.append(i)
#         else:
#             right.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# arr = list(map(int, input("too: ").split(", ")))
# print(quick_sort(arr)[-2::])
# # task 7
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if i[1] < pivot[1]:
#             left.append(i)
#         elif i[1] == pivot[1]:
#             mid.append(i)
#         else:
#             right.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# students = []
# n = int(input("Oyutnii too: "))
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     students.append((name, score))
# print(quick_sort(students))
# # task 8
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if len(i) < len(pivot):
#             left.append(len(i))
#         elif len(i) == len(pivot):
#             mid.append(len(i))
#         else:
#             right.append(len(i))
#     return quick_sort(left) + mid + quick_sort(right)
# # task 9
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i == pivot:
#             mid.append(i)
#         else:
#             right.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# arr = list(map(int, input("too: ").split(", ")))
# sorted_arr = quick_sort(arr)
# n = len(sorted_arr)
# if n % 2 == 1:
#     median = sorted_arr[n//2]
# else:
#     median = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
# print("Sorted:", sorted_arr)
# print("Median:", median)

# # task 10

# def quick_sort(qwert):
#     if len(qwert) <= 1:
#         return arr
#     pivot = qwert[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in qwert:
#         if i > pivot:
#             left.append(i)
#         elif i == pivot:
#             mid.append(i)
#         else:
#             right.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# n = int(input("heden input: "))
# for i in range(n):
#     arr = list(map(int, input("too: ").split(", ")))
#     arr.append(arr)
#     qwert = arr + arr
# print(quick_sort(arr))