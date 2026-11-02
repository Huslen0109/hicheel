# # task 1
# class Student:
#     def __init__(self, name, age):
#         self.ner = name
#         self.nas = age
# Students = []
# n = int(input("heden suragch: "))
# for i in range(n):
#     ner = input(f"{i+1}-r suragchiin ner: ")
#     nas = int(input(f"{i+1}-r suragchiin nas: "))
#     Students.append(Student(ner, nas))
# for Student in Students:
#     print(Student.ner, Student.nas)
# # task 3
# class Student:
#     def __init__(self, name, age, grade):
#         self.ner = name
#         self.nas = age
#         self.angi = grade
# Students = []
# n = int(input("heden suragch: "))
# for i in range(n):
#     ner = input(f"{i+1}-r suragchiin ner: ")
#     nas = int(input(f"{i+1}-r suragchiin nas: "))
#     angi = input(f"{i+1}-r suragchiin angi: ")
#     Students.append(Student(ner, nas, angi))
# m = int(input("hed dahi suragchiin data: "))
# print(Students[m-1].ner)
# print(Students[m-1].nas)
# print(Students[m-1].angi)
# # task 4
# class Student:
#     def __init__(self, name, age):
#         self.ner = name
#         self.nas = age
# Students = []
# n = int(input("heden suragch: "))
# for i in range(n):
#     ner = input(f"{i+1}-r suragchiin ner: ")
#     nas = int(input(f"{i+1}-r suragchiin nas: "))
#     Students.append(Student(ner, nas))
# for Student in Students:
#     print(Student.ner, Student.nas)
# # task 5
# class Student:
#     def __init__(self, name, score):
#         self.ner = name
#         self.onoo = score
#     def add_score(self):
#         self.onoo += 5
# suragch = []
# n = int(input("Heden suragch: "))
# for i in range(n):
#     ner = input("Ner: ")
#     onoo = int(input("Onoo: "))
#     suragch.append(Student(ner, onoo))
# for k in suragch:
#     if k.onoo < 60:
#         k.add_score()
#     print(k.ner, k.onoo)
# # task 6
# class Student:
#     def __init__(self, name, age, grade):
#         self.ner = name
#         self.nas = age
#         self.angi = grade
# Students = []
# n = int(input("heden suragch: "))
# for i in range(n):
#     ner = input(f"{i+1}-r suragchiin ner: ")
#     nas = int(input(f"{i+1}-r suragchiin nas: "))
#     angi = input(f"{i+1}-r suragchiin angi: ")
#     Students.append(Student(ner, nas, angi))
# m = int(input("hed dahi suragchiin data: "))
# print(Students[m-1].ner)
# print(Students[m-1].nas)
# print(Students[m-1].angi)
# # task 7
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def check(self):
#         if self.score < 60:
#             return "unasan"
#         else:
#             return "tentssen"
# Students = []
# n = int(input("Heden suragch: "))
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     Students.append(Student(name, score))
# for j in Students:
#     print(j.name, j.score, j.check())



#######################################
# # task 8
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5
# Students = []
# n = int(input("heden suragch: "))
# for i in range(n):
#     name = input("ner: ")
#     score = int(input("score: "))
#     Students.append(Student(name, score))
# for k in suragch:
#     if k.score < 60:
#         k.add_score()
#     print(k.ner, k.score)
# # task 9
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def birthday(self):
#         self.age += 1
# name = input("ner: ")
# age = int(input("nas: "))
# student1 = Student(name, age)
# n = int(input("nemeh too: "))
# for i in range(n):
#     student1.birthday()
# print(student1.age)
# # task 10
# class Student:
#     def __init__(self, score):
#         self.score = score
#     def get_grade(self):
#         if self.score > 100 or self.score < 0:
#             return "baij bolomgui dun"
#         elif self.score >= 90:
#             return "A"
#         elif self.score >= 80:
#             return "B"
#         else:
#             return "C"
# score = int(input("Onoo: "))
# student = Student(score)
# print(student.get_grade())
# # task 11
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.attendance = 0
#     def attend(self):
#         self.attendance += 1
#     def show_attendance(self):
#         print(self.name, "ирц:", self.attendance)
# name = input("Нэр: ")
# student = Student(name)
# n = int(input("Хэдэн удаа ирсэн бэ: "))
# for i in range(n):
#     student.attend()
# student.show_attendance()
# # task 12
# class Student:
#     def __init__(self, onoo, irts):
#         self.onoo = onoo
#         self.irts = irts
#     def check(self):
#         if self.onoo >= 60 and self.irts >= 80:
#             return "tentsen"
#         else: 
#             return "tentseegui"
# onoo = int(input("onoo: "))
# irts = int(input("irts: "))
# Student1 = Student(onoo, irts)
# print(Student1.check())
# # task 13
# class Student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores
#     def show_scores(self):
#         print("Onoonuud:", self.scores)
#     def add_score(self, score):
#         self.scores.append(score)
#     def average(self):
#         return sum(self.scores) / len(self.scores)
# name = input("Ner: ")
# scores = list(map(int, input("Onoonuud: ").split()))
# student1 = Student(name, scores)
# student1.show_scores()
# new_score = int(input("Shine onoo nem: "))
# student1.add_score(new_score)
# student1.show_scores()
# print("Dundaj onoo:", student1.average())
# # task 14
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def show_info(self):
#         print("Ner:", self.name)
#         print("Nas:", self.age)
#         print("Angi:", self.grade)
#     def change_name(self, new_name):
#         self.name = new_name
#     def change_grade(self, new_grade):
#         self.grade = new_grade
# name = input("Ner: ")
# age = int(input("Nas: "))
# grade = input("Angi: ")
# s = Student(name, age, grade)
# new_name = input("Shine ner: ")
# new_grade = input("Shine angi: ")
# s.change_name(new_name)
# s.change_grade(new_grade)
# s.show_info()
# # task 15
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#         self.scores = []
#     def show_info(self):
#         print("Ner:", self.name)
#         print("Angi:", self.grade)
#         print("Onoonuud:", self.scores)
#     def add_score(self, score):
#         self.scores.append(score)
#     def average(self):
#         if len(self.scores) == 0:
#             return 0
#         return sum(self.scores) / len(self.scores)
#     def check_result(self):
#         if len(self.scores) == 0:
#             print("Onoo baihgui")
#         elif self.average() >= 60:
#             print("Tentssen")
#         else:
#             print("Tentseegui")
# name = input("Ner: ")
# grade = input("Angi: ")
# s = Student(name, grade)
# n = int(input("Shalgaltin too: "))
# for i in range(n):
#     score = int(input("Onoo: "))
#     s.add_score(score)
# s.show_info()
# print("Dundaj:", s.average())
# s.check_result()
