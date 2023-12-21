def isWordInFile(fileName, word):
    nameHandle = open(fileName , "r")
    s = nameHandle.read()
    nameHandle.close()
    
    return (word in s)


print(isWordInFile("test.txt","Programming"))
print(isWordInFile("test.txt","programming"))
