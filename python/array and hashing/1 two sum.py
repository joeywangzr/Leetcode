target = 7
nums = [3,2,4,10,20]
dict = {}

for i in range(len(nums)):
    diff = target - nums[i]
    
    if nums[i] in dict.keys():
        print([i, dict[nums[i]]])

    dict[diff] = i