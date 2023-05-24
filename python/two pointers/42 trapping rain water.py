height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
# height = [4,2,3]
# height = [5,4,1,2]
# height = [0,7,1,4,6]
# height = [9,2,9,3,2,2,1,4,8]
# height = [2,8,5,5,6,1,7,4,5]
# height = [5,3,7,7]
# height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]

if len(height) < 3:
    print(0)

# brute force solution
collected = 0

l = 0

# get to the first l you can start at
while height[l] == 0 or height[l+1] >= height[l]:
    l += 1
    if l >= len(height) - 2:
        break

while l < len(height) - 2:

    # find r
    # two cases: 1) there is r greater than l, 2) if not, r less than l
        # if r greater than l:
        # take first greatest height
        # for each of the heights, keep adding 1 if next is greater or equal until it goes lower

        # if r less than l (no r greater):
        # get the greatest height after l and set that as r

    r = l+2
    found = False
    for i in range(r, len(height)):
        if height[i] >= height[l]:
            r = i
            found = True
            if r >= len(height)-1:
                break
            while height[r+1] >= height[r]:
                r += 1
                if r >= len(height)-1:
                    break
            break
    
    if not found:
        for i in range(r, len(height)):
            if height[i] >= height[r]:
                r = i

    min_height = min(height[l], height[r])
    for j in range(l+1, r+1):
        to_add = min_height - height[j]
        if to_add <= 0:
            continue
        else:
            collected += to_add

    while height[l] == 0 or height[l+1] >= height[l]:
        l += 1
        if l >= len(height) - 2:
            break

    l = r

print(collected)

# better brute force:
# for each element of water, get left max and right max. get the minimum height of both of these max values, and then subtract the minimum by the height at that point.
# if negative or 0, add nothing. otherwise add that number

# dp solution
if len(height) < 3:
    print(0)


max_left = [0]
max_right = [0]
sol = 0

max_left.append(max(height[0], height[1]))
for i in range(2,len(height)):
    max_left.append(max(max_left[i-1], height[i]))

max_right.append(max(height[len(height)-1], height[len(height)-2]))
for i in range(2,len(height)):
    max_right.append(max(max_right[i-1], height[len(height)-i]))
max_right.reverse()

for i in range(1, len(height)):
    minimum = min(max_left[i], max_right[i])
    add = minimum - height[i]
    if add <= 0:
        continue
    else:
        sol += add

print(sol)