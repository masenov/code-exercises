def compressString(s):
    new_string = ""
    current = s[0]
    count = 1
    for i in range(1,len(s)):
        if (s[i]==current):
            count = count + 1
        else:
            new_string = new_string + s[i-1] + str(count)
            current = s[i]
            count = 1
    new_string = new_string + s[len(s)-1] + str(count)
    if (len(new_string)<len(s)):
        return new_string
    else:
        return s

print (compressString("aabcccccaaa"))
