strs = ["eat","tea","tan","ate","nat","bat"]

solution = {}
for string in strs:
    anagram_dict = {}
    for i in string:
        anagram_dict[i] = anagram_dict.get(i,0) + 1
    solution[tuple(anagram_dict)] = solution.get(tuple(anagram_dict), []).append(string)
    print(tuple(anagram_dict))
print(solution.values())