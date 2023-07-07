def duplicate(lis):
    uniqueList = []
    duplicateList = []
 
    for i in lis:
        if i not in uniqueList:
            uniqueList.append(i)
        elif i not in duplicateList:
            duplicateList.append(i)
 
    return duplicateList

nums = [4,3,2,7,8,2,3,1]
print(duplicate(nums))