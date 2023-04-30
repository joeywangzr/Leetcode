nums = [100,4,200,1,3,2]

numset = set(nums)
maximum = 0

for i in numset:
    temp = 0
    if i-1 not in numset: # it is the beginning of a new sequence
        number = i
        while number + temp in numset:
            temp += 1
    maximum = max(maximum, temp)

print(maximum)