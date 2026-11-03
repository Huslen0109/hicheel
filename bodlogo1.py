# # task 1
# n = input("ug: ").split()
# print(len(n))
# # task 2
# n = input("ug: ").split()
# urtug = [0]
# for i in n:
#     if len(i) > len(urtug):
#         urtug = i
# print(urtug)
# # task 3
# count = 0
# n = input("Ug: ").split()
# for i in n:
#     if i == "a" or "e" or "o":
#         count += 1
# print(count)
# # task 4
# count = 0
# n = input("ugs: ").split()
# m = input("ug: ")
# for i in n:
#     if m == i:
#         count += 1
# print(count)
# # task 5
# n = input("ugs: ").split()
# n.sort()
# print(n)
# # task 6
# n = input("apl ugs: ").split()
# for i in n:
#     if i[::-1] == i:
#         print(i, end=" ")
# # task 7
# n = input("ners: ").split()
# for i in n:
#     print(i, len(i))
# # task 8
# n = input("ug: ")
# temdegt = 0
# dawt = 0
# for i in n:
#     count = n.count(i)
#     if count > temdegt:
#         temdegt = count
#         dawt = i
# print(dawt, temdegt)
# # task 9
# n = input("ugs: ").split()
# new = []
# for i in n:
#     if i not in  new:
#         new.append(i)
# print(*new)
# # task 10
# x = input("ner, onoo: ").split()
# ih = 0
# for i in x:
#     name, score = i.split(":")
#     score = int(score)
#     if score > ih:
#         ih = score
# for i in x:
#     name, score = i.split(":")
#     score = int(score)
#     if score == ih:
#         print(name, score)
#######################################            hard              ############################################
#######################################            hard              ############################################
# # task 1
# s = input("Og uulber: ")
# words = s.split()
# lengths = []
# for word in words:
#     if len(word) not in lengths:
#         lengths.append(len(word))
# lengths.sort(reverse=True)
# if len(lengths) < 2:
#     print("NO")
# else:
#     for word in words:
#         if len(word) == lengths[1]:
#             print(word)
#             break
# # task 2
# s = input("Text: ")
# result = ""
# count = 1
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         result += s[i - 1] + str(count)
#         count = 1
# if len(s) > 0:
#     result += s[-1] + str(count)
# print(result)
# # task 3
# s = input("Og uulber: ")
# words = s.split()
# result = []
# for word in words:
#     result.append(word[::-1])
# print(" ".join(result))
# # task 4
# s = input("Og uulber: ")
# words = s.split()
# big = 0
# answer = ""
# for word in words:
#     count = 0
#     for letter in word.lower():
#         if letter in "aeiou":
#             count += 1
#     if count > big:
#         big = count
#         answer = word
# print(answer, big)
# # task 5
# a = input("Ug 1: ").lower()
# b = input("Ug 2: ").lower()
# if sorted(a) == sorted(b):
#     print("YES")
# else:
#     print("NO")
# # task 6
# s = input("Og uulber: ")
# words = s.split()
# checked = []
# for word in words:
#     if word not in checked:
#         count = 0
#         for w in words:
#             if w == word:
#                 count += 1
#         if count > 1:
#             print(word, count)
#         checked.append(word)
# # task 7
# s = input("Og uulber: ")
# s = s.lower().replace(" ", "")
# if s == s[::-1]:
#     print("YES")
# else:
#     print("NO")
# # task 8
# s = input("Og uulber: ")
# words = s.split()
# result = []
# for word in words:
#     for letter in word:
#         if letter.isdigit():
#             result.append(word)
#             break
# if len(result) > 0:
#     print(" ".join(result))
# else:
#     print("NO")
# # task 9
# password = input("Nuuts ug: ")
# upper = False
# lower = False
# digit = False
# special = False
# space = False
# for letter in password:
#     if letter.isupper():
#         upper = True
#     if letter.islower():
#         lower = True
#     if letter.isdigit():
#         digit = True
#     if letter in "!@#$":
#         special = True
#     if letter == " ":
#         space = True
# if len(password) >= 8 and upper and lower and digit and special and space == False:
#     print("STRONG")
# else:
#     print("WEAK")
# # task 10
# s = input("Suragchid: ")
# students = s.split()
# names = []
# scores = []
# for student in students:
#     name, score = student.split(":")
#     names.append(name)
#     scores.append(int(score))
# highest = max(scores)
# average = round(sum(scores) / len(scores), 1)
# print("Highest:", end=" ")
# for i in range(len(scores)):
#     if scores[i] == highest:
#         print(names[i], end=" ")
# print()
# print("Average:", average)
# print("Above average:", end=" ")
# for i in range(len(scores)):
#     if scores[i] > average:
#         print(names[i], end=" ")
# print()
# print("Failed:", end=" ")
# for i in range(len(scores)):
#     if scores[i] < 60:
#         print(names[i], end=" ")
# print()


