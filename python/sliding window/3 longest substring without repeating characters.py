s = "abcabcbb"
letters = set()
left = 0
longest = 0
for right in range(len(s)):
    while s[right] in letters:
        # move left forward until its unique
        letters.remove(s[left])
        left += 1
    letters.add(s[right])
    longest = max(longest, right-left+1)
print(longest)