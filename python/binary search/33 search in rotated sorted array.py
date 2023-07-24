nums = [4,5,6,7,8,1,2,3]
target = 8

# better sol
l, r = 0, len(nums)-1
while l <= r:
    mid = (l+r)//2
    if target == nums[mid]:
        print(mid)

    if nums[l] <= nums[mid]: # this condition is true if we are in the left sorted portion
        if target > nums[mid] or target < nums[l]: # target not in left
            l = mid + 1
        else: # in left
            r = mid - 1
    else: # right sorted portion
        if target < nums[mid] or target > nums[r]: # target not in right
            r = mid - 1
        else:
            l = mid + 1

# my shitty sol
# l, r = 0, len(nums)-1
# minimum = (nums[0],0)
# # find min
# while l <= r:
#     mid = (l+r)//2
#     if nums[mid] < minimum[0]:
#         minimum = (nums[mid], mid)
#     if nums[mid] > nums[r]:
#         l = mid + 1
#     else:
#         r = mid - 1
# if nums[mid] < minimum[0]:
#     minimum = (nums[mid], mid)

# if target > nums[len(nums)-1]:
#     l = 0
#     r = minimum[1]-1
# else:
#     l = minimum[1]
#     r = len(nums)-1

# while l <= r:
#     mid = (l+r)//2
#     if nums[mid] == target:
#         print(mid)
#     elif target > nums[mid]:
#         l = mid+1
#     else:
#         r = mid-1
# print(-1)