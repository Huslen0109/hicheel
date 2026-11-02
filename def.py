# def tegsh_niilber(a, b):
#     total = 0
#     for too in range(a, b + 1):
#         if too % 2 == 0:
#             total += too
#     return total
# a = int(input("Эхлэх тоо: "))
# b = int(input("Дуусах тоо: "))
# hariu = tegsh_niilber(a, b)
# print("Тэгш тоонуудын нийлбэр:", hariu)
# # task 1
# def primetr(a, b, c):
#     return a + b +c
# a, b, c = map(int, input("too: ").split())
# print(primetr(a, b, c))
# # task 2
# def total (a, b):
#     return a +b
# a, b = map(int, input("Too:").split())
# print(total(a, b))
# # task 3
# def kwad(a):
#     return a**3, a**2*6
# a = int(input("too: "))
# print(kwad(a))
# # task 4
# def qwer(a, b):
#     return (a + b)*2, a *b
# a, b = map(int, input("Too: ").split())
# print(qwer(a, b))
# # task 5
# def qwert(x):
#     return 3 * x + 5
# x = int(input("Too: "))
# print(qwert(x))
# # task6
# def oloh(x):
#     return 4 * (x**2) - 3 *x +5
# x = int(input("Too: "))
# print(oloh(x))
# # task 7
# def last(x):
#     return x % 10
# x = int(input("TOo: "))
# print(last(x))
# # task 8
# def mid(x):
#     return x // 10 % 10
# x = int(input())
# print(mid(x))
# # task 9
# def multi(x):
#     a = x // 10
#     b = x % 10
#     return a * b
# x = int(input("too: "))
# print(multi(x))
# # task 10
# def asd(x):
#     a = asd % 10
#     b = asd // 100
#     c = asd // 10 % 10
#     return a + b + c
# x = int(input("Too: "))
# print(asd(x))
###################################
# # task 1
# def hello():
#     print("hello pythoin")
# hello()
# # task 2
# def great(name):
#     print(f"hello {name}")
# name = input()
# great(name)
# # task 3
# def cass(name , age):
#     print(f"{name} n {age} nastai")
# name = input("ner: ")
# age = int(input("nas: "))    
# cass(name, age)
# # task 4
# def total(*a):
#     return sum(a)
# a = map(int, input("Too: ").split())
# print(total(*a))
# # task 5
# def square(n):
#     return n * n
# a = square(5)
# print(a)
# # task 6
# def zxc(*n):
#     return max(n)
# n = map(int, input("Too:").split())
# print(zxc(*n))
# # task 7
# def qwer(n):
#     if n % 2 == 0:
#         return " even"
#     else:
#         return "odd"
# n = int(input("Too: "))
# print(qwer(n))
# # task 8
# def check(n):
#     if n > 18:
#         return "adult"
#     else:
#         return " minor"
# n = int(input("Too: "))
# print(check(n))
# # task 9
# def score(n):
#     while True:
#         if n > 100 or n < 0:
#             n = int(input("Agian: "))
#         elif n > 90 and n <= 100:
#             return "A"
#         elif n > 80 and n < 90:
#             return "B"
#         elif n > 70 and n < 80:
#             return "C"    
# n = int(input("Too: "))
# print(score(n))
# # task 10
# def print_numbers(n):
#     for too in range(1, n + 1):
#         print(too, end=" ")
# n = int(input())
# print_numbers(n)
# # task 11
# def numbers(n):
#     total = 0
#     for i in range(1, n +1):
#         total += i
#     print(total)
# n = int(input("Too: "))
# numbers(n)
# # task 12
# def qwer(n):
#     count = 0
#     for i in range (1, n+1):
#         if i % 2 ==0:
#             count += 1
#     print(count)
# n = int(input("Too: "))
# qwer(n)

# # task 13
# def countt(num):
#     if num < 0:
#         num = -num
#     if num == 0:
#         return 1
#     count = 0
#     while num > 0:
#         num //= 10
#         count += 1
#     return count
# num = int(input())
# print(countt(num))
# # task 14
# def qwer(*nums):
#     return max(*nums)
# nums = list(map(int, input("Too: ").split()))
# print(qwer(*n))
# # task 15
# def find_min(nums):
#     smallest = nums[0]
#     for too in nums:
#         if too < smallest:
#             smallest = too
#     return smallest
# nums = list(map(int, input("too: ").split()))
# print(find_min(nums))
# # task 16
# def qwer(n):
#     count = 0
#     for i in n:
#         if i% 2 == 0:
#             count += 1
#         print(count)
# n = list(map(int, input("Too: ").split()))
# qwer(n) 
# # task 17
# def qwer(n):
#     total = 0
#     for i in n:
#         if n == n:
#             total += i
#             print(total)
# n = list(map(int, input("Too: ").split()))
# qwer(n)
# # task 18
# def get_age(student, name):
#     return student[name]
# students = {}
# s = int(input("heden suracgh: "))
# for i in range(s):
#     name = input("suragchiin ner: ")
#     age = int(input("suargchiin nas: "))
#     students[name] = age
# n = input("nasiig n oloh suragchiin ner: ")
# print(get_age(students, n))
# # task 19
# def find_student(students, name):
#     if name in students:
#         return "Found"
#     else:
#         return "Not found"
# students = {}
# n = int(input("heden suragch: "))
# for i in range(n):
#     name = input("names: ")
#     students[name] = True
# name = input("oloh ner: ")
# print(find_student(students, name))
# # task 20                                                                                                
# def average_score(students):
#     scores = students.values()
#     avrg = sum(scores) // len(scores)
#     return avrg
# students = {}
# n = int(input("Хэдэн сурагч: "))
# for i in range(n):
#     name = input("Нэр: ")
#     score = int(input("Оноо: "))
#     students[name] = score
# print(average_score(students))
# # task 21
# def unique_count(nums):
#     b = set(nums)
#     return len(b)
# nums = list(map(int, input("Too: ").split()))
# print(unique_count(nums))
# # task 22
# def uni_num(nums):
#     return set(nums)
# nums = map(int, input("Too: ").split())
# print(uni_num(nums))
# # task 23
# def greet(name="Guest"):
#     print("hello ",  name)
# n = input()
# greet(n)
# greet()
# task 24
# # task 25
# def discount(price, percent=10):
#     if percent > 0:
#         return price - (price * percent / 100)
# print(discount(10000))     
# print(discount(10000, 20)) 
# # task 26
# def sum_all(*args):
#     return sum(args)
# n = map(int, input("Too: ").split())
# print(sum_all(*n))
# # task 27
# def find_max(*args):
#     return max(*args)
# n = map(int, input("too: ").split())
# print(find_max(n))
# # task 28
# def even(*n):
#     count = 0
#     for i in n:
#         if i % 2 == 0:
#             count += 1
#     return count
# n = map(int, input("Too: ").split())
# print(even(*n))
# # task 29
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
# name = input("Нэр: ")
# age = int(input("Нас: "))
# city = input("Хот: ")
# print(show_info(name=name, age=age, city=city))
# # task 30
# def calculate_total(**prices):
#     total = 0
#     for key, val in prices.items():
#         total += val
#     return total
# n = int(input("Хэдэн жимс: "))
# prices = {}
# for i in range(n):
#     jims = input("Жимс: ")
#     une = int(input("Үнэ: "))
#     prices[jims] = une
# print(calculate_total(**prices))
# # task 31
# def qwer(nums):
#     total = 0
#     count = 0
#     n = max(nums)
#     b = min(nums)
#     c = sum(nums)
#     for i in nums:
#         if i % 2 == 0:
#             total += 1
#         else:
#             count += 1
#     return {
#         "max": n,
#         "min": b,
#         "sum": c,
#         "even": total,
#         "odd": count
#     }
# nums = list(map(int, input("Too: ").split()))
# print(qwer(nums))
# # task 32
# def avrg(students, name):
#     scores = students[name]
#     avr = sum(scores) / len(scores)
#     return avr
# students = {}
# n = int(input("heden suragch: "))
# for i in range(n):
#     ner = input("ner: ")
#     scores = list(map(int, input("dun: ").split()))
#     students[ner] = scores
# m = input("dundaj oloh huuhdiin ner: ")
# print(avrg(students, m))
# # task 33
# def max_score(students):
#     scores = students[name]
#     maxscore = max(scores)
#     return maxscore
# students = {}
# n = int(input("heden suragch: "))
# for i in range(n):
#     ner = input("ner: ")
#     scores = list(map(int, input("dun: ").split()))
#     students[ner] = scores
# print(max_score(students))
# # task 34
# def calculate(*args, **kwargs):
#     bonus = kwargs["bonus"]
#     tax = kwargs["tax"]
#     total = sum(args)
#     return total + bonus - tax
# a = list(map(int, input("Too :").split()))
# kwargs = {}
# bonus = int(input("Bonus ni :"))
# tax = int(input("Tax ni :"))
# kwargs.update({"bonus" : bonus,
# "tax" : tax
# })
# print(calculate(*a, **kwargs))
# def x(ner, score):
#     for ner, score in ner:
#         if ner == find:
#             return score
#     return "tiim hvvhd bhu"
# xs= []
# n = int(input("heden udaa: "))
# for i in range(n):
#     ner = input("ner: ")
#     score = int(input("onoo: "))
#     xs.append([ner, score])
# find = input("haih ner: ")
# print(x(xs, find))