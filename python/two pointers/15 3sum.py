# nums = [-1,0,1,2,-1,-4]
nums = [0,0,0]
solution = []

nums.sort()

for i in range(len(nums)):
    if (nums[i] == nums[i-1]) and (i>0):
        continue
    else:
        # do two sum        
        l = i+1
        r = len(nums)-1
        while l<r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                solution.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums [l-1] and l<r:
                    l += 1
            elif sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            

print(solution)