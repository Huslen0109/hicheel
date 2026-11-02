
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