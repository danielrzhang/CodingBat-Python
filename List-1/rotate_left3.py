def rotate_left3(nums):
    num = nums.pop(0)
    nums.append(num)
    return nums