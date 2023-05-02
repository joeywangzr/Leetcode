# gitignore is not working on this so whatever i give up
import re, collections
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

# range is up to but not including

# things to remember

# 1. normalize
s = "string to normalize"
s = re.sub('[\W_]+', '', s).lower()

# 2. default dic
dict = collections.defaultdict(set) # can be set, list, whatever
