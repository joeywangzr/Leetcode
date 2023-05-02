import re
s = "race a car"

s = re.sub('[\W_]+', '', s).lower()

for i in range(-(len(s)//-2)): # ceil division
    if s[i] != s[len(s)-1-i]:
        print(False)

print(True)