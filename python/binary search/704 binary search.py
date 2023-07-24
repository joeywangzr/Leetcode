# sorted in ascending order
nums = [-1,0,3,5,9,12]
target = 3

l = 0
r = len(nums)-1

while l <= r:
    mid = (l+r)//2
    if target > nums[mid]:
        l = mid + 1
    elif target < nums[mid]:
        r = mid - 1
    else:
        print(mid)
print(-1)