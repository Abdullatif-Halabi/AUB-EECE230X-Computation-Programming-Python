def anagrams(s1,s2):
    D1 = {}
    D2 = {}

    for x in s1:
        if x in D1 : D1[x] +=1
        else : D1[x] = 1 

    for x in s2:
        if x in D2 : D2[x] +=1
        else : D2[x] = 1 

    if D1 == D2 : return True
    else : return False


# print(anagrams("",""))
# print(anagrams("i","i"))
# print(anagrams("is","si"))
# print(anagrams("fun","nfu"))
# print(anagrams("aaabaab","abba"))
# print(anagrams("aaabaab","baabaaa"))
# print(anagrams("EECE230","EECE230"))
# print(anagrams("EECE230","3EE02CE"))
# print(anagrams("EECE230","3EEE02E"))