
# # task 1.1
# age = int(input("Nas: "))
# if age >= 18:
#     print("Oroh bolomjtoi")
# else:
#     print("Oroh bolomjgui")
# # task 1.2
# n = int(input("Too: "))
# if n % 2 == 0:
#     print("Tegsh")
# else:
#     print("Sondgoi")
# # task 1.3
# a = int(input("a: "))
# b = int(input("b: "))
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print("Tentsuu")
# # task 1.4
# day = int(input("Odor: "))
# if day == 1:
#     print("Davaa")
# elif day == 2:
#     print("Myagmar")
# elif day == 3:
#     print("Lhagva")
# elif day == 4:
#     print("Purev")
# elif day == 5:
#     print("Baasan")
# elif day == 6:
#     print("Byamba (Amraltiin odor)")
# elif day == 7:
#     print("Nyam (Amraltiin odor)")
# else:
#     print("Buruu too")
# # task 1.5
# km = int(input("Km: "))
# hour = int(input("Tsag: "))
# if km <= 2:
#     price = 3000
# else:
#     price = 3000 + (km - 2) * 1500
# if hour >= 22 or hour < 6:
#     price = price * 1.2
# print(int(price))
# # task 1.6
# kwh = int(input("Kwh: "))
# if kwh <= 150:
#     price = kwh * 100
# elif kwh <= 300:
#     price = 150 * 100 + (kwh - 150) * 150
# else:
#     price = 150 * 100 + 150 * 150 + (kwh - 300) * 200
# print(price)
# # task 1.7
# username = input("Ner: ")
# password = input("Nuuts ug: ")
# is_blocked = input("Blocked (True/False): ")
# failed_attempts = int(input("Aldaa: "))
# if is_blocked == "True":
#     print("Tanii erh haagdsan baina")
# elif username == "" or password == "":
#     print("Medeelel bureen oruulna uu")
# elif username != "admin":
#     print("Hereglegch oldsongui")
# elif password != "1234":
#     if failed_attempts >= 2:
#         print("Erh haagdlaa")
#     else:
#         print("Nuuts ug buruu")
# else:
#     print("Amjilttai nevterlee")
# # task 2.1
# n = int(input("N: "))
# for i in range(1, n + 1):
#     print(i)
# # task 2.2
# n = int(input("N: "))
# total = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total += i
# print(total)
# # task 2.3
# n = int(input("Too: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
# # task 2.4
# money = 1000000
# year = 0
# while money < 2000000:
#     money = money * 1.12
#     year += 1
# print(year, "jil")
# # task 2.5
# n = int(input("Too: "))
# if n < 2:
#     print(n, "anhnii too bish")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(n, "anhnii too bish,", str(i) + "-t huvaagdana")
#             break
#     else:
#         print(n, "anhnii too")
# # task 2.6
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")
# print()
# # task 2.7
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()
# # task 2.8
# secret = 42
# guesses = [50, 30, 42, 10]
# found = False
# for i in range(5):
#     if i >= len(guesses):
#         break
#     n = guesses[i]
#     if n > secret:
#         print(n, ": Ih baina", sep="")
#     elif n < secret:
#         print(n, ": Baga baina", sep="")
#     else:
#         print(n, ": Zow! ", i + 1, " dahi oroldlogoor taalaa", sep="")
#         found = True
#         break
# if found == False:
#     print("Ylagdlaa. Nuuts too:", secret)
# # task 2.9
# n = int(input("Too: "))
# if n < 0:
#     n = 0 - n
# while n >= 10:
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     n = total
# print(n)
# # task 3.1
# scores = [80, 90, 70, 60]
# total = 0
# count = 0
# for score in scores:
#     total += score
#     count += 1
# average = total / count
# print("Niilber:", total)
# print("Dundaj:", average)
# # task 3.2
# scores = [45, 89, 72, 89, 30]
# big = scores[0]
# index = 0
# for i, score in enumerate(scores):
#     if score > big:
#         big = score
#         index = i
# print("Hamgiin ih:", big, "index:", index)
# # task 3.3
# names = ["Bat", "Saraa", "Dorj"]
# name = input("Ner: ")
# if name in names:
#     print("Oldloo, index:", names.index(name))
# else:
#     print("Oldsongui")
# # task 3.4
# prices = [1000, 2500, 8000]
# new_prices = [int(p * 0.9) for p in prices]
# print(new_prices)
# new_prices2 = list(map(lambda p: int(p * 0.9), prices))
# print(new_prices2)
# # task 3.5
# scores = [45, 78, 60, 30, 92]
# passed = [s for s in scores if s >= 60]
# print(passed, "Tentssen:", len(passed))
# passed2 = list(filter(lambda s: s >= 60, scores))
# print(passed2, "Tentssen:", len(passed2))
# # task 3.6
# orders = [1200, 45000, 8000, 23000, 500]
# total = 0
# for order in orders:
#     if order >= 5000:
#         total += order + 2000
# print(total)
# total2 = sum(order + 2000 for order in orders if order >= 5000)
# print(total2)
# # task 3.7
# names = ["Bat", "Saraa", "Dorj"]
# subjects = ["Matematik", "Fizik", "Angli", "Tuuh"]
# scores = [[80, 90, 70, 60], [95, 85, 75, 65], [50, 60, 70, 80]]
# for i in range(len(names)):
#     total = 0
#     for score in scores[i]:
#         total += score
#     print(names[i] + ":", total / len(scores[i]))
# for j in range(len(subjects)):
#     big = scores[0][j]
#     best = names[0]
#     for i in range(len(names)):
#         if scores[i][j] > big:
#             big = scores[i][j]
#             best = names[i]
#     print(subjects[j] + ":", best, "(" + str(big) + ")")
# # task 4.1
# name = input("Ner: ")
# name = name.capitalize()
# print(name, "(" + str(len(name)) + " useg)")
# # task 4.2
# word = input("Ug: ")
# letter = input("Useg: ")
# count = 0
# for ch in word:
#     if ch == letter:
#         count += 1
# print(count)
# print(word.count(letter))
# # task 4.3
# email = input("Email: ")
# if email.count("@") == 1 and email[0] != "@":
#     username, domain = email.split("@")
#     if "." in domain and domain[-1] != "." and domain[0] != ".":
#         print("Username:", username)
#         print("Domain:", domain)
#     else:
#         print("Buruu email")
# else:
#     print("Buruu email")
# # task 4.4
# bad_words = ["muu", "teneg"]
# text = input("Og uulber: ")
# words = text.split()
# result = []
# for word in words:
#     if word.lower() in bad_words:
#         result.append("*" * len(word))
#     else:
#         result.append(word)
# print(" ".join(result))
# # task 4.5
# text = input("Text: ")
# clean = ""
# for ch in text.lower():
#     if ch.isalnum():
#         clean += ch
# print(clean == clean[::-1])
# left = 0
# right = len(clean) - 1
# palindrome = True
# while left < right:
#     if clean[left] != clean[right]:
#         palindrome = False
#         break
#     left += 1
#     right -= 1
# print(palindrome)
# # task 5.1
# def square(n):
#     return n * n
# print(square(5))
# print(square(-3))
# # task 5.2
# def greet(name="Zochin"):
#     return "Sain uu, " + name + "!"
# print(greet("Bat"))
# print(greet())
# # task 5.3
# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False
# print(is_adult(20))
# print(is_adult(16))
# # task 5.4
# def calculate_bmi(weight, height):
#     return round(weight / (height * height), 2)
# def get_category(bmi):
#     if bmi < 18.5:
#         return "Turanhai"
#     elif bmi < 25:
#         return "Heviin"
#     elif bmi < 30:
#         return "Iluudel jintei"
#     else:
#         return "Targalalttai"
# weight = float(input("Jin: "))
# height = float(input("Ondor: "))
# bmi = calculate_bmi(weight, height)
# print("BMI:", bmi, get_category(bmi))
# # task 5.5
# def calc_insurance(gross):
#     return gross * 0.115
# def calc_tax(gross):
#     insurance = calc_insurance(gross)
#     return (gross - insurance) * 0.10
# def calc_net(gross):
#     insurance = calc_insurance(gross)
#     tax = calc_tax(gross)
#     return gross - insurance - tax
# gross = int(input("Tsalin: "))
# print("NDSH:", int(calc_insurance(gross)))
# print("Tatvar:", int(calc_tax(gross)))
# print("Gart:", int(calc_net(gross)))
# # task 5.6
# def make_counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     def decrement():
#         nonlocal count
#         count -= 1
#         return count
#     def reset():
#         nonlocal count
#         count = 0
#         return count
#     return {"increment": increment, "decrement": decrement, "reset": reset}
# c1 = make_counter()
# c2 = make_counter()
# print(c1["increment"]())
# print(c1["increment"]())
# print(c2["increment"]())
# print(c1["decrement"]())
# print(c1["reset"]())
# # task 6.1
# user = {"name": "Bat", "age": 20, "city": "Ulaanbaatar"}
# print(user)
# user["age"] += 1
# user["email"] = "bat@mail.com"
# del user["city"]
# print(user)
# # task 6.2
# prices = {"talh": 2500, "suu": 3800, "mah": 18000}
# for name, price in prices.items():
#     print(name, "-", str(price) + " tugrug")
# # task 6.3
# prices = {"talh": 2500, "suu": 3800, "mah": 18000, "ondog": 6500}
# best = ""
# big = 0
# total = 0
# for name, price in prices.items():
#     total += price
#     if price > big:
#         big = price
#         best = name
# print("Hamgiin unetei:", best, "-", str(big) + " tugrug")
# print("Niit:", str(total) + " tugrug")
# # task 6.4
# votes = ["Bat", "Saraa", "Bat", "Dorj", "Bat", "Saraa"]
# result = {}
# for name in votes:
#     result[name] = result.get(name, 0) + 1
# print(result)
# best = ""
# big = 0
# for name, count in result.items():
#     if count > big:
#         big = count
#         best = name
# print("Ylagch:", best, "(" + str(big), "sanal)")
# # task 6.5
# students = [{"name": "Bat", "class": "10A", "score": 85}, {"name": "Saraa", "class": "10B", "score": 92}, {"name": "Dorj", "class": "10A", "score": 70}, {"name": "Naraa", "class": "10B", "score": 78}, {"name": "Temuulen", "class": "10A", "score": 95}]
# groups = {}
# for student in students:
#     cls = student["class"]
#     if cls not in groups:
#         groups[cls] = []
#     groups[cls].append(student["name"])
# print(groups)
# # task 6.6
# students = [{"name": "Bat", "class": "10A", "score": 85}, {"name": "Saraa", "class": "10B", "score": 92}, {"name": "Dorj", "class": "10A", "score": 70}, {"name": "Naraa", "class": "10B", "score": 78}, {"name": "Temuulen", "class": "10A", "score": 95}]
# groups = {}
# for student in students:
#     cls = student["class"]
#     if cls not in groups:
#         groups[cls] = []
#     groups[cls].append(student)
# for cls, members in groups.items():
#     total = 0
#     big = members[0]["score"]
#     best = members[0]["name"]
#     for student in members:
#         total += student["score"]
#         if student["score"] > big:
#             big = student["score"]
#             best = student["name"]
#     average = round(total / len(members), 2)
#     print(cls, "- dundaj:", average, "shildeg:", best, "(" + str(big) + ")")
# # task 6.7
# books = {"Harri Potter": 1, "Sherlok Holms": 2}
# loans = {}
# def borrow(person, title):
#     if title not in books:
#         return "Iim nom baihgui"
#     if books[title] == 0:
#         return "Buh huvi zeelegdsen baina"
#     if person not in loans:
#         loans[person] = []
#     if len(loans[person]) >= 3:
#         return "Hamgiin ihdee 3 nom zeelne"
#     books[title] -= 1
#     loans[person].append(title)
#     return "Amjilttai zeellee"
# def return_book(person, title):
#     if person not in loans:
#         return "Ene nomiig zeeleegui baina"
#     if title not in loans[person]:
#         return "Ene nomiig zeeleegui baina"
#     books[title] += 1
#     loans[person].remove(title)
#     return "Amjilttai butsaalaa"
# print(borrow("Bat", "Harri Potter"))
# print(borrow("Saraa", "Harri Potter"))
# print(borrow("Bat", "Hobbi"))
# print(return_book("Saraa", "Sherlok Holms"))
# print(return_book("Bat", "Harri Potter"))
# print(borrow("Saraa", "Harri Potter"))
