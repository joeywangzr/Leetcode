# s1 = "adc"
# s2 = "dcda"
# s1 = "ab"
# s2 = "eidbaooo"
s1 = "a"
s2 = "b"
if len(s2) < len(s1):
    print(False)

dict1 = {}
for a in s1:
    dict1[a] = dict1.get(a,0) + 1

dict2 = {}
# looking for substring same length as s1
l = 0
for b in range(len(s1)):
    dict2[s2[b]] = dict2.get(s2[b],0) + 1

if len(s1) == len(s2):
    print(dict2 == dict1)

while dict1 != dict2:
    dict2[s2[l]] -= 1
    if dict2[s2[l]] == 0:
        dict2.pop(s2[l])
    for c in range(l+len(s1),l+len(s1)+1):
        dict2[s2[c]] = dict2.get(s2[c],0) + 1
    l += 1
    if l+len(s1) >= len(s2):
        break

print(dict2 == dict1)