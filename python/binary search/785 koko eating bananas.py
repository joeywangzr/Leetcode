# yo what are these guards doing leaving koko unguarded for 823855818 hours?! that's negligence
# - codewhisperer_ on leetcode

piles = [30,11,23,4,20]
h = 6

import math

l = 1
r = max(piles)
res = r

while l <= r:
    mid = (l+r)//2
    hours = 0
    for i in piles:
        hours += math.ceil(i/mid)
    if hours <= h:
        res = min(res,mid)
        r = mid-1
    elif hours > h:
        l = mid+1

print(res)