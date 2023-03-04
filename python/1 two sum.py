target = 6
nums = [3,2,3]
dict = {}
for i in range(len(nums)):
    difference = target-nums[i]
    if nums[i] in dict.keys():
        print([dict[difference], i])
    dict[difference] = i