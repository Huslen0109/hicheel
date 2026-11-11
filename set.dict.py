
# # TASK1
# n = list(map(int, input("Too: ").split()))
# b = set(n)
# print(b)
# # task2
# n = set(input().split())
# b = input("nemeh: ")
# n.add(b)
# print(n)
# # task3
# n = set(input().split())
# b = input()
# n.remove(b)
# print(n)
# # task 4
# n = set(map(int, input("too: ").split()))
# b = int(input("too: "))
# if b in n:
#     print("yes")
# else:
#     print("No")
# # task 5
# n = set(map(int, input("Too: ").split()))
# print(len(n))
# # task 6
# n = input("ners: ").split()
# b = set(n)
# print(len(b))
# # task 7
# n = set(map(int, input("too: ").split()))
# b = set(map(int, input("too: ").split()))
# print(n | b)
# # task 8
# n = set(map(int, input("too: ").split()))
# b = set(map(int, input("too: ").split()))
# print(n & b)
# # task 9
# n = set(map(int, input("too: ").split()))
# b = set(map(int, input("too: ").split()))
# print(n - b)
# # task 10
# a = set(input("txt: ").split())
# b = set(input("txt: ").split())
# print(a & b)
# # task 11
# b = set(input("txt: ").split())
# a = set(input("txt: ").split())
# print(a - b, b - a)
# # task 12
# word = input("txt: ")
# letters = set(word)
# print(len(letters))
# # task 13
# name = input()
# age = int(input())
# score = int(input())
# student = {
#     "name": name,
#     "age": age,
#     "score": score
# }
# print(student)
# # task 14
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 90
# }
# print(student["name"])
# # task 15
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 85
# }
# student["score"] = 98
# print(student)
# # task 16
# student = {
#     "name": "Anu",
#     "age": 18
# }
# student["city"] = "Ulaanbaatar"
# print(student)
# # task 17
# student = {
#     "name": "Bold",
#     "age": 20,
#     "score": 88
# }
# del student["age"]
# print(student)

# # task 18
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# for key in car:
#     print(key)
# # task 19
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# for i in car.values():
#     print(i)
# # task 20
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 95
# }
# print(student.items())
# # task 21
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 92
# }
# print("score" in student)
# # task 22
# product = {
#     "name": "Keyboard",
#     "price": 120000,
#     "stock": 5
# }
# if product["stock"] > 0:
#     print("Available")
# else:
#     print("Out of stock")
# # task 23
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# for i in scores.values():
#     if i > 80:
#         print(i)
# # task 24
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# max_score = 0
# max_name = ""
# for name, score in scores.items():
#     if score > max_score:
#         max_score = score
#         max_name = name
# print(max_name, max_score)
# # task 25
# sales = {
#     "Monday": 10,
#     "Tuesday": 15,
#     "Wednesday": 20
# }
# total = 0
# for value in sales.values():
#     total += value
# print(total)
# # task 26
# sentence = input("Uguulber: ")
# words = sentence.split()
# count = {}
# for word in words:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1
# for word, number in count.items():
#     print(word, number)
# # task 27
# students = {
#     "Bat": ["Python", "Java"],
#     "Sara": ["Python", "C++"],
#     "Bold": ["Java", "Python"]
# }
# subjects = set()
# for lessons in students.values():
#     for lesson in lessons:
#         subjects.add(lesson)
# print(subjects)
# # task 28
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Temuulen": "Darkhan"
# }
# cities = set(students.values())
# print(len(cities))
# # task 29
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet"
# }
# for name, city in students.items():
#     if city == "Ulaanbaatar":
#         print(name)
# # task 30
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30,
#     "e": 20
# }
# unique = set(data.values())
# print(unique)


#################################   medium   ######################################

# # task 1

# user1=set(input("User 1 friends: ").split())
# user2=set(input("User 2 friends: ").split())
# print(user1 & user2)

# # task 2
# players=set(input("All players: ").split())
# played=set(input("Played players: ").split())
# print(players-played)

# # task 3

# team_a=set(input("Team A: ").split())
# team_b=set(input("Team B: ").split())
# print((team_a-team_b)|(team_b-team_a))

# # task 4

# known=set(input("Known languages: ").split())
# required=set(input("Required languages: ").split())
# print(*sorted(required-known))

# # tasl 5

# subjects=input("Subjects: ").split()
# unique=set(subjects)
# print("Count:",len(unique))
# print("Subjects:",unique)

# # task 6

# password=input("Password: ")
# letters=set()
# digits=set()
# for c in password:
#     if c.isalpha():
#         letters.add(c)
#     elif c.isdigit():
#         digits.add(c)
# print("Letters:",len(letters))
# print("Digits:",len(digits))

# # task 7

# word1=input("First word: ")
# word2=input("Second word: ")
# characters=set(word1+word2)
# print("Count:",len(characters))
# print(characters)

# # task 8

# n=int(input("Student count: "))
# students={}
# for i in range(n):
#     name=input("Name: ")
#     students[name]=int(input("Score: "))
# for name,score in students.items():
#     if score>=90:
#         print(name,"- Excellent")
#     elif score>=60:
#         print(name,"- Pass")
#     else:
#         print(name,"- Fail")

# # task 9

# products={"apple":3000,"banana":2500,"milk":4500,"bread":3500}
# name=input("Product: ")
# count=int(input("Quantity: "))
# if name in products:
#     print("Total:",products[name]*count)
# else:
#     print("Product not found")

# # task 10

# n=int(input("Product count: "))
# sales={}
# for i in range(n):
#     name=input("Product: ")
#     sales[name]=int(input("Sold: "))
# if sales:
#     name=max(sales,key=sales.get)
#     print(name,sales[name])

# # task 11

# n=int(input("Employee count: "))
# employees={}
# for i in range(n):
#     name=input("Name: ")
#     employees[name]=int(input("Salary: "))
# for name in employees:
#     if employees[name]<1500000:
#         employees[name]=int(employees[name]*1.1)
# print(employees)

# # task 12

# n=int(input("People count: "))
# people={}
# for i in range(n):
#     name=input("Name: ")
#     people[name]=int(input("Age: "))
# for name,age in people.items():
#     if age>=18:
#         print(name)

# # task 13

# n=int(input("Student count: "))
# scores={}
# for i in range(n):
#     name=input("Name: ")
#     scores[name]=int(input("Score: "))
# for name in scores:
#     scores[name]=min(100,scores[name]+5)
# print(scores)

# # task 14

# n=int(input("Product count: "))
# products={}
# for i in range(n):
#     name=input("Product: ")
#     products[name]=int(input("Price: "))
# price=int(input("Minimum price: "))
# for name,value in products.items():
#     if value>price:
#         print(name)

# # task 15

# n=int(input("Student count: "))
# students={}
# for i in range(n):
#     name=input("Name: ")
#     students[name]=input("City: ")
# city=input("Search city: ")
# result=set()
# for name,value in students.items():
#     if value==city:
#         result.add(name)
# print(result)


# # task 16

# n=int(input("Player count: "))
# games={}
# for i in range(n):
#     name=input("Name: ")
#     games[name]=set(input("Games: ").split())
# result=set()
# for name,game in games.items():
#     if "CS2" in game:
#         result.add(name)
# print(result)

# # task 17

# n=int(input("Player count: "))
# games={}
# for i in range(n):
#     name=input("Name: ")
#     games[name]=set(input("Games: ").split())
# result=set()
# for game in games.values():
#     result.update(game)
# print(result)

# # tak 18

# n=int(input("Player count: "))
# games={}
# for i in range(n):
#     name=input("Name: ")
#     games[name]=set(input("Games: ").split())
# for name,game in games.items():
#     if "CS2" in game and "WoW" in game:
#         print(name)

# # task 19

# n=int(input("Student count: "))
# skills={}
# for i in range(n):
#     name=input("Name: ")
#     skills[name]=set(input("Skills: ").split())
# for name,skill in skills.items():
#     if "Python" in skill and "JavaScript" in skill:
#         print(name)

# # task 20

# n=int(input("Employee count: "))
# employees={}
# for i in range(n):
#     name=input("Name: ")
#     employees[name]=set(input("Languages: ").split())
# for name,language in employees.items():
#     if "English" in language and "Korean" not in language:
#         print(name)

# # task 21

# web_users=set(input("Web users: ").split())
# mobile_users=set(input("Mobile users: ").split())
# result=web_users&mobile_users
# print(result)
# print("Total:",len(result))

# # task 22

# n=int(input("User count: "))
# status={}
# for i in range(n):
#     name=input("Name: ")
#     status[name]=input("Status: ")
# online=set()
# for name,value in status.items():
#     if value=="online":
#         online.add(name)
# print(online)
# name=input("Search name: ")
# if name in online:
#     print("Online")
# else:
#     print("Offline or not found")

# # task 23

# n=int(input("Course count: "))
# courses={}
# for i in range(n):
#     course=input("Course: ")
#     courses[course]=set(input("Students: ").split())
# name=input("Search student: ")
# for course,students in courses.items():
#     if name in students:
#         print(course)

# # task 24

# n=int(input("Course count: "))
# courses={}
# for i in range(n):
#     course=input("Course: ")
#     courses[course]=set(input("Students: ").split())
# counts={}
# for students in courses.values():
#     for name in students:
#         counts[name]=counts.get(name,0)+1
# if counts:
#     highest=max(counts.values())
#     for name,count in counts.items():
#         if count==highest:
#             print(name,count)
















