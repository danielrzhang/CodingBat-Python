def last2(str):
    findString = str[len(str) - 2: len(str)]
    counter = 0
    for i in range(len(str) - 2):
        if (str[i:i + 2] == findString):
            counter += 1

    return counter
            
