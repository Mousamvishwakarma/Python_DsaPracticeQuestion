pick = 6  

def guess(num):
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1

def guessNumber(n):
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        res = guess(mid)

        if res == 0:
            return mid
        elif res < 0:
            high = mid - 1
        else:
            low = mid + 1

print(guessNumber(10))  
