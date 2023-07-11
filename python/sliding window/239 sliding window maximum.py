nums = [7,2,4]
k = 2

# brute force
res = []
window = [nums[i] for i in range(k)]

for i in range(len(nums)-k):
    res.append(max(window))
    window.remove(nums[i])
    window.append(nums[i+k])
res.append(max(window))
print(res)

# deque
# if smaller element exists when adding new, then remove
# if smaller element after, then add
# 1 remove leftmost element
import collections
res = []
q = collections.deque() # stores indices
l,r = 0, 0

while r < len(nums):
    # remove elements from q if smaller
    while q and nums[q[-1]] < nums[r]: # while q is non empty
        q.pop()
    # add new value to q
    q.append(r)
    # remove left value if its outside of the index
    if l > q[0]:
        q.popleft()
    # add max
    if (r+1) >= k:
        res.append(nums[q[0]])
        l += 1
    r += 1

print(res)
