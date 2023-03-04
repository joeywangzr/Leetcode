# pyramid levels
n = 80
maximum = 2*(n-1) + 1

for i in range(n):
    length = 2*(i-1) + 1
    difference = (maximum - length)//2
    print(" "*difference + "*"*length)
