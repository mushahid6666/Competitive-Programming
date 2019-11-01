def longest_substring_with_k_distinct(str, k):
    letterMap = {}
    i = 0
    letterMap[str[i]] = 1
    j = 0
    longestSubstring = 1
    curSubstringLen = 1
    while i< len(str) and j < len(str) -1:
        if len(letterMap) == k:
            longestSubstring = max(longestSubstring, curSubstringLen)
        j+=1
        if str[j] not in letterMap and len(letterMap) < k:
            letterMap[str[j]] = 1
            curSubstringLen += 1
        elif str[j] not in letterMap and len(letterMap) == k:
            letterMap[str[j]] = 1
            curSubstringLen += 1
            #delete until <=k
            while len(letterMap) >=k and i<j:
                letterMap[str[i]] -=1
                if letterMap[str[i]] == 0:
                    del letterMap[str[i]]
                i+=1
                curSubstringLen -=1
        else:
            letterMap[str[j]] +=1
            curSubstringLen +=1
    return longestSubstring





String="araaci"
K=2
print longest_substring_with_k_distinct(String, K)
String="araaci"
K=1
print longest_substring_with_k_distinct(String, K)
String="cbbebi"
K=3
print longest_substring_with_k_distinct(String, K)
