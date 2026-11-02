# # task 1
# n = int(input("nas: "))
# if n >= 18:
#     print("yse")
# else:
#     print("no")
# # task 2
# n = int(input("Too: "))
# if n % 2 == 0:
#     print("tegshg")
# else:
#     print("sondgoi")
# # task 3
# a, b = map(int, input("Too: ").split())
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# elif a == b:
#     print("tentsuu")
# # task 4
# n = int(input("Too: "))
# if n == 7:
#     print("margaash ajiltai")
# # task 5
# km = int(input("Явсан км: "))
# hour = int(input("Цаг: "))
# if km <= 2:
#     price = 3000
# else:
#     price = 3000 + (km - 2) * 1500
# if hour >= 22 or hour < 6:
#     price = price * 1.2
# print(int(price))
# # task 6
# n = int(input("kWt: "))
# if n <= 150:
#     price = n * 100
# elif n > 150 and n < 300:
#     price = 150 * 100 + (n - 150) * 150
# elif n > 300:
#     price = 150 * 100 + 150 * 150 + (n - 300)* 200
# print(price)
# # task 7
# failed = 0
# while True:
#     username = input("Username: ")
#     if username == "":
#         print("medeelel dutuu")
#         continue
#     if username != "admin":
#         print("hereglegch oldsongui")
#         continue
#     while True:
#         password = input("Password: ")
#         if password == "":
#             print("medeelel dutuu")
#             continue
#         if password == "1234":
#             print("wellcome")
#             break
#         failed += 1
#         if failed >= 2:
#             print("blockde")
#             break
#         else:
#             print("worng password")
#     break
############################################## task 2.1
# n = int(input("too"))
# for i in  range(1, n+1):
#     print(i)
# # task 2
# total = 0
# n = int(input("Too: "))
# for i in range(1, n +1):
#     if i % 2 == 0:
#         total += i
#         print(total)
# # task 3
# n = int(input("Too: "))
# for i in range(1, 11):
#     print(f"{n} * {i} = {i * n}")
# # task 4
# n = int(input("Mongo: "))
# b = int(input("goal: "))
# count = 0
# while n < b:
#     n = n * 1.12
#     count += 1
# print(count, "jil")
# # task 5
# count = 0
# n = int(input("Too: "))
# for i in range(1, n +1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("anhnii too")
# elif count > 2:
#     print(count)
# # task 6
# n = int(input("Too: "))
# for i in range(1, n + 1):
#     if i % 3 != 0:
#         continue
#     print(i)
# # task 7
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()
# # task 8
# count = 0
# while True: 
#     n = int(input("Too: "))
#     secret = 42
#     if n > secret:
#         count += 1
#         print("IH baina")
#     elif n < secret:
#         count += 1
#         print("baga baina")
#     elif n == secret:
#          count += 1
#          print(f"taachlashde psda")
#          print(f"Niit oroldlogo: {count}")
#          break
#     if count == 5:
#         print("muu loser 5n udaa buruu shaachlaa too n 42 bsiin")
#         break
# # task 9
# n = int(input("Too: "))
# while n >= 10:
#     total = 0
#     while n > 0:
#         i = n % 10
#         total += i
#         n //= 10
#     n = total
# print(n)
################################### task 3.1
# # task 1
# total = 0
# avg = 0
# count = 0
# n = list(map(int, input("too: ").split()))
# for i in n:
#     total += i
#     count += 1
#     avg = total / count
# print(f"niilber: {total}")
# print(f"dundaj: {avg}")
# # task 2
# n = list(map(int, input("too: ").split()))
# ihtoo = 0
# a = []
# for i in n:
#     if i > ihtoo:
#         ihtoo = i
#         if i not in a:
#             a.append(i)
#             index = a.index(ihtoo)
# print("hamgiin ih: ", ihtoo, index)
# # task 3
# n = input("name: ").split()
# b = input("oloh ner: ")
# if b in n:
#     index = n.index(b)
#     print("oldloo", index)
# elif b not in n:
#     print("oldsongui")
# # taks 4
# n = list(map(int, input("une: ").split()))
# b  = []
# for i in n:
#     c = int(i * 0.9)
#     b.append(c)
# print(n, b)
# # task 5
# n = list(map(int, input("Too: ").split()))
# count = 0
# a = []
# for i in n:
#     if i > 60:
#         a.append(i)
#         count += 1
# print(a, count)
# # task 6
# n = list(map(int, input("Zahialgiin vne: ").split()))
# a = []
# for i in n:
#     if i > 5000:
#         a.append(i)
#         c = len(a) * 2000
# print(sum(a) + c)
# ##################################### task 7
# n = int(input("heden suragch: "))
# m = int(input("heden hicheel: "))
# names = []
# scores = []
# subjects = []
# for i in range(n):
#     a = input("suragchiin ner: ")
#     names.append(a)
#     duns = []
#     for j in range(m):
#         b = input("hicheelin ner ba dvn: ").split()
#         c = int(b[1])
#         duns.append(c)
#         if i == 0:
#             subjects.append(b[0])
#     scores.append(duns)
#     print(a, sum(duns) / len(duns))
# for j in range(m):
#     max_score = scores[0][j]
#     max_name = names[0]
#     for i in range(n):
#         if scores[i][j] > max_score:
#             max_score = scores[i][j]
#             max_name = names[i]
#     print(subjects[j], max_name, max_score)
# ###################################################### task 4.1
# word = input("Ug: ")
# word = word[0].upper() + word[1:]
# print(word, len(word), "vseg")
# # task 2
# n = input("ug: ")
# m = input("haih vseg: ")
# count = 0
# for i in n:
#     if i == m:
#         count += 1
# print(count)
# # task 3
# n = input("Mail: ")
# if n.count("@") != 1 or n.startswith("@") or n.endswith("."):
#     print("Buruu email")
# else:
#     username, domain = n.split("@")
#     if "." not in domain:
#         print("Buruu email")
#     else:
#         print("Username:", username)
#         print("Domain:", domain)
# # task 4
# n = input("txt: ")
# b = ["sda", "lalar", "gichii", "ynhan", "al", "boow", "vtree", "batsaan"]
# for i in b:
#     if i in n:
#         n = n.replace(i, "(buzartai vg tul ene txteer solicy)")
# print(n)
# # task 5
# text = input("Text: ")
# clean = ""
# for i in text:
#     if i.isalnum():
#         clean += i.lower()
# if clean == clean[::-1]:
#     print(True)
# else:
#     print(False)
############################################################# task 5.1
# def square(n):
#     return n * n
# n = int(input("Too: "))
# print(square(n))
# # task 2
# def greet(name="asd"):
#     return "sainuu, " + name + "!"
# name = input("ner: ")
# if name == "":
#     print(greet())
# else:
#     print(greet(name))
# # task 3
# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False
# age = int(input("nas: "))
# print(is_adult(age))
# task 4
