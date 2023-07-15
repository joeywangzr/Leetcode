tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 9

stack = []
op = {'+': lambda x, y: x+y,
      '-': lambda x, y: x-y,
      '*': lambda x, y: x*y,
      '/': lambda x, y: x/y}

for i in tokens:
    if i in op:
        r_val = int(stack.pop(-1))
        l_val = int(stack.pop(-1))
        val = op[i](l_val,r_val)
        stack.append(int(val))
    else:
        stack.append(i)
print(stack[0])