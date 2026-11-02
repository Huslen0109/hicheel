# # task 1
# n = list(map(int, input("Too: ").split()))
# target = int(input("target: "))
# left = 0
# right = len(n) - 1
# while left <= right:
#     mid = (right + left)//2
#     if n[mid] == target:
#         print(mid)
#         break
#     elif n[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# # task 2
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return mid
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "-1"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 3
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return mid
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "-1"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 4
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return mid
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "-1"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 5
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return mid
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "-1"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 6
# def numbers(nums):
#     count = 0
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         count += 1
#         if nums[mid] == target:
#             return count
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "-1"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 7
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return mid
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "tiim suragch baidgue"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 8
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return "bvrtgeltei baraa"
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "tiim baraa baidgue"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 11
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return mid
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "-1"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 12
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     a = 0
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             a = mid 
#             left = mid + 1 
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return a
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 13
# def number(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return nums
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     nums.insert(left, target)
#     return nums ,mid
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(number(nums))
# # task 14
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return nums[mid-1]
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 15
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return nums[mid+1]
#             break
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#         if nums[mid+1] not in nums:
#             return "baihgui"
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(numbers(nums))
# # task 16
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# numbers = list(map(int, input("Toonuud: ").split(", ")))
# a = int(input("a = "))
# b = int(input("b = "))
# print(binary_search(numbers, a))
# print(binary_search(numbers, b))
# # task 17
# def numbers(nums):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (right + left)//2
#         if nums[mid] == target:
#             return mid
#             break
#         elif nums[mid] > target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "-1"
# nums = list(map(int, input("Toonuud: ").split(", ")))
# target = int(input("target: "))
# print(numbers(nums))
# # task 18
# def numbers(nums, target):
#     for x, i in enumerate(nums): 
#         if i == target:
#             return x
# nums = list(map(int, input("Toonuud: ").split(", ")))
# target = int(input("target: "))
# print(numbers(nums, target))
# # task 19
# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             result = mid
#             right = mid - 1 
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# nums = [1, 2, 2, 2, 2, 4, 5, 5, 7, 8]
# target = int(input("target: "))
# print(binary_search(nums, target))

# # task 20.1

# def numbers(nums):
#     l = 0
#     r = len(nums) - 1
#     count = 0
#     while l <= r:
#         mid = (l + r)//2
#         count += 1
#         if nums[mid] == target:
#             return count, mid
#         elif nums[mid] < target :
#             l = mid + 1
#         else:
#             r = mid - 1
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("find: "))
# print(numbers(nums))              # 3n udaa shalgasan 

# # task 20.2

# def numbers(nums, target):
#     count = 0
#     for x, i in enumerate(nums):
#         count += 1
#         if i == target:
#             return x, count
# nums = list(map(int, input("Toonuud: ").split()))
# target = int(input("find: "))
# print(numbers(nums, target))

# import time
# start = time.perf_counter()
# n = [6, 3, 7, 2, 8, 1]
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j + 1]:
#             ih = n[j]
#             n[j] = n[j+1]
#             n[j+1] = ih
# print(n)
# end = time.perf_counter()
# print(f"{(end - start) * 1000:.2f} ms")