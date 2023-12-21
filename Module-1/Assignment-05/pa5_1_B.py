def wordSearch(fileName , word):
    nameHandle = open(fileName , 'r')
    found = False
    for i , line in enumerate(nameHandle):
        i += 1
        if (word in line):
            found = True
            break
    nameHandle.close()
    if found:
        return i  
    return 0


print(wordSearch("test.txt","Programming"))
print(wordSearch("test.txt","programming"))