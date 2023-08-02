res = []
def backtrack(start, sol):
    if len(sol) == k:
        res.append(sol.copy())
        return
    for i in range(start, n+1):
        sol.append(i)
        backtrack(i+1,sol)
        sol.pop()

backtrack(1,[])
print(res)