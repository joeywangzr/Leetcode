nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0]
nums = [1,-1,-1,0]
nums = [-2,0,0,2,2]

sol = []
nums.sort()
for i in range(len(nums)):
    if (nums[i] == nums[i-1]) and (i>0):
        continue
    else:
        l = i+1
        r = len(nums)-1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            
            if sum == 0:
                if [nums[i],nums[l],nums[r]] in sol:
                    continue
                else:
                    sol.append([nums[i],nums[l],nums[r]])
                r -= 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
            elif sum < 0:
                l += 1
            elif sum > 0:
                r -= 1

print(sol)