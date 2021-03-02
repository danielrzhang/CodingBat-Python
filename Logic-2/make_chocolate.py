def make_chocolate(small, big, goal):
    bigRequired = min(big, goal / 5)
    smallRequired = goal - (bigRequired * 5)
    
    if bigRequired <= big and smallRequired <= small:
        return smallRequired
    
    else:
        return -1