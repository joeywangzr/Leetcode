from typing import List

nums = [1,2,3]

# memory inefficient
res = []
def permutations(a, vals):
    if len(a) == len(nums):
        res.append(a.copy())

    for i in range(len(vals)):
        a.append(vals[i])
        vals_copy = vals.copy()
        vals_copy.pop(i)
        permutations(a, vals_copy)
        a.pop()

permutations([], nums)
print(res)

# neetcode comment guy
res = []
def permutations(i):
    if i == len(nums):
        res.append(nums[:])
    for j in range(i,len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        permutations(i+1)
        nums[i], nums[j] = nums[j], nums[i]
        
permutations(0)
print(res)

# neetcode sol
def permute(nums:List[int]) -> List[List[int]]:
    result = []
    if (len(nums) == 1):
        return [nums.copy()]
    
    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)

    return result

print(permute([1,2,3]))