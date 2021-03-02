def near_ten(num):
    if ((num + 2) % 10 == 0) or ((num + 1) % 10 == 0) or (num % 10 == 0) or ((num - 1) % 10 == 0) or ((num - 2) % 10 == 0):
        return True
    
    else:
        return False