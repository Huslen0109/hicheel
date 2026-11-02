# # task 1
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 2
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] < n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 3
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 4
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 5
# n = list(map(int, input("too: ").split()))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j+1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1]= ih
# print(n)
# # task 6
# n = list(input("ner: ").split(", "))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 7
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 8
# n = list(map(int, input("too: ").split(", ")))
# for i in range((len(n)+1)-len(n)):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 9
# count = 0
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     count += 1
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# print(count)
# # task 10
# count = 0
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
#             count += 1
# print(n)
# print(count)
# # task 11
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# print(n[-2])
# # task 12
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 13
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n) - 1):
#     for j in range(len(n) - 1 - i):
#         if n[j] > n[j + 1]:
#             n[j], n[j + 1] = n[j + 1], n[j]
#     print(f"{i + 1}-r dwatalt {n}")
# # task 14
# numbers = list(map(int, input("too: ").split(" ")))
# for i in range(len(numbers)-1):
#     swapped = False
#     for j in range(len(numbers)- 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swapped = True
#     if not swapped:
#         print(f"{i + 1}-toirogt yuc hiigdeegui bna")
#         break
#     print(numbers)
# # task 15
# n =list(map(int, input("Too: ").split(", ")))
# for i in range(len(n)-1):
#     swap = False
#     for j in range(len(n)-1 -i):
#         if n[j] > n[j+1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
#             swap =True
#     if not swap:
#         print(f"{i + 1}-r toirogt yuu c hiigdsengui")
#         break
# print(n)
# # task 17
# students = []
# n = int(input("heden oyutan: "))
# for i in range(n):
#     name = input("ner: ")
#     score = int(input("nas: "))
#     students.append([name, score])
# for i in range(len(students) - 1):
#     for j in range(len(students) - 1 - i):
#         if students[j][1] < students[j + 1][1]:
#             temp = students[j]
#             students[j] = students[j + 1]
#             students[j + 1] = temp
# print(students)
# print(f"hamgiin zaluu: {students[-1]}")
# print(f"hamgiin hogshin: {students[0]}")
# # task 18
# def sort_numbers(n):
#     for i in range(len(n) - 1):
#         for j in range(len(n) - 1 - i):
#             if n[j] > n[j + 1]:
#                 temp = n[j]
#                 n[j] = n[j + 1]
#                 n[j + 1] = temp
#     return n
# def count_target(n, target):
#     count = 0
#     for k in n:
#         if k == target:
#             count += 1
#     return count
# numbers = list(map(int, input("Too: ").split()))
# target = int(input("target: "))
# numbers = sort_numbers(numbers)
# count = count_target(numbers, target)
# print(numbers)
# print(f"{target} too {count} shirheg bna")
# # task 21
# n = list(map(int, input("too: ").split(", ")))
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# # task 22
# words = input("words: ").split(", ")
# n = len(words)
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if len(words[j]) > len(words[j + 1]):
#             words[j], words[j + 1] = words[j + 1], words[j]
# print(words)
# # task 23
# def selection(numbers):
#     n = len(numbers)
#     count = 0
#     for i in range(n -1):
#         min = i
#         for j in range(i + 1, n):
#             if numbers[j] < numbers[min]:
#                 min = j
#         numbers[i], numbers[min] = number[min], numbers[i]
#         count += 1
#         if count == 1:
#             return numbers
# number = list(map(int, input("toonuud: ").split(", ")))
# print(selection(number))
# # task 24
# def bubble(arr):
#     n = len(arr)
#     for i in range(n -1):
#         for j in range(n -1 -i):
#             if arr[j] % 2 != 0 and arr[j + 1] % 2 == 0:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return(arr)
# number = list(map(int,input("toonuud: ").split(", ")))
# print(bubble(number))
# # task 25
# def num(arr):
#     for i in range(len(arr) - 1):
#         for x in range(len(arr)-1-i):
#             if arr[x] > arr[x+1]:
#                 ih = arr[x]
#                 arr[x] = arr[x+1]
#                 arr[x+1] = ih
#     return arr  
# a = list(map(int, input("Too: ").split(", ")))
# b = list(map(int, input("Too: ").split(", ")))
# print(num(a+b))
# # task 26
# def bubble_sort_count(numbers):
#     n = len(numbers)
#     total = 0
#     for i in range(n - 1):
#         round_count = 0
#         for x in range(n - 1 - i):
#             if numbers[x] > numbers[x + 1]:
#                 ih = numbers[x]
#                 numbers[x] = numbers[x + 1]
#                 numbers[x + 1] = ih
#                 round_count += 1
#         total += round_count
#         print(f"{i + 1}-r toirgiin daraa: {round_count} солилцоо")
#     print(f"niit: {total}")
# numbers = list(map(int, input("Toonuud: ").split(", ")))
# bubble_sort_count(numbers)
# # task 27
# n = list(map(int, input("Too: ").split(", ")))
# for i in range(len(n) - 1):
#     for j in range(len(n) - 1 - i):
#         if n[j] > n[j+1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n[2])
# # task 28
# def qwerty(n):
#     for i in range(len(n) - 1):
#         for j in range(len(n) - 1 - i):
#             if n[j][1] < n[j + 1][1]:
#                 baga = n[j]
#                 n[j] = n[j + 1]
#                 n[j + 1] = baga
#     return n
# n = []
# a = int(input("heden suragch: "))
# for x in range(a):
#     name = input("ner: ")
#     score = int(input("score: "))
#     n.append([name, score])
# print(qwerty(n))
# # task 29
# def bubble_analyze(numbers):
#     n = len(numbers)
#     comparisons = 0
#     swaps = 0
#     no_swap_round = 0 
#     for i in range(n - 1):
#         swapped = False
#         for j in range(n - 1 - i):
#             comparisons += 1
#             if numbers[j] > numbers[j + 1]:
#                 temp = numbers[j]
#                 numbers[j] = numbers[j + 1]
#                 numbers[j + 1] = temp
#                 swaps += 1
#                 swapped = True
#         if not swapped:
#             no_swap_round = i + 1
#             break
#     print("Нийт харьцуулалтын тоо:", comparisons)
#     print("Нийт солилцооны тоо:", swaps)
#     if no_swap_round:
#         print(f"Солилцоо хийгдээгүй эхний тойрог: {no_swap_round}-р тойрог")
#     else:
#         print("Солилцоо хийгдээгүй тойрог байхгүй")
#     print("Эцсийн жагсаалт:", numbers)
# numbers = list(map(int, input("Toonuud: ").split(", ")))
# bubble_analyze(numbers)
# import time
# start = time.perf_counter()

#######################################################################
import time
start = time.perf_counter()

a = 10
b = 20
c = a + b

end = time.perf_counter()
print("O(1)")
print(f"Time: {(end - start) * 1000:.6f} ms")

########################################################################

import time

n = 1000000
arr = list(range(n))
target = n - 1

start = time.perf_counter()

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

end = time.perf_counter()

print("O(log n)")
print(f"Time: {(end - start) * 1000:.6f} ms")

#####################################################################

import time

n = 1000000
arr = list(range(n))
target = n - 1

start = time.perf_counter()

for i in arr:
    if i == target:
        break

end = time.perf_counter()

print("O(n)")
print(f"Time: {(end - start) * 1000:.6f} ms")

######################################################################

import time

n = 3000

start = time.perf_counter()

count = 0

for i in range(n):
    for j in range(n):
        count += 1

end = time.perf_counter()

print("O(n²)")
print(f"Time: {(end - start) * 1000:.6f} ms")



# Өгөгдөл (n)	O(log n) үйлдэл	Хугацаа

# 1,000	            ~10 алхам	    0.001 - 0.01 ms
# 100,000	        ~17 алхам	    0.005 - 0.05 ms
# 1,000,000	        ~20 алхам	    0.01 - 0.1 ms
# 100,000,000	    ~27 алхам	    0.01 - 0.2 ms
