# def isSubsequencePalindrome(s,start,end):
#     n = end-start+1
#     pal = True
#     if n>1 :
#         r = 0
#         for i in range(start , start + n//2):
#             if  s[i] != s[end - r]:
#                 pal = False
#                 break
#             r += 1
#     if pal:
#         return True 
      
#     return False




def longestPalSubsC(s):
    n = len(s)
    start = 0
    end = 0

    #Thanks to ur Hint ...:

    for center in range(n):
        # We have to take into consideration that it could be odd or even in length (that why i used the variable X)
        for X in [0, 1]:
            left = center
            right = center + X
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            # Checking if it's longer 
            if right - left - 1 > end - start:
                start = left + 1
                end = right - 1

    return s[start:end+1]



print(longestPalSubsC("aceexcivicgrfdds"))
print(longestPalSubsC("civicgrfdds"))
print(longestPalSubsC("aceexcivic"))
print(longestPalSubsC("civic"))
print(longestPalSubsC(""))
print(longestPalSubsC("123abba1"))
print(longestPalSubsC("abba1"))
print(longestPalSubsC("123abba"))
print(longestPalSubsC("12345"))            
    