#Needleman-Wunsch Algorithm

import sys

def S(i,j,s1,s2):

    if(s1==0 and s2==0 and i==0 and j==0):
        return(-1)
    else:
        if(s1[i-1] == s2[j-1]):
            return(1)
        else:
            return(-1)

def Traceback_NW(array,s1,s2):

    Str = []
    str1 = []
    str2 = []
    i = len(array)-1
    j = len(array[0])-1

    while(not(i==0 and j==0)):

        a = -sys.maxsize
        b = -sys.maxsize
        c = -sys.maxsize

        if(i-1<0 and j-1>=0):
            b = array[i][j-1]
        elif(j-1<0 and i-1>=0):
            c = array[i-1][j]
        elif(i-1>=0 and j-1>=0):
            a = array[i-1][j-1]
            b = array[i][j-1]
            c = array[i-1][j]
        
        if(max(a,b,c) == a):
            str1.append(s1[i-1])
            str2.append(s2[j-1])
            i=i-1
            j=j-1
        elif(max(a,b,c) == b):
            str1.append('-')
            str2.append(s2[j-1])
            j=j-1
        elif(max(a,b,c) == c):
            str2.append('-')
            str1.append(s1[i-1])
            i=i-1

    Str.append(str1)
    Str.append(str2)
    return(Str)

def Needleman_Wunsch(s1,s2):
    
    array = []

    for i in range(len(s1)+1):
        temp = []
        for j in range(len(s2)+1):
            temp.append(0)
        array.append(temp)

    array[0][0] = 0

    for i in range(len(array)):
        for j in range(len(array[0])):
            if(i==0 and not(j==0)):
                array[i][j] = array[i][j-1]+S(0,0,0,0)
            elif(j==0 and not(i==0)):
                array[i][j] = array[i-1][j]+S(0,0,0,0)
            elif(not(j==0 and i==0)):
                array[i][j] = max(array[i-1][j-1]+S(i,j,s1,s2),array[i-1][j]+S(0,0,0,0),array[i][j-1]+S(0,0,0,0))

    Str = Traceback_NW(array,s1,s2)
    return(Str)

'''a = Needleman_Wunsch('CGTGAATTCAT','GACTTAC')
print(a[0])
print(a[1])'''
