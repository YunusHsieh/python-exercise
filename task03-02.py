def num_sum(nums, target):
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
    return []
    

nums = [2,7,11,15]
target = 17


d = num_sum(nums, target)



print(d) # [0,1]
