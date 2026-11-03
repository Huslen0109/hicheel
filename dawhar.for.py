# # task 1
# n = int(input("niit suragch: "))
# m = int(input("niit shalgalt: "))
# i = 1
# for i in range(n):
#     i += 1
#     total = 0
#     for q in range(m):
#        score = int(input("onoo: "))
#     total += score 
#     dundaj = total  / m
#     print(f"{i}-r suragch")
#     print(f"Niit onoo: {total}")
#     print(f"Dundaj onoo: {dundaj}")
#     if dundaj >= 60:
#         print("Tentssen")
#     else:
#         print("Tentseegui")
# # task 2
# n = int(input("Hunii too: "))
# for i in range(n):
#     total = 0
#     p = int(input("Heden torliin baraa awsan: "))
#     for baraa in range(p):
#         m = int(input("Heden togrognii baraa: "))
#         print(f"shirhegeer toloh dvn: {m}")
#         k = int(input("baraani too hemjee: "))
#         total += m * k
#         print(f"baraanii vne: {total}")  
#     mongo = int(input("Heden togrog ogson: "))
#     hariult = mongo - total
#     print(f"Niit: {total}")
#     if hariult > 0:
#         print(f"hariult: {hariult}")
#     else:
#         print(f"Mongo n dutuu baina: {total - mongo}")
# # task 3
# n = int(input("Ajichidiin too: "))
# for i in range(n):
#     q = 0
#     total = 0
#     for day in range(5):
#         q += 1
#         ajilsantsag = int(input(f"day {q} -Ajilsan tsag: "))  
#         if ajilsantsag == 8:
#             w = ajilsantsag * 5000
#             print(f"neg odriin tsalin: {w}")
#         if ajilsantsag > 8:
#             k = ajilsantsag - 8
#             w = k *7500+40000
#             print(f"iluu tsag {k}: {w}")
#         total+= w
#     print(f"5n odriin niit tsalin: {total}")
# # task 4
# total = 0
# q = 0
# n = int(input("hun:  "))
# for i in range(n):
#     f = int(input("anhnii or: "))
#     b = int(input("heden sar tolson: "))
#     for i in range(b):
#         tololt = int(input("sard tolson mongo: "))
#         total += tololt
#         q += 1
#         print(f"{q}-r sariin daraah vldegdel: {f - total}")
#     print(f"Niit tolson: {total}")
# # task 5
# total = 0
# box = 12
# max = 1
# day = int(input("DAY: "))
# for i in range(day):
#     m = int(input("Odort heden udaa vildwerleh: "))
#     for u in range(m):
#         count = int(input(f"{max}-r uilwerlelteer: "))
#         max += 1
#         total += count
#         buten = total // 12
#         vld = total % 12
#     print(f"1 odort niitde: {total}, buten hairtsag: {buten}, vldegdel: {vld}")
# # task 6
# count = 0
# countt = 0
# amount = 0
# bus = 0
# aylal = 0
# n = int(input("Bus heden udaa aylah: "))
# for i in range(n):
#     aylal += 1
#     m = int(input("Buudliin too: "))
#     for u in range(m):
#         suusan = int(input(f"{bus+1}-r buudald suusan hunii too: "))
#         buusan = int(input(f"{bus+1}-r buudald buusan hunii too: "))
#         bus += 1
#         count += suusan
#         countt += buusan
#         amount = count * 1000
# print(f"{bus}-r buudliin daraa: {count}")
# print(f"{aylal}-r aylald niit suusan: {count}")
# print(f"Aylaliin orlogo: {amount}")
# # task 8
# n = int(input("N = "))
# count = 0
# for i in range(1, n + 1):
#     j = n - i
#     if i <= j and j >= 1:
#         print(i, "+", j, "=", n)
#         count += 1
# print("Niit:", count, "hos")
# # task 9
# n = int(input("N = "))
# count = 0
# for i in range(n // 2000, -1, -1):
#     j = (n - i * 2000) // 1000
#     print("1000:", j, "shirheg, 2000:", i, "shirheg")
#     count += 1
# print("Niit:", count, "huvilbar")
# # task 10
# n = int(input("N = "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         j = n // i
#         if i <= j:
#             print(i, "x", j, "=", n, "ylgavar", j - i)
#             count += 1
# print("Niit:", count, "hos")