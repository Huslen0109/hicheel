# # task 1
# nums = list(map(int, input("Toonuud: ").split()))
# nums = sorted(set(nums))
# if len(nums) >= 2:
#     print(nums[-2])
# else:
#     print("Hoyor dahi ih too baihgui")
# # task 2
# nums = list(map(int, input("Toonuud: ").split()))
# result = []
# for i in nums:
#     if i not in result:
#         result.append(i)
# print(result)
# # task 3
# text = input("Text: ")
# reverse = ""
# for i in range(len(text) - 1, -1, -1):
#     reverse += text[i]
# if text == reverse:
#     print("YES")
# else:
#     print("NO")
# # task 4
# words = input("Og uulber: ").split()
# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print(longest)
# # task 5
# text = input("Text: ").lower()
# vowels = "аэиоуөү"
# count = 0
# for ch in text:
#     if ch in vowels:
#         count += 1
# print(count)
# # task 6
# n = int(input("Too: "))
# total = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total += i
# print(total)
# # task 7
# n = int(input("Too: "))
# total = 0
# if n < 0:
#     n = 0 - n
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
# print(total)
# # task 8
# n = int(input("Too: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
# print(reverse)
# # task 9
# n = int(input("Too: "))
# is_prime = True
# if n < 2:
#     is_prime = False
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")
# # task 10
# nums = list(map(int, input("Toonuud: ").split()))
# smallest = nums[0]
# for num in nums:
#     if num < smallest:
#         smallest = num
# print(smallest)
# # task 11
# nums = list(map(int, input("Toonuud: ").split()))
# count = 0
# for num in nums:
#     if num % 2 == 0:
#         count += 1
# print(count)
# # task 12
# nums = list(map(int, input("Toonuud: ").split()))
# best = nums[0]
# best_count = 0
# for num in nums:
#     count = nums.count(num)
#     if count > best_count:
#         best_count = count
#         best = num
# print(best)
# # task 13
# words = input("Og uulber: ").split()
# target = input("Ug: ")
# count = 0
# for word in words:
#     if word == target:
#         count += 1
# print(count)
# # task 14
# nums = list(map(int, input("Toonuud: ").split()))
# for i in range(len(nums) - 1, -1, -1):
#     print(nums[i], end=" ")
# print()
# # task 15
# nums = list(map(int, input("Toonuud: ").split()))
# max_sum = nums[0] + nums[1]
# for i in range(len(nums) - 1):
#     current = nums[i] + nums[i + 1]
#     if current > max_sum:
#         max_sum = current
# print(max_sum)
# # task 16
# words = input("Og uulber: ").split()
# result = []
# for word in words:
#     result.append(word[::-1])
# print(" ".join(result))
# # task 17
# n = int(input("Too: "))
# if n < 0:
#     n = 0 - n
# count = 1
# while n >= 10:
#     count += 1
#     n //= 10
# print(count)
# # task 18
# n = int(input("Too: "))
# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)
# # task 19
# a = list(map(int, input("List 1: ").split()))
# b = list(map(int, input("List 2: ").split()))
# result = []
# for x in a:
#     if x in b and x not in result:
#         result.append(x)
# print(result)
# # task 20
# nums = list(map(int, input("Toonuud: ").split()))
# total = 0
# count = 0
# for n in nums:
#     if n > 0:
#         total += n
#         count += 1
# if count > 0:
#     print(total / count)
# else:
#     print("Eyreg too baihgui")
# # task 21
# student = ("Saraa", 19, "Python", 95, "A")
# name, age, lesson, score, grade = student
# print(name)
# print(age)
# print(lesson)
# # task 22
# data = (10, 20, 30, 40, 50)
# first = data[0]
# remaining = data[1:]
# print(first)
# print(remaining)
# # task 23
# nums = (-12, -5, -30, -8, -21)
# largest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
# print(largest)
# # task 24
# nums = (5, 1, 8, 3, 2)
# nums = tuple(sorted(nums))
# print(nums)
# # task 25
# nums = (10, 20, 30, 40, 50)
# x = int(input("Too: "))
# if x in nums:
#     print(nums.index(x))
# else:
#     print("Oldsongui")
# # task 26
# nums = (1, 2, 2, 3, 4, 4, 5)
# result = []
# for n in nums:
#     if nums.count(n) > 1 and n not in result:
#         result.append(n)
# print(tuple(result))
# # task 27
# words = input("Og uulber: ").lower().split()
# best_word = ""
# best_count = 0
# for word in words:
#     count = words.count(word)
#     if count > best_count:
#         best_count = count
#         best_word = word
# print(best_word)
# # task 28
# nums = tuple(map(int, input("Toonuud: ").split()))
# total = 0
# for n in nums:
#     if n % 2 == 0:
#         total += n
# print(total)