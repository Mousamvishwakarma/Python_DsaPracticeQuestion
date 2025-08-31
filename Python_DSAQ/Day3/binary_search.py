def binary(array, target):
    left = 0
    right= len(array) - 1
    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
             return mid
        elif array[mid] < target:
              left = mid + 1
        else:
               right = mid - 1

array = [22, 45, 66, 77, 88, 99]
target = 88
print(binary(array, target))

# def search(nums,target):
#     left =0
#     right = len(nums)-1
#     while left <= right:
#         mid = (left + right) // 2

#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid +1

#         else:
#             right = mid -1

# nums = [22,45,66,77,88,99]
# target = 88
# print(nums,target)