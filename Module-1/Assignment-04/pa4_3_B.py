def isSubsequencePalindrome(s,start,end):
    n = end-start+1
    pal = True
    if n>1 :
        r = 0
        for i in range(start , start + n//2):
            if  s[i] != s[end - r]:
                pal = False
                break
            r += 1
    if pal:
        return True 
      
    return False


def longestPalSubsB(s):
    n = len(s)
    start = 0
    end = 0
    length = 0
    for i in range(n):
        for j in range(i , n):
            if ( isSubsequencePalindrome(s , i , j) and length < j -i +1 ):
                start = i
                end = j+1
                length = j+1-i
    return s[start:end]          


print(longestPalSubsB("aceexcivicgrfdds"))
print(longestPalSubsB("civicgrfdds"))
print(longestPalSubsB("aceexcivic"))
print(longestPalSubsB("civic"))
print(longestPalSubsB(""))
print(longestPalSubsB("123abba1"))
print(longestPalSubsB("abba1"))
print(longestPalSubsB("123abba"))
print(longestPalSubsB("12345"))