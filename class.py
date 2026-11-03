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


#####################################


# # task 1
# class Phone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery
#     def use_phone(self):
#         self.battery -= 10
#         if self.battery < 0:
#             self.battery = 0
#     def charge(self):
#         self.battery += 20
#         if self.battery > 100:
#             self.battery = 100
#     def show_battery(self):
#         print("Tseneg:", str(self.battery) + "%")
# phone1 = Phone("iPhone", 80)
# phone1.use_phone()
# phone1.show_battery()
# phone1.charge()
# phone1.show_battery()
# # task 2
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def sell(self, amount):
#         if amount > self.quantity:
#             print("Baraa hureltsehgui")
#         elif amount > 0:
#             self.quantity -= amount
#     def show_total(self):
#         print("Uldegdel:", self.quantity)
#         print("Niit une:", self.price * self.quantity)
# product1 = Product("Mouse", 30000, 10)
# product1.sell(3)
# product1.show_total()
# # task 3
# class Athlete:
#     def __init__(self, name, points):
#         self.name = name
#         self.points = points
#     def add_points(self, points):
#         self.points += points
#     def lose_points(self, points):
#         self.points -= points
#     def show_points(self):
#         print("Onoo:", self.points)
# athlete1 = Athlete("Bat", 20)
# athlete1.add_points(15)
# athlete1.lose_points(5)
# athlete1.show_points()
# # task 4
# class Movie:
#     def __init__(self, title, rating, views):
#         self.title = title
#         self.rating = rating
#         self.views = views
#     def add_view(self):
#         self.views += 1
#     def update_rating(self, new_rating):
#         self.rating = new_rating
#     def show_info(self):
#         print("Kino:", self.title)
#         print("Unelgee:", self.rating)
#         print("Uzeltiin too:", self.views)
# movie1 = Movie("Avatar", 8.5, 100)
# movie2 = Movie("Titanic", 9.0, 200)
# movie1.add_view()
# movie2.update_rating(9.5)
# movie1.show_info()
# movie2.show_info()
# # task 5
# class GameCharacter:
#     def __init__(self, name, health, damage):
#         self.name = name
#         self.health = health
#         self.damage = damage
#     def attack(self, enemy):
#         enemy.health -= self.damage
#         if enemy.health < 0:
#             enemy.health = 0
#     def show_health(self):
#         print(self.name, "iin ami:", self.health)
# player1 = GameCharacter("Knight", 100, 20)
# player2 = GameCharacter("Goblin", 60, 10)
# player1.attack(player2)
# player2.show_health()
# # task 6
# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def add_money(self, amount):
#         if amount > 0:
#             self.balance += amount
#     def pay(self, amount):
#         if amount > self.balance:
#             print("Mongo hureltsehgui")
#         elif amount > 0:
#             self.balance -= amount
#     def show_balance(self):
#         print("Uldegdel:", self.balance)
# wallet1 = Wallet("Bat", 50000)
# wallet1.add_money(20000)
# wallet1.pay(30000)
# wallet1.show_balance()
# # task 7
# class LibraryBook:
#     def __init__(self, title, available):
#         self.title = title
#         self.available = available
#     def borrow(self):
#         if self.available:
#             self.available = False
#             print("Nomiig zeellee")
#         else:
#             print("Nom ali hediin zeelegdsen baina")
#     def return_book(self):
#         self.available = True
#         print("Nomiig butsaalaa")
# book1 = LibraryBook("Python", True)
# book1.borrow()
# book1.borrow()
# book1.return_book()
# # task 8
# class Exam:
#     def __init__(self, student_name, score, max_score):
#         self.student_name = student_name
#         self.score = score
#         self.max_score = max_score
#     def get_percentage(self):
#         return self.score / self.max_score * 100
#     def check_result(self):
#         percent = self.get_percentage()
#         if percent >= 90:
#             print("Mash sain")
#         elif percent >= 80:
#             print("Sain")
#         elif percent >= 60:
#             print("Tentssen")
#         else:
#             print("Tentseegui")
# exam1 = Exam("Bat", 85, 100)
# exam1.check_result()
# # task 9
# class Employee:
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus
#     def add_bonus(self, amount):
#         self.bonus += amount
#     def get_total_salary(self):
#         print("Niit tsalin:", self.salary + self.bonus)
# employee1 = Employee("Bat", 2000000, 100000)
# employee1.add_bonus(50000)
# employee1.get_total_salary()
# # task 10
# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def increase_quantity(self, amount):
#         if amount > 0:
#             self.quantity += amount
#     def decrease_quantity(self, amount):
#         if amount > 0 and amount <= self.quantity:
#             self.quantity -= amount
#     def get_total_price(self):
#         print(self.name, "Niit une:", self.price * self.quantity)
# item1 = CartItem("Mouse", 30000, 2)
# item2 = CartItem("Keyboard", 50000, 1)
# item3 = CartItem("Monitor", 300000, 1)
# item1.increase_quantity(1)
# item2.decrease_quantity(1)
# item1.get_total_price()
# item2.get_total_price()
# item3.get_total_price()
# # task 11
# class Computer:
#     def __init__(self, brand, ram, storage):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#     def upgrade_ram(self, amount):
#         self.ram += amount
#     def upgrade_storage(self, amount):
#         self.storage += amount
#     def show_info(self):
#         print("Uildverlegch:", self.brand)
#         print("RAM:", self.ram, "GB")
#         print("Bagtaamj:", self.storage, "GB")
# pc1 = Computer("Lenovo", 8, 256)
# pc1.upgrade_ram(8)
# pc1.upgrade_storage(256)
# pc1.show_info()
# # task 12
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#     def add_interest(self):
#         self.balance += self.balance * self.interest_rate / 100
#         print("Huu nemsnii daraah uldegdel:", self.balance)
# account1 = SavingsAccount("Bat", 100000, 10)
# account1.add_interest()
# # task 13
# class Device:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
# class Laptop(Device):
#     def __init__(self, brand, price, ram):
#         super().__init__(brand, price)
#         self.ram = ram
#     def show_info(self):
#         print("Uildverlegch:", self.brand)
#         print("Une:", self.price)
#         print("RAM:", self.ram, "GB")
# laptop1 = Laptop("Apple", 4500000, 16)
# laptop1.show_info()
# # task 14
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
# class Admin(User):
#     def __init__(self, username, email, permission):
#         super().__init__(username, email)
#         self.permission = permission
#     def show_info(self):
#         print("Hereglegch:", self.username)
#         print("Email:", self.email)
#         print("Erh:", self.permission)
# admin1 = Admin("saraa", "saraa@example.com", "Full Access")
# admin1.show_info()
# # task 15
# class Character:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
# class Mage(Character):
#     def __init__(self, name, health, mana):
#         super().__init__(name, health)
#         self.mana = mana
#     def cast_spell(self):
#         if self.mana >= 10:
#             self.mana -= 10
#         else:
#             print("Mana hureltsehgui")
#     def show_info(self):
#         print("Ner:", self.name)
#         print("Ami:", self.health)
#         print("Mana:", self.mana)
# mage1 = Mage("Wizard", 100, 20)
# mage1.cast_spell()
# mage1.show_info()
