t = "ADOBECODEBANC"
s = "ABC"

if t == "":
    print("")

res = [-1,-1]
resLen = float("infinity")
t_map, sliding_window = {}, {}

for i in t:
    t_map[i] = t_map.get(i, 0) + 1

l = 0
have = 0
need = len(t_map)

for r in range(len(s)):
    c = s[r]
    sliding_window[c] = sliding_window.get(c, 0) + 1

    if c in t_map and t_map[c] == sliding_window[c]:
        have += 1
    
    # move left forward
    while have == need:
        if (r-l+1) < resLen:
            res = [l,r]
            resLen = r-l+1
        sliding_window[s[l]] -= 1
        if s[l] in t_map and sliding_window[s[l]] < t_map[s[l]]:
            have -= 1
        l += 1

l, r = res
print(s[l : r + 1] if resLen != float("infinity") else "")
