def cat_dog(str):
    catCounter = 0
    dogCounter = 0
    
    for i in range(len(str) - 2):
        if str[i:i + 3] == "cat":
            catCounter += 1
            
        elif str[i:i + 3] == "dog":
            dogCounter += 1
            
    if (catCounter == dogCounter):
        return True
    
    else:
        return False