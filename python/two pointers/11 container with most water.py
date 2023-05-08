height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
height = [1,2,3,4,5,25,24,3,4]

# brute force solution
max_area = 0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        max_area = max(max_area, min(height[i], height[j])*(j-i))

# two pointer
l = 0
r = len(height) - 1
max_area = min(height[l],height[r]) * (r-l)

while l < r:
    if height[l] < height[r]:
        l += 1
    elif height[l] > height[r]:
        r -= 1
    else: # same height
        if height[l+1] > height[r-1]:
            l += 1
        else:
            r -= 1
    max_area = max(max_area, min(height[l],height[r]) * (r-l))
print(max_area)