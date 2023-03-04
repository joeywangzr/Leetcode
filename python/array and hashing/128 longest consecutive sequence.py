nums = [100,4,200,1,3,2]

numset = set(nums)
longest = 0
for i in numset:
    # start counting from start of a consecutive sequence
    counter = 0
    if ((i-1) not in numset) and (i in numset):
        while (i+counter) in numset:
            counter += 1
    longest = max(longest, counter)

print(longest)