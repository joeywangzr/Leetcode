# s = "ABAB"
# k = 2
s = "AABABBA"
k = 1

# brute force: look at every individual substring
# non brute force:
res = 0
for i in set(s):
    hashmap = {}
    l = 0
    for r in range(len(s)):
        while hashmap.get("not", 0) >= k and s[r] != i:
            if s[l] != i:
                hashmap["not"] = hashmap.get("not", 0) - 1
            else:
                hashmap[i] =  hashmap.get(i, 0) - 1

            l += 1
            
        if s[r] == i:
            hashmap[i] = hashmap.get(i, 0) + 1
        else:
            hashmap["not"] = hashmap.get("not", 0) + 1
        
        res = max(res, r-l+1)
print(res)

# neetcode ref
count = {}
res = 0
l = 0
for r in range(len(s)):
    count[s[r]] = count.get(s[r], 0) + 1
    # make sure window is valid
    # if too many then increment until its not
    while (r-l+1) - max(count.values()) > k:
        count[s[l]] -= 1
        l += 1
    res = max(res, r - l + 1)
print(res)
# O(26*n)

# better optimized solution
count = {}
res = 0
l = 0
max_frequency = 0
for r in range(len(s)):
    count[s[r]] = count.get(s[r], 0) + 1
    max_frequency = max(max_frequency, count[s[r]])
    # make sure window is valid
    # if too many then increment until its not
    while (r-l+1) - max_frequency > k:
        count[s[l]] -= 1
        l += 1
    res = max(res, r - l + 1)
print(res)
# O(n)