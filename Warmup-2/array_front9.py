def array_front9(nums):
    if (len(nums) < 4):
        for i in nums:
            if i == 9:
                return True
            
    else:
        for i in nums[0:4]:
            if i == 9:
                return True
            
    return False   
            
            
            