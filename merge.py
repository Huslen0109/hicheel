# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# numbers = [8, 3, 5, 4, 7, 6, 1, 2]
# print(merge_sort(numbers))

# # task 1

# def merge_sort(n):
#     if len(n) <= 1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right) 
#     result = []
#     j = 0
#     i = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# n = list(map(int, input("Toonuud: ").split(", ")))
# print(merge_sort(n))

# # task 2

# def merge_sort(n):
#     if len(n) <= 1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# n = list(map(int, input("Toonuud: ").split(", ")))
# print(merge_sort(n))

# # task 3

# def merge_sort(n):
#     if len(n) <= 1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right) 
#     result = []
#     j = 0
#     i = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# n = list(map(int, input("Toonuud: ").split(", ")))
# print(merge_sort(n))

# # task 4

# def merge_sort(n):
#     if len(n) <= 1:
#         return n
#     mid = len(n)//2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right) 
#     result = []
#     j = 0
#     i = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# n = list(map(int, input("Toonuud: ").split(", ")))
# print(merge_sort(n))

# # task 5

# def merge_sort(n):
#     if len(n) <= 1:
#         return n
#     mid = len(n) // 2
#     left = merge_sort(n[:mid])
#     right = merge_sort(n[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] % 2 == 0 and right[j] % 2 != 0:
#             result.append(left[i])
#             i += 1
#         elif left[i] % 2 != 0 and right[j] % 2 == 0:
#             result.append(right[j])
#             j += 1
#         elif left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# n = list(map(int, input("Toonuud: ").split(", ")))
# print(merge_sort(n))

# # task 6

# def merge(a, b):
#     result = []
#     i = 0
#     j = 0
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1
#     result.extend(a[i:])
#     result.extend(b[j:])
#     return result
# a = list(map(int, input("a массив: ").split()))
# b = list(map(int, input("b массив: ").split()))
# print(merge(a, b))

# # task 7

# def merge(n):
#     if len(n) <= 1:
#         return n
#     mid = len(n) // 2
#     left = n[:mid]
#     right = n[mid:]
#     left = merge(left)
#     right = merge(right)
#     i = 0
#     j = 0
#     result = []
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# n = list(map(int, input("Toonuud: ").split(", ")))
# sortedlist = merge(n)
# print(sortedlist[:3])

# # task 8

# def merge_sort_count(arr):
#     if len(arr) <= 1:
#         return arr, 0, 0
#     mid = len(arr) // 2
#     left, c1, m1 = merge_sort_count(arr[:mid])
#     right, c2, m2 = merge_sort_count(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     count = c1 + c2
#     while i < len(left) and j < len(right):
#         count += 1
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result, count, m1 + m2 + 1
# arr = list(map(int, input("Тоонууд: ").split()))
# sorted_arr, comparisons, merges = merge_sort_count(arr)
# print("Эрэмбэлсэн:", sorted_arr)
# print("Харьцуулалт:", comparisons)
# print("Merge:", merges)

# # task 9

# def largest_two(arr):
#     arr.sort(reverse=True)
#     return arr[:2]
# arr = list(map(int, input("Тоонууд: ").split()))
# print(largest_two(arr))

# # task 10

# def merge_sort(names):
#     if len(names) <= 1:
#         return names
#     mid = len(names) // 2
#     left = merge_sort(names[:mid])
#     right = merge_sort(names[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
# names = input("ners: ").split()
# print(merge_sort(names))

# # task 11

# def sort_students(students):
#     return sorted(students, key=lambda x: (-x[1], x[0]))
# n = int(input("count stu: "))
# students = []
# for i in range(n):
#     name = input("ner: ")
#     score = int(input("onoo: "))
#     students.append((name, score))
# print(sort_students(students))

# # task 12

# def sort_words(words):
#     return sorted(words, key=lambda x: (len(x), x))
# words = input("vgs: ").split()
# print(sort_words(words))

# # task 13

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
# def binary_search(arr, target):
#     arr = merge_sort(arr)
#     print("Эрэмбэлсэн:", arr)
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# arr = list(map(int, input("Тоонууд: ").split()))
# target = int(input("Хайх тоо: "))
# print("Индекс:", binary_search(arr, target))

# # task 14

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
# def is_anagram(word1, word2):
#     return merge_sort(list(word1)) == merge_sort(list(word2))
# word1 = input("Эхний үг: ")
# word2 = input("Хоёр дахь үг: ")
# print(is_anagram(word1, word2))

# # task 15

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
# def closest_pair(arr):
#     arr = merge_sort(arr)
#     print("Эрэмбэлсэн:", arr)
#     min_diff = arr[1] - arr[0]
#     pair = (arr[0], arr[1])
#     for i in range(1, len(arr) - 1):
#         diff = arr[i+1] - arr[i]
#         if diff < min_diff:
#             min_diff = diff
#             pair = (arr[i], arr[i+1])
#     return pair, min_diff
# arr = list(map(int, input("Тоонууд: ").split()))
# pair, diff = closest_pair(arr)
# print("Хос:", pair)
# print("Зөрүү:", diff)
