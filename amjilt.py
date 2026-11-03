
# # task 1 - Hoyor dahi hamgiin ih too
# nums = [7, 3, 9, 9, 2, 5, 7, 8]
# a = sorted(set(nums))
# print(a[-2])
# # task 2 - Hoyor dahi hamgiin baga too
# nums = list(map(int, input("Toonuud: ").split()))
# a = sorted(set(nums))
# if len(a) >= 2:
#     print(a[1])
# else:
#     print("Baihgui")
# # task 3 - Hamgiin urt sondgoi heseg
# nums = [2, 1, 3, 5, 4, 7, 9, 11, 6]
# count = 0
# big = 0
# for n in nums:
#     if n % 2 == 1:
#         count += 1
#         if count > big:
#             big = count
#     else:
#         count = 0
# print(big)
# # task 4 - Hamgiin urt osoh daraalal
# nums = [1, 2, 4, 2, 3, 5, 7, 1]
# count = 1
# big = 1
# for i in range(1, len(nums)):
#     if nums[i] > nums[i - 1]:
#         count += 1
#     else:
#         count = 1
#     if count > big:
#         big = count
# print(big)
# # task 5 - Hamgiin tsoon davtagdsan too
# nums = list(map(int, input("Toonuud: ").split()))
# best = nums[0]
# small = nums.count(best)
# for n in nums:
#     count = nums.count(n)
#     if count < small:
#         small = count
#         best = n
# print(best)
# # task 6 - Hoyor listiin niitleg element
# a = [1, 2, 3, 4, 5]
# b = [3, 5, 7, 8, 1]
# result = []
# for n in a:
#     if n in b and n not in result:
#         result.append(n)
# print(result)
# # task 7 - Niilber ni hamgiin ih hos
# nums = [4, 7, 2, 9, 5]
# a = nums[0]
# b = nums[1]
# big = a + b
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         s = nums[i] + nums[j]
#         if s > big:
#             big = s
#             a = nums[i]
#             b = nums[j]
# print(a, b)
# # task 8 - Niilber ni target
# nums = [4, 8, 2, 7, 5]
# target = 9
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)
# # task 9 - Zoruu hamgiin baga hos
# nums = list(map(int, input("Toonuud: ").split()))
# small = None
# a = 0
# b = 0
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] != nums[j]:
#             d = nums[i] - nums[j]
#             if d < 0:
#                 d = 0 - d
#             if small == None or d < small:
#                 small = d
#                 a = nums[i]
#                 b = nums[j]
# if small == None:
#     print("Baihgui")
# else:
#     print(a, b)
# # task 10 - Zero togsgold
# nums = [0, 1, 0, 3, 12]
# result = []
# count = 0
# for n in nums:
#     if n == 0:
#         count += 1
#     else:
#         result.append(n)
# for i in range(count):
#     result.append(0)
# print(result)
# # task 11 - Neg udaa baigaa too
# nums = [4, 1, 2, 1, 2]
# for n in nums:
#     if nums.count(n) == 1:
#         print(n)
#         break
# # task 12 - Horshuudiin hamgiin ih niilber
# nums = list(map(int, input("Toonuud: ").split()))
# big = nums[0] + nums[1]
# index = 0
# for i in range(len(nums) - 1):
#     s = nums[i] + nums[i + 1]
#     if s > big:
#         big = s
#         index = i
# print(big)
# print(index, index + 1)
# # task 13 - Toon piramid
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end="")
#     print()
# # task 14 - Urwuu piramid
# n = int(input("N: "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(i, end="")
#     print()
# # task 15 - Floyd Triangle
# n = int(input("N: "))
# a = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(a, end=" ")
#         a += 1
#     print()
# # task 16 - Prime pair
# n = int(input("N: "))
# for a in range(2, n + 1):
#     b = n - a
#     if a <= b:
#         p1 = True
#         p2 = True
#         if b < 2:
#             p2 = False
#         for i in range(2, a):
#             if a % i == 0:
#                 p1 = False
#         for i in range(2, b):
#             if b % i == 0:
#                 p2 = False
#         if p1 and p2:
#             print(a, b)
# # task 17 - Goldbach
# n = int(input("N: "))
# count = 0
# for a in range(2, n + 1):
#     b = n - a
#     if a <= b:
#         p1 = True
#         p2 = True
#         if b < 2:
#             p2 = False
#         for i in range(2, a):
#             if a % i == 0:
#                 p1 = False
#         for i in range(2, b):
#             if b % i == 0:
#                 p2 = False
#         if p1 and p2:
#             count += 1
# print(count)
# # task 18 - Perfect number
# n = int(input("N: "))
# total = 0
# for i in range(1, n):
#     if n % i == 0:
#         total += i
# if n > 1 and total == n:
#     print("YES")
# else:
#     print("NO")
# # task 19 - Perfect numbers
# n = int(input("N: "))
# for a in range(2, n + 1):
#     total = 0
#     for i in range(1, a):
#         if a % i == 0:
#             total += i
#     if total == a:
#         print(a)
# # task 20 - Armstrong number
# n = int(input("N: "))
# a = n // 100
# b = n // 10 % 10
# c = n % 10
# total = a**3 + b**3 + c**3
# if total == n:
#     print("YES")
# else:
#     print("NO")
# # task 21 - Armstrong numbers
# n = int(input("N: "))
# for a in range(1, n + 1):
#     temp = a
#     digits = 0
#     while temp > 0:
#         digits += 1
#         temp //= 10
#     temp = a
#     total = 0
#     while temp > 0:
#         d = temp % 10
#         total += d ** digits
#         temp //= 10
#     if total == a:
#         print(a)
# # task 22 - Prime digit sum
# n = int(input("N: "))
# for a in range(2, n + 1):
#     prime = True
#     for i in range(2, a):
#         if a % i == 0:
#             prime = False
#     if prime:
#         temp = a
#         total = 0
#         while temp > 0:
#             total += temp % 10
#             temp //= 10
#         prime2 = True
#         if total < 2:
#             prime2 = False
#         for i in range(2, total):
#             if total % i == 0:
#                 prime2 = False
#         if prime2:
#             print(a)
# # task 23 - Daraalsan elementiin hamgiin ih urjwer
# nums = [2, -3, 4, 5, -2, 8, 1]
# big = nums[0] * nums[1]
# index = 0
# for i in range(len(nums) - 1):
#     p = nums[i] * nums[i + 1]
#     if p > big:
#         big = p
#         index = i
# print(nums[index], nums[index + 1])
# # task 24 - Hamgiin urt ijil daraalal
# nums = [1, 2, 2, 2, 3, 4, 4, 5]
# count = 1
# big = 1
# for i in range(1, len(nums)):
#     if nums[i] == nums[i - 1]:
#         count += 1
#     else:
#         count = 1
#     if count > big:
#         big = count
# print(big)
# # task 25 - Hamgiin urt palindrome heseg
# nums = [1, 2, 3, 2, 1, 7]
# big = 0
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums) + 1):
#         part = nums[i:j]
#         if part == part[::-1]:
#             if len(part) > big:
#                 big = len(part)
# print(big)
# # task 26 - Hoyor list ijil uu
# a = list(map(int, input("List 1: ").split()))
# b = list(map(int, input("List 2: ").split()))
# same = True
# if len(a) != len(b):
#     same = False
# else:
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             same = False
# if same:
#     print("YES")
# else:
#     print("NO")
# # task 27 - Neg ijil elementuud
# a = list(map(int, input("List 1: ").split()))
# b = list(map(int, input("List 2: ").split()))
# result = []
# for n in a:
#     if n in b and n not in result:
#         result.append(n)
# print(result)
# # task 28 - List intersection count
# a = [1, 2, 2, 3]
# b = [2, 2, 4]
# count = 0
# used = []
# for n in a:
#     if n in b and used.count(n) < b.count(n):
#         count += 1
#         used.append(n)
# print(count)
# # task 29 - Hamgiin oir hoyor too
# nums = [10, 3, 20, 8, 9]
# small = None
# a = 0
# b = 0
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] != nums[j]:
#             d = nums[i] - nums[j]
#             if d < 0:
#                 d = 0 - d
#             if small == None or d < small:
#                 small = d
#                 a = nums[i]
#                 b = nums[j]
# if small == None:
#     print("Baihgui")
# else:
#     print(a, b)
# # task 30 - Equilibrium index
# nums = [-7, 1, 5, 2, -4, 3, 0]
# for i in range(len(nums)):
#     left = 0
#     right = 0
#     for j in range(i):
#         left += nums[j]
#     for j in range(i + 1, len(nums)):
#         right += nums[j]
#     if left == right:
#         print(i)
# # task 31 - Majority element
# nums = [2, 2, 1, 1, 1, 2, 2]
# found = False
# for n in nums:
#     if nums.count(n) > len(nums) // 2:
#         print(n)
#         found = True
#         break
# if found == False:
#     print("Baihgui")
# # task 32 - Tuple coordinate
# points = ((2, 5), (1, 3), (7, 2), (4, 9))
# best = points[0]
# for p in points:
#     if p[1] > best[1]:
#         best = p
# print(best)
# # task 33 - Hamgiin hol tseg
# points = ((2, 5), (1, 3), (7, 2), (4, 9))
# best = points[0]
# big = best[0]**2 + best[1]**2
# for p in points:
#     d = p[0]**2 + p[1]**2
#     if d > big:
#         big = d
#         best = p
# print(best)
# # task 34 - Student average
# students = (
#     ("Bat", (80, 90, 75)),
#     ("Bold", (92, 88, 95)),
#     ("Saraa", (70, 75, 80))
# )
# best = ""
# big = -1
# for student in students:
#     total = 0
#     for score in student[1]:
#         total += score
#     avg = total / len(student[1])
#     print(student[0], round(avg, 2))
#     if avg > big:
#         big = avg
#         best = student[0]
# print("Highest:", best)
# # task 35 - Product price
# products = (
#     ("Mouse", 120000),
#     ("Keyboard", 180000),
#     ("Monitor", 650000),
#     ("Headset", 250000)
# )
# budget = int(input("Budget: "))
# best = ""
# price = -1
# for p in products:
#     if p[1] <= budget and p[1] > price:
#         price = p[1]
#         best = p[0]
# if price == -1:
#     print("Baihgui")
# else:
#     print(best, price)
# # task 36 - Two Sum buh hos
# nums = [2, 7, 11, 15, 3, 6]
# target = 9
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i], nums[j])
# # task 37 - Three Sum
# nums = [1, 2, 3, 4, 5, 6]
# target = 9
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         for k in range(j + 1, len(nums)):
#             if nums[i] + nums[j] + nums[k] == target:
#                 print(nums[i], nums[j], nums[k])
# # task 38 - Longest consecutive sequence
# nums = [100, 4, 200, 1, 3, 2]
# a = sorted(set(nums))
# count = 1
# big = 1
# for i in range(1, len(a)):
#     if a[i] == a[i - 1] + 1:
#         count += 1
#     else:
#         count = 1
#     if count > big:
#         big = count
# print(big)
# # task 39 - Stock Profit
# prices = [7, 1, 5, 3, 6, 4]
# buy = prices[0]
# profit = 0
# for price in prices:
#     if price < buy:
#         buy = price
#     if price - buy > profit:
#         profit = price - buy
# print(profit)
# # task 40 - Student Ranking System
# students = (
#     ("Bat", (85, 90, 78)),
#     ("Bold", (92, 88, 95)),
#     ("Saraa", (70, 75, 80)),
#     ("Dulmaa", (95, 91, 94)),
#     ("Temuulen", (60, 72, 68))
# )
# names = []
# averages = []
# highest = ""
# lowest = ""
# big = -1
# small = 101
# count90 = 0
# count80 = 0
# count70 = 0
# countlow = 0
# high_score = -1
# all70 = []
# below60 = []
# for student in students:
#     name = student[0]
#     scores = student[1]
#     total = 0
#     good = True
#     bad = False
#     for score in scores:
#         total += score
#         if score > high_score:
#             high_score = score
#         if score < 70:
#             good = False
#         if score < 60:
#             bad = True
#     avg = total / len(scores)
#     names.append(name)
#     averages.append(avg)
#     print(name, "-", format(avg, ".2f"))
#     if avg > big:
#         big = avg
#         highest = name
#     if avg < small:
#         small = avg
#         lowest = name
#     if avg >= 90:
#         count90 += 1
#     elif avg >= 80:
#         count80 += 1
#     elif avg >= 70:
#         count70 += 1
#     else:
#         countlow += 1
#     if good:
#         all70.append(name)
#     if bad:
#         below60.append(name)
# print("Highest average:", highest)
# print("Lowest average:", lowest)
# print("90+:", count90)
# print("80-89:", count80)
# print("70-79:", count70)
# print("Below 70:", countlow)
# print("Highest score:", high_score)
# print("All 70+:", all70)
# print("Below 60:", below60)
# for i in range(len(averages)):
#     for j in range(i + 1, len(averages)):
#         if averages[j] > averages[i]:
#             averages[i], averages[j] = averages[j], averages[i]
#             names[i], names[j] = names[j], names[i]
# print("Ranking:")
# for i in range(len(names)):
#     print(names[i], "-", format(averages[i], ".2f"))
# ```
