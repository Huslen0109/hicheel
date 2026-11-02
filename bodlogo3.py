# # task 1
# def num(n):
#     if n == 0:
#         return "0"
#     elif n > 0:
#         return "eyreg"
#     else:
#         return "sorog"

# n = int(input("Too: "))
# print(num(n))
# # task 2
# def score(n):
#     if n > 100 or n < 0:
#         return "buruu dvn"
#     elif n < 100 and n > 90:
#         return "A"
#     elif n < 90 and n > 80:
#         return "B"
#     elif n < 80 and n > 70:
#         return "C"
#     else:
#         return "D"
    
# n = int(input("Dun: "))
# print(score(n))
# # task 3
# def year(n):
#     if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#         return "ondor jil"
#     else:
#         return "engiin jil"
# n = int(input("JIl: "))
# print(year(n))
# # task 4
# def trangle(n):
#     if n[0] == n[1] == n[2]:
#         return " tegsh talt"
#     elif n[0] == n[1] or n[1] == n[2] or n[0] == n[2]:
#         return "adil hajhuut"
#     elif n[0] + n[1] > n[2] and n[0] + n[2] > n[1] and n[1] + n[2] > n[0]:
#         return "gurwaljin"
#     else:
#         "gurwaljin bish"
# n = list(map(int, input("Cm: ").split()))
# print(trangle(n))
# # task 5
# km = int(input("Km: "))
# tsag = int(input("Tsag (0-23): "))
# if km <= 2:
#     tulbur = 3000
# else:
#     tulbur = 3000 + (km - 2) * 1500
# if tsag >= 22 or tsag <= 5:
#     tulbur = tulbur + 2000
# print(tulbur)
# # task 6
# total = 0
# n = int(input("Too: "))
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total += i
# print(total)
# # task 7
# n = int(input("too: "))
# total = 0
# while n > 0:
#     a = n % 10
#     total += a
#     n = n // 10
# print(total)
# # task 8
# n = int(input("too: "))
# k = []
# total = 0
# while n > 0:
#     a = n % 10
#     k.append(a)
#     n = n // 10
# for i in k:
#     total = total * 10 + i
# print(total)
# # task 9
# n = int(input("Too: "))
# for i in range(1, n + 1):
#     if i % 15 == 0:
#         print("pizzpazz", end = " ")
#     elif i % 3 == 0:
#         print("piz", end=" ")
#     elif i % 5 == 0:
#         print("pazz", end = " ")
#     else:
#         print(i, end = " ")
# # task 10
# m = 54
# n = int(input("Too: "))
# while n > 0:
#         if n > m:
#             print("too ih baina")
#             n = int(input("Too: "))
#         if n < m:
#             print("too baga baina")
#             n = int(input("Too: "))
#         else:
#             print("oldloo")
#             break
# # task 11
# n = int(input("n: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=" ")
#     print()
# # task 12
# n = int(input("Too: "))
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))
# # task 13
# def find_pairs(arr, target):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 pairs.append((arr[i], arr[j]))
#     return pairs
# arr = list(map(int, input("Too: ").split(", ")))
# target = int(input("Target: "))
# print(find_pairs(arr, target))
# # task 14
# def most_frequent(arr):
#     max_count = 0
#     most_num = arr[0]

#     for i in range(len(arr)):
#         count = 0
#         for j in range(len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#         if count > max_count:
#             max_count = count
#             most_num = arr[i]
#     return (most_num, max_count)
# arr = list(map(int, input("Too: ").split(", ")))
# print(most_frequent(arr))  
# # task 15
# def row_col_sums(matrix):
#     row_sum = []
#     col_sum = []
#     for i in range(len(matrix)):
#         total = 0
#         for j in range(len(matrix[i])):
#             total += matrix[i][j]
#         row_sum.append(total)
#     for j in range(len(matrix[0])):
#         total = 0
#         for i in range(len(matrix)):
#             total += matrix[i][j]
#         col_sum.append(total)
#     return row_sum, col_sum
# row = int(input("Moriin too: "))
# matrix = []
# for i in range(row):
#     temp = list(map(int, input().split()))
#     matrix.append(temp)
# print(row_col_sums(matrix))
# # task 16
# def remove_duplicates(arr):
#     seen = set()
#     result = []
#     for i in arr:
#         if i not in seen:
#             seen.add(i)
#             result.append(i)
#     return result
# n = input("Elementuud: ").split()
# print(remove_duplicates(n))
# # task 17
# def word_count(text):
#     words = text.split()
#     count = {}
#     for word in words:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
#     return count
# text = input("Ugsiig oruul: ")
# print(word_count(text))
# # atask 18
# def averages(grades):
#     avg = {}
#     highest_name = ""
#     highest_avg = 0
#     for name in grades:
#         total = 0
#         for score in grades[name]:
#             total += score
#         average = total / len(grades[name])
#         avg[name] = average
#         if average > highest_avg:
#             highest_avg = average
#             highest_name = name
#     return avg, highest_name
# n = int(input("Suragchiin too: "))
# grades = {}
# for i in range(n):
#     name = input("Ner: ")
#     scores = list(map(int, input("Onoonuud: ").split()))
#     grades[name] = scores
# print(averages(grades))
# # task 19
# python = set(input("Python: ").split())
# math = set(input("Math: ").split())
# print("Hoyuland:", python & math)
# print("Zowhon Python:", python - math)
# print("Zowhon Math:", math - python)
# print("Niit:", len(python | math))
# # task 20
# def farthest_point(points):
#     farthest = points[0]
#     max_distance = 0
#     for point in points:
#         x, y = point
#         distance = x * x + y * y
#         if distance > max_distance:
#             max_distance = distance
#             farthest = point
#     return farthest, max_distance
# n = int(input("Tsegiin too: "))
# points = []
# for i in range(n):
#     x, y = map(int, input().split())
#     points.append((x, y))
# print(farthest_point(points))