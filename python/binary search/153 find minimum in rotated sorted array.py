nums = [3,5,1]

res = nums[0]
l = 0
r = len(nums)-1
# if rotated, left is always greater
while l<=r:
    mid = (l+r)//2
    res = min(nums[mid], res)
    if nums[mid] > nums[r]:
        l = mid+1
    else:
        r = mid-1
print(min(nums[mid], res))