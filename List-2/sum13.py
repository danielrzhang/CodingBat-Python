def sum13(nums):
    if len(nums) == 0:
        return 0
    
    else:
        counter = 0
        
        if (nums[0] != 13):
            counter = nums[0]
            
        for i in range(1, len(nums)):
            if nums[i] != 13 and nums[i - 1] != 13:
                counter += nums[i]
                
                
        return counter
                