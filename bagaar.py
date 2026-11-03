# # task 1.2
# def grades():
#     n = int(input("Suragchdiin too: "))
#     students = {}
#     counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
#     total = 0
#     big = -1
#     small = 101
#     best = ""
#     lowest = ""
#     for i in range(n):
#         name = input("Suragchiin ner: ")
#         score = int(input("Onoo: "))
#         while score < 0 or score > 100:
#             print("Onoo 0-100 hoorond baih yostoi!")
#             score = int(input("Onoo: "))
#         students[name] = score
#         total += score
#         if score > big:
#             big = score
#             best = name
#         if score < small:
#             small = score
#             lowest = name
#     average = total / n
#     above = []
#     print("=== Unelgee ===")
#     for name, score in students.items():
#         if score >= 90:
#             grade = "A"
#         elif score >= 80:
#             grade = "B"
#         elif score >= 70:
#             grade = "C"
#         elif score >= 60:
#             grade = "D"
#         else:
#             grade = "F"
#         counts[grade] += 1
#         print(name + ":", score, "(" + grade + ")")
#         if score > average:
#             above.append(name)
#     print("Dundaj onoo:", format(average, ".2f"))
#     print("Hamgiin ondor:", best, "(", big, ")")
#     print("Hamgiin baga:", lowest, "(", small, ")")
#     print("Dundjaas deesh:", above)
#     print("=== Unelgeenii too ===")
#     for grade, count in counts.items():
#         print(grade + ":", count)
# grades()