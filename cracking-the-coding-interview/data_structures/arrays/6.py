def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print (str(i)+str(j))

def printRotMatrix(n):
    for j in range(n):
        for i in range(n-1,-1,-1):
            print (str(i)+str(j))

printMatrix(4)
print ()
printRotMatrix(4)
