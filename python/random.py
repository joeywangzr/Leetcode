array = [5,9,3]
# print(len(array)) # len is the number of elements in the array, to get index of last do len-1

# for i in range(0,3):
#     print(i) 
#     # range starts from 0 and goes until n-1

# # print all numbers except array
# i = 1 # random index
# print(array[:i] + array[i+1:])

# enumerate
for i, n in enumerate(array):
    print(i, n)