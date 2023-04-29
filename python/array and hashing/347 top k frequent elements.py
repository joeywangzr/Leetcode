# use a bucket search approach
nums = [1,1,1,2,2,3]
# nums = [-1,-1]
k = 2

hashmap = {}
for i in nums:
    hashmap[i] = hashmap.get(i,0) + 1

buckets = [[] for _ in range(len(nums)+1)]

for j in hashmap:
    index = hashmap[j]
    buckets[index].append(j)

ans = []
print(buckets)
for h in range(len(buckets)-1,-1,-1):
    for l in buckets[h]:
        ans.append(l)
        if len(ans) == k:
            print(ans)