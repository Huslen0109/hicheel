# ###################################
# m = [[1,2,3], [4,5,6],[7,8,9]]
# for i in range(0, len(m)):
#     for o in m[i]:
#         print(o, end = " ")
# # task 1
# n = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# b = n[1][2]
# print(b)
# # task2
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# b = students[2][0]
# print(b)
# # task3
# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# b = nums[1]
# print(b)
# # task4
# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# c = nums[2][0]
# print(c)
# # task5
# nums = [
#     [5, 10],
#     [15, 20]
# ]
# b = nums[0][0]
# print(b)
# # atask 6
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# n = nums[-1][-1]
# print(n)
# # task7
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for i in nums:
#     for j in i:
#         print(j, end = "")
# # task8
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in nums:
#     for j in i:
#         print(j, end="")
# # task 9
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in nums:
#     for j in i:
#         print(j, end=" ")
# # task 10
# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]
# for i in nums:
#     for j in i:
#         if j > 10:
#             print(j)
# # task 11
# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]
# count = 0
# for i in nums:
#     for j in i:
#         count += 1
# print(count)
# # task 12
# n = int(input("heden list: "))
# nums = []
# for i in range(n):
#     row = list(map(int, input("too: ").split()))
#     nums.append(row)
# total = 0
# for row in nums:
#     for x in row:
#         total += sum(x)
# print(total2)
# # task 13
# n= int(input("heden llist: "))
# m = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     m.append(too)
#     for j in m:
#         for q in j:
#             if q % 2 == 0:
#                 print(q)
# # task 14
# n = int(input("heden list: "))
# nums = []
# for i in range(n):
#     too = list(map(int, input("Too:" ).split()))
#     nums.append(too)
#     for j in nums:
#         for q in j:
#             if q % 2 != 0:
#                 print(q)
# # task 15
# n= int(input("heden llist: "))
# m = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     m.append(too)
#     total = 0
#     for j in m:
#         for q in j:
#             if q % 2 == 0:
#                 total += q
# print(total)
# # task 16
# n= int(input("heden llist: "))
# m = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     m.append(too)
#     for j in m:
#          for q in j:
#             if q > 0:
#                 print(q)
# # task 17
# n = int(input("heden list: "))
# nums = []
# for i in range(n):
#     too = list(map(int, input("Too:" ).split()))
#     nums.append(too)
#     total = 0
#     for j in nums:
#         for q in j:
#             if q > 0:
#                 total += q
# print(total)
# # task 18
# n = int(input("heden list: "))
# nums = []
# maxtoo = 0
# for i in range(n):
#     too = list(map(int, input("Too:" ).split()))
#     nums.append(too)
#     for j in nums:
#         for q in j:
#             if maxtoo < q:
#                 maxtoo = q
# print(maxtoo)
# # task 19
# n = int(input("heden list: "))
# nums = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     nums.append(too)
# mintoo = min(nums[0])
# for j in nums:
#     if min(j) < mintoo:
#         mintoo = min(j)
# print(mintoo)
# # task 20
# n = int(input("heden list: "))
# nums = []
# totall = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     nums.append(too)
#     total = 0
#     for j in nums:
#         a = sum(j)
#         print(a)   
# # task 21
# n = int(input("heden list: "))
# nums = []
# maxtoo = 0
# for i in range(n):
#     too = list(map(int, input("Too:" ).split()))
#     nums.append(too)
#     for j in nums:
#         for q in j:
#             if maxtoo < q:
#                 maxtoo = q
#         print(maxtoo)
# # task 22
# n = int(input("heden list: "))
# nums = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     nums.append(too)
# for j in nums:
#     print(min(j))
# # task 23
# n = int(input("heden list: "))
# b = int(input("oloh too: "))
# nums = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     nums.append(too)
#     for j in nums:
#         for k in j:
#             if b == k:
#                 print("yes")
#             else:
#                 print("No")
# # task 24
# n = int(input("heden list: "))
# b = int(input("oloh too: "))
# count = 0
# nums = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     nums.append(too)
#     for j in nums:
#         for k in j:
#             if k == b:
#                 count += 1
#                 print(count)
# # task 25
# n = int(input("heden list: "))
# b = int(input("jisjih too: "))
# total = 0
# nums = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     nums.append(too)
# for j in nums:
#     for k in j:
#         if k > b:
#             total += k
#             print(total)
# # task 26
# n = int(input("heden list: "))
# nums = []
# sums = []
# for i in range(n):
#     too = list(map(int, input("Too: ").split()))
#     nums.append(too)
# for j in nums:
#         a = sum(j)
#         sums.append(a)
# ih = max(sums)
# index = sums.index(ih)
# print(nums[index])
# # task 27
# n = int(input("heden list: "))
# nums = []
# for i in range(n):
#     ners = list(input("Too: ").split())
#     nums.append(ners)
# for i in nums:
#     print(i[0], i[1])
# # task 28
# n = int(input("heden list: "))
# nums = []
# for i in range(n):
#     ners = list(input("Too: ").split())
#     nums.append(ners)
#     for j in nums:
#         if int(j[1]) > 18:
#             print(j[0])
# # task 29
# n = int(input("heden suragch: "))
# students = []
# for i in range(n):
#     data = input("Ner onoo: ").split()
#     students.append(data)
# for student in students:
#     name = student[0]
#     total = 0
#     for j in range(1, len(student)):
#         total += int(student[j])
#     avg = total / (len(student) - 1)
#     print(name, a)
# # task 30
# n = int(input("heden suragch: "))
# nums = []
# for i in range(n):
#     data = input("Ner onoo: ").split()
#     nums.append(data)
# max_avg = 0
# max_name = ""
# for j in nums:
#     name = j[0]
#     total = 0
#     for k in range(1, len(j)):
#         total += int(j[k])
#     avg = total / (len(j) - 1)
#     if avg > max_avg:
#         max_avg = avg
#         max_name = name
# print(max_name, round(max_avg, 2))