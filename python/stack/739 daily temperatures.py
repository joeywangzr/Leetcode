temperatures = [73,74,75,71,69,72,76,73]
# [1,1,4,2,1,1,0,0]

res = [0] * len(temperatures)
stack = []

for i, v in enumerate(temperatures):
    while stack and v > stack[-1][0]:
        stack_value, stack_index = stack.pop()
        res[stack_index] = i - stack_index
    stack.append((v, i))
print(res)