# use a bucket search approach
nums = [1, 1, 1, 2, 2, 3]
k = 2

hashmap = {}
solution = [[] for i in range(len(nums))]
for i in nums:
    hashmap[i] = hashmap.get(i, 0) + 1

for i in hashmap.items():
    solution[i[1]].append(i[0])

answer = []
for i in range(len(solution)-1, 0, -1):
    for j in solution[i]:
        if len(answer) == k:
            print(answer)
        answer.append(j)
print(answer)