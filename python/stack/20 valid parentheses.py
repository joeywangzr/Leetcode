s = "]"

stack = []
pairs = {")":"(", "]":"[", "}":"{"}

for i in s:
    if i not in pairs:
        stack.append(i)
        continue
    else:
        if not stack or stack[-1] != pairs[i]:
            print(False)
    stack.pop()
print(not stack)