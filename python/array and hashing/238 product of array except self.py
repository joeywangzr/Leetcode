nums = [1,2,3,4]

ans = [1]*len(nums)

# prefixes
prefix = 1
for i in range(len(ans)):
    ans[i] = prefix
    prefix *= nums[i]

# suffixes
suffix = 1
for j in range(len(ans)-1, -1, -1):
    ans[j] *= suffix
    suffix *= nums[j]

print(ans)