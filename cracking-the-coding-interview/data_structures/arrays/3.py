def permutationString(s1,s2):
    sorted1 = "".join(sorted(s1))
    sorted2 = "".join(sorted(s2))
    if (sorted1 == sorted2):
        return True
    else:
        return False

s1 = "test"
s2 = "estt"
s3 = "different test"
print (permutationString(s1,s2))
print (permutationString(s1,s3))
