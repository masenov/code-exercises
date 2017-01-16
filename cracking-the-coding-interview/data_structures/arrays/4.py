def replaceCharacter(s,pos,char):
    return s[0:pos]+char+s[pos+1:]

def replaceSpaces(s,true_length):
    actual_length = len(s)-1
    for i in range(true_length-1, -1, -1):
        if (s[i]==' '):
            s=replaceCharacter(s,actual_length,'0')
            s=replaceCharacter(s,actual_length-1,'2')
            s=replaceCharacter(s,actual_length-2,'%')
            actual_length = actual_length - 3
        else:
            s=replaceCharacter(s,actual_length,s[i])
            actual_length = actual_length - 1
    return s


print (replaceCharacter("asdf",3,'x'))
print (replaceSpaces("Mr John Smith    ", 13))
