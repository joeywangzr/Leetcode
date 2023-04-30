import collections

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

row = collections.defaultdict(set)
column = collections.defaultdict(set)
box = collections.defaultdict(set)

for i in range(9):
    for j in range(9):
        value = board[i][j]
        if value == ".":
            continue
        if ((value in row[i]) or (value in column[j]) or (value in box[(i//3,j//3)])):
            print(False)
        
        row[i].add(value)
        column[j].add(value)
        box[(i//3,j//3)].add(value)

print(True)
        