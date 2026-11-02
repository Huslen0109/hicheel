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
# n = input("ugs: ").split()
# urt1 = ""
# urt2 = "" 
# for i in n:
#     if len(i) > len(urt1):
#         urt2 = urt1
#         urt1 = i
#     elif len(i) > len(urt2):
#         urt2 = i
# print(urt2)
