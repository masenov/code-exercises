def sort(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if ()

def uniqueCharacters(s):
    s = sort(s)
    for i in range(len(s)-1):
        if (s[i]==s[i+1]):
            return False
    return True

uniqueCharacters("ksjfdskljf")
