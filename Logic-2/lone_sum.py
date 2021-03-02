def lone_sum(a, b, c):
    if (a == b) and (not b == c) and (not c == a):
        return c
    
    elif (not a == b) and (b == c) and (not c == a):
        return a
    
    elif (not a == b) and (not b == c) and (c == a):
        return b
    
    elif a == b == c:
        return 0
    
    else:
        return a + b + c
        