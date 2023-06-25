def firstUniqueChar(string):
    fnc = ""
    index = 0
    if len(string) == 0:
        print("EMTPY STRING")

    for i in string:
        if string.count(i) == 1:
            fnc += i
            break
        else:
            index += 1
    if index == len(string) - 1:
        return 0
    else:
        return index


string = "skills"
print(firstUniqueChar(string))
