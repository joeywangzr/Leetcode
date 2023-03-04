import collections

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

rows = collections.defaultdict(set)
columns = collections.defaultdict(set)
box = collections.defaultdict(set)

for r in range(9):
    for c in range(9):
        value = board[r][c]
        if (value != ".") and ((value in rows[r]) or (value in columns[c]) or (value in box[(r // 3, c // 3)])):
            print(False)
        rows[r].add(value)
        columns[c].add(value)
        box[(r // 3, c // 3)].add(value)
print(rows)
print(True)