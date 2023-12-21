def duplicateLines(fileName):
    assert fileName[-4:] == '.txt' , "The file should be of type .txt "
    newFile = fileName[:-4]+'Duplicated'+fileName[-4:]
    nameHandle = open(fileName , 'r')
    nameHandle2 = open(newFile , 'w')

    lst = []
    for line in nameHandle:
        lst.append(line) 

    for i , line in enumerate(lst):
        if i < len(lst)-1:
            nameHandle2.write(2*line)
        else:
            nameHandle2.write(line+'\n'+line)    

    nameHandle.close()
    nameHandle2.close()

# duplicateLines("test.txt")
# duplicateLines("idk.ipynb")