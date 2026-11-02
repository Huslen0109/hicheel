# # task 1
# n = input("ner: ")
# print("sainuu, ",n)

# # task 2
# n = map(int,input("too: ").split())
# print(sum(n))

# # task 3
# n = float(input("une: "))
# print(2 * n)

# # task 5
# n = input("text: ")
# print(len(n))

# # task 6
# n = input("text; ")
# print(n[0], n[-1])
# # task 7

# n = int(input("too: "))
# for i in range( 1,n+1):
#     print(i)
# # task 8

# n = map(int,input("too: ").split())
# print(sum(n))
# # task 9

# n = list(map(int, input("too: ").split()))
# print(max(n), min(n))
# # task 10

# n = list(map(int, input("Too: ").split()))
# avrg = sum(n)/len(n)
# print(round(avrg, 2)

# # task 11
# n = input("amitna: ").split()
# n.append("tiger")
# print(n)

# # task 12
# n = input("animals: ").split()
# n.insert(1, "tiger")
# print(n)
# # task 13
# n = input("txt: ").split()
# m = input("txt: ")
# n.remove(m)
# print(n)
# # Task 14
# n = input("txt: ").split()
# m  = int(input("index: "))
# delete = n.pop(m)
# print(delete)
# print(",".join(n))
# # task 15
# n = list(map(int, input().split()))
# n.sort()
# print(n)
# n.reverse()
# print(n)
# # task 16
# n = list(map(int, input("too: ").split()))
# n.reverse()
# print(n)
# # task 17
# n = input("txt: ")
# print(f"[{n.strip()}]")
# print(f"[{n.lstrip()}]")
# print(f"[{n.rstrip()}]") 
# # task 18
# n = input("txt: ").split()
# print(len(n))
# # task 19
# n = input("txt: ")
# m = input()
# j = n.lower()
# i = m.lower()
# print(j.count(m))
# # task 20
# text = input("txt: ")
# n = input("find: ")
# m = text.find(n)
# print(m)
# if m != -1:
#     print(text.index(n))
# else:
#     print("mt")
# # task 21
# n = input("txt: ").split()
# m = []
# for i in n:
#     if i.startswith("report") and i.endswith(".pdf"):
#         m.append(i)
# if len(m) == 0:
#     print("oldsngu")
# else:
#     for i in m:
#         print(i)
# # task 22
# n = input("txt: ")
# m = input("soligdoh ug: ")
# a = input("solih ug: ")
# n = n.replace(m, a)
# print(n)
# # task 23
# n = input("txt: ").split()
# m = input("txt: ")
# if m in n:
#     print("yes")
# else:
#     print("no")
# # task 24
# n = input("txt: ")
# b = n[0:3]
# c = n[-3:]
# print(b, c)
# # task 25
# n = input("txt: ")
# n = n.strip()
# n = n.lower()
# if n == n[::-1]:
#     print("yes")
# else:
#     print("no")
# # task 26
# n = input("txt: ").split()
# urtug = ""
# for i in n:
#     if len(i) > len(urtug):
#         urtug = i
# print(urtug)
# # task 27
# n = input().split(",")
# name = n[0].strip()
# age = int(n[1].strip())
# city = n[2].strip()
# print(name, "| Ирэх жил:", age+1, "|", city)
# # task 28
# n = input("txt: ").lower().split()
# new = []
# for i in n:
#     if i not in new:
#         new.append(i)
# new.sort()
# print(" ".join(new))
# # task 29
# n = map(int, input("too: ").split())
# new = []
# for i in n:
#     if int(i) not in new:
#         new.append(i)
#         new.sort()
# print(new[-2])
# # task 30
# n = int(input("Heden suragch: "))
# names = []
# scores = []
# for i in range(n):
#     m = input("ner, dun: ").split()
#     name = m[0].rstrip(",")
#     score = int(m[1])
#     names.append(name)
#     scores.append(score)
# dundaj = sum(scores) / len(scores)
# maxscore = max(scores)
# index = scores.index(maxscore)
# print(f"dundaj dun: {round(dundaj, 2)}")
# print(f"hamgiin ondor: {names[index]} {maxscore}")
# print(f"ners: {', '.join(names)}")