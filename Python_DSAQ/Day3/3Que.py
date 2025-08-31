def sortedSquares(nums):
    res = [0] * len(nums)
    i, j = 0, len(nums) - 1
    pos = len(nums) - 1
    while i <= j:
        if abs(nums[i]) > abs(nums[j]):
            res[pos] = nums[i] ** 2
            i += 1
        else:
            res[pos] = nums[j] ** 2
            j -= 1
        pos -= 1
    return res
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  
