# s1 = "adc"
# s2 = "dcda"
# s1 = "ab"
# s2 = "eidbaooo"
# s1 = "a"
# s2 = "b"
# if len(s2) < len(s1):
#     print(False)

# dict1 = {}
# for a in s1:
#     dict1[a] = dict1.get(a,0) + 1

# dict2 = {}
# # looking for substring same length as s1
# l = 0
# for b in range(len(s1)):
#     dict2[s2[b]] = dict2.get(s2[b],0) + 1

# if len(s1) == len(s2):
#     print(dict2 == dict1)

# while dict1 != dict2:
#     dict2[s2[l]] -= 1
#     if dict2[s2[l]] == 0:
#         dict2.pop(s2[l])
#     for c in range(l+len(s1),l+len(s1)+1):
#         dict2[s2[c]] = dict2.get(s2[c],0) + 1
#     l += 1
#     if l+len(s1) >= len(s2):
#         break

# print(dict2 == dict1)

# better neetcode sol
s1 = "adc"
s2 = "dcda"

if len(s2) < len(s1):
    print(False)

s1_count = [0]*26
s2_count = [0]*26

for i in range(len(s1)):
    s1_count[ord(s1[i]) - ord("a")] += 1
    s2_count[ord(s2[i]) - ord("a")] += 1

matching = 0

for i in range(26):
    matching += 1 if s1_count[i] == s2_count[i] else 0

l = 0
for r in range(len(s1), len(s2)):
    if matching == 26:
        print(True)
    
    index = ord(s2[r]) - ord("a")
    s2_count[index] += 1
    if s1_count[index] == s2_count[index]:
        matching += 1
    elif s1_count[index] + 1 == s2_count[index]:
        matching -= 1

    index = ord(s2[l]) - ord("a")
    s2_count[index] -= 1
    if s1_count[index] == s2_count[index]:
        matching += 1
    elif s1_count[index] - 1 == s2_count[index]:
        matching -= 1
    l += 1

print(matching == 26)