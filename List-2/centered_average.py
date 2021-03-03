def centered_average(nums):
    nums.sort()
    counter = 0
    for i in range(1, len(nums) - 1):
       counter += nums[i]
       
    return counter / (len(nums) - 2)