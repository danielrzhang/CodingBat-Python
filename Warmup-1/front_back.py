def front_back(str):
    if (len(str) < 2) :
        return str
    else:
        return str[-1] + str[1:-1] + str[0]

print(front_back("code"))
