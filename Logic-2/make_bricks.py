def make_bricks(small, big, goal):
    bigRequired = min(big, goal / 5)
    smallRequired = goal - (bigRequired * 5)
    
    if (bigRequired <= big) and (smallRequired <= small):
        return True
    
    else:
        return False