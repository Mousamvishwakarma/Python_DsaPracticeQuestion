def linear(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
array = [22,55,66,77,88,99]
target = 66
print(linear(array, target) )