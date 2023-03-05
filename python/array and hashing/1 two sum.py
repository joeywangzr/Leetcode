target = 7
nums = [3,2,4,10,20]

# solution 1: map of diff to index  
dict = {}
for i in range(len(nums)):
    if nums[i] in dict.keys():
        print([i, dict[nums[i]]])
        break

    dict[target-nums[i]] = i

# solution 2: map of value to index
dict = {}
for i, n in enumerate(nums):
    diff = target - n
    if diff in dict.keys():
        print([i, dict[diff]])
        break
    
    dict[n] = i