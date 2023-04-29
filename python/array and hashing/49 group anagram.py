import collections
strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
# strs = ["eat","tea","tan","ate","nat","bat"]

solution = collections.defaultdict(list)
for i in strs:
    key = [0]*26
    for letter in i:
        key[ord(letter)-ord("a")] += 1

    solution[tuple(key)].append(i)

print(solution.values())