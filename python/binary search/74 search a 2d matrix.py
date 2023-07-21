matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix = [[1,3]]
target = 3

l = 0
r = len(matrix) - 1
mid = l+(r-l)//2

if r != l:
    while True:
        mid = l+(r-l)//2
        mid_row = matrix[mid]
        if l > r:
            print(False)
        elif target < mid_row[0]:
            r = mid - 1
        elif target > mid_row[-1]:
            l = mid + 1
        else:
            break

l = 0
r = len(matrix[mid]) - 1
row = matrix[mid]
while l <= r:
    mid = l+(r-l)//2
    if target < row[mid]:
        r = mid - 1
    elif target > row[mid]:
        l = mid + 1
    else:
        print(True)