def splitArray(nums, k):
    def isValid(mid):
        count = 1
        curr_sum = 0
        for num in nums:
            if curr_sum + num > mid:
                count += 1
                curr_sum = num
            else:
                curr_sum += num
        return count <= k

    low = max(nums)
    high = sum(nums)

    while low < high:
        mid = (low + high) // 2
        if isValid(mid):
            high = mid
        else:
            low = mid + 1

    return low

nums = [7, 2, 5, 10, 8]
k = 2
print(splitArray(nums, k)) 
