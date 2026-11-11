# # task 1
# a, b = map(int, input().split())
# n = int(input("Suudal: "))
# row = (n - 1) // b + 1
# seat = (n - 1) % b + 1
# print(row, seat)
# # task 2
# a, b = map(int, input().split())
# n = int(input("Havtas: "))
# cabinet = (n - 1) // b + 1
# folder = (n - 1) % b + 1
# print(cabinet, folder)
# # task 3
# a, b = map(int, input().split())
# n = int(input("Suragch: "))
# group = (n - 1) // b + 1
# student = (n - 1) % b + 1
# print(group, student)
# # task 4
# a, b = map(int, input().split())
# n = int(input("Mashinii bair: "))
# floor = (n - 1) // b + 1
# place = (n - 1) % b + 1
# print(floor, place)
# # task 5
# a, b, c = map(int, input().split())
# n = int(input("Suudal: "))
# sector = (n - 1) // (b * c) + 1
# row = ((n - 1) % (b * c)) // c + 1
# seat = (n - 1) % c + 1
# print(sector, row, seat)