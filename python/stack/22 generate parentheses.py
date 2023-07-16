n = 3
# ["((()))","(()())","(())()","()(())","()()()"]

# sol 1 with string
res = []

def brackets_string(open_count, closed_count, string):
    if open_count == closed_count == n:
        res.append(string)
        return
    if open_count < n:
        string += "("
        brackets_string(open_count + 1, closed_count, string)
        string = string[:-1]
    if closed_count < open_count:
        string += ")"
        brackets_string(open_count, closed_count + 1, string)
        string = string[:-1]

brackets_string(1,0,"(")
print(res)

# sol 2 with stack
res = []
stack = []

def brackets_stack(open_count, closed_count):
    if open_count == closed_count == n:
        res.append("".join(stack))
        # if just append stack then it will make empty list because it is based on the original stack, needs to be a copy
        return
    if open_count < n:
        stack.append("(")
        brackets_stack(open_count + 1, closed_count)
        stack.pop()
    if closed_count < open_count:
        stack.append(")")
        brackets_stack(open_count, closed_count + 1)
        stack.pop()

brackets_stack(0,0)
print(res)