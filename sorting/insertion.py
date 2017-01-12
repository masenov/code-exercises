# https://www.toptal.com/developers/sorting-algorithms


# Keep a sorted list and gradually expand it
def insertionSort(s):
    for i in range(len(s)):
        j = i
        while (j > 0 and s[j-1] > s[j]):
            # Swap j-1 and j element in a string - have to create a new String since
            # String are immutable in Python
            s = s[0:j-1]+s[j]+s[j-1]+s[j+1:]
            j = j - 1
    return s

a = "qwertyuiopasdfghjklzxcvbnm"
print (insertionSort(a))
