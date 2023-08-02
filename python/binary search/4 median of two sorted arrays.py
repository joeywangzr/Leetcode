nums1 = [1,3]
nums2 = [2]

# binary search sol
array_1 = nums1
array_2 = nums2
if len(array_1) > len(array_2):
    array_1, array_2 = array_2, array_1 # array_1 should be smallest

total = len(array_1) + len(array_2)
half = total//2

l, r = 0, len(array_1) - 1
while True:
    i = (l+r)//2
    j = half - i - 2

    left_1 = array_1[i] if i >= 0 else float("-infinity")
    right_1 = array_1[i+1] if (i+1) < len(array_1) else float("infinity")

    left_2 = array_2[j] if j >= 0 else float("-infinity")
    right_2 = array_2[j+1] if (j+1) < len(array_2) else float("infinity")

    if left_1 <= right_2 and left_2 <= right_1:
        if total%2: # odd
            print(min(right_1, right_2)) # since its floor
        print((max(left_1,left_2) + min(right_1, right_2))/2)
    
    elif left_1 > right_2:
        r = i-1
    else:
        l = i+1

# divide and conquer sol, not log(m+n)
nums = []
i = j = k = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        nums.append(nums1[i])
        i += 1
        k += 1
    else:
        nums.append(nums2[j])
        j += 1
        k += 1
# leftovers
while i < len(nums1):
    nums.append(nums1[i])
    i += 1
    k += 1
while j < len(nums2):
    nums.append(nums2[j])
    j += 1
    k += 1
mid = (k - 1)//2
# odd
if k%2 == 1:
    print(nums[mid])
# even
else:
    print((nums[mid]+nums[mid+1])/2)