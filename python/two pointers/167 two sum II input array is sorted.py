numbers = [0,0,3,4]
target = 0

# indexes of both pointers
lpointer = 0
rpointer = len(numbers)-1
sum = -1
while sum != target:
    sum = numbers[rpointer] + numbers[lpointer]
    print(sum)
    if sum > target:
        rpointer -= 1
    elif sum < target:
        lpointer += 1

print([lpointer+1, rpointer+1])