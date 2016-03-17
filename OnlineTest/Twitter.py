__author__ = 'mushahidalam'


# Complete the function below.


def firstRepeatingLetter(s):
    hasttable = dict()
    for i in range(0, len(s)):
        if s[i] in hasttable:
            hasttable[s[i]] += 1
        else:
            hasttable[s[i]] = 1
    for i in s:
        if i in hasttable:
            return i


print firstRepeatingLetter("abcba")
