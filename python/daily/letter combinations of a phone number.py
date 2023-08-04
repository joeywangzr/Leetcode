digits = "23"

map = {
    "2": ["a","b","c"],
    "3": ["d","e","f"],
    "4": ["g","h","i"],
    "5": ["j","k","l"],
    "6": ["m","n","o"],
    "7": ["p","q","r","s"],
    "8": ["t","u","v"],
    "9": ["w","x","y","z"]
}

res = []
def backtrack(start, str):
    if len(str) == len(digits):
        res.append(str)
        return

    for i in map[digits[start]]:
        backtrack(start+1, str+i)
if digits:
    backtrack(0,"")
print(res)