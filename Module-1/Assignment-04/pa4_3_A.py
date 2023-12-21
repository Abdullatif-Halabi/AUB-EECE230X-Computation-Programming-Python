def longestPalSubsA(s):
    n = len(s)
    start = 0
    end = 0
    length = 0
    for i in range(n):
        for j in range(i , n):
            t = s[i : j+1]
            if (t == t[::-1] and length < j+1-i):
                start = i
                end = j+1
                length = j+1-i
    return s[start:end]          


print(longestPalSubsA("aceexcivicgrfdds"))
print(longestPalSubsA("civicgrfdds"))
print(longestPalSubsA("aceexcivic"))
print(longestPalSubsA("civic"))
print(longestPalSubsA(""))
print(longestPalSubsA("123abba1"))
print(longestPalSubsA("abba1"))
print(longestPalSubsA("123abba"))
print(longestPalSubsA("12345"))
