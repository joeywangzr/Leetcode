target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

# for i in range(len(position)):
#     pair = (position[i], speed[i])
#     stack.append(pair)

# stack.sort(reverse=True)
pair = [(p,s) for p,s in zip(position, speed)]
pair.sort(reverse=True) # O(nlogn)
stack = []
for p,s in pair:
    stack.append((target-p)/s)
    if len(stack) >= 2 and stack[-1] <= stack[-2]: # if just one element then there is only one car
        stack.pop()
    print(len(stack))
