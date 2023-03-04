import re
s = "race a car"

s = re.sub('[\W_]+', '', s).lower()

for i in range(len(s)-1):
    if s[i] != s[len(s)-1-i]:
        print(False)
        break
print(True)