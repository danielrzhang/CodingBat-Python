def string_splosion(str):
    string = ""
    for i in range(len(str) + 1):
        string += str[:i]

    return string
        
