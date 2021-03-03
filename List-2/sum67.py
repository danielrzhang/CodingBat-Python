def sum67(nums):
    
    if len(nums) == 0:
        return 0
    
    counter = 0
    skipNums = False
    
    for i in range(len(nums)):
        if (nums[i] == 6):
            skipNums = True
            
        else:
            if skipNums:
                if nums[i] == 7:
                    skipNums = False
                
            else:
                counter += nums[i]
                
    return counter
                
                
            
        
                
                
            
            