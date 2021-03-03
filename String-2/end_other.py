def end_other(a, b):
    if a.lower().endswith(b.lower()) or b.lower().endswith(a.lower()):
        return True
    
    else:
        return False
    