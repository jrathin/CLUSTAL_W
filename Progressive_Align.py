#Progressive Alignment

import sys

def MS(i,j,l1,l2):

    if(l1==0 and l2==0 and i==0 and j==0):
        return(-1)

    h = []
    
    for k in range(len(l1)):
        h.append(l1[k][i])

    for k in range(len(l2)):
        h.append(l2[k][j])

    pairwise_score = 0

    for k in range(len(h)):
        for l in range(k,len(h),1):
            if(h[l]==h[k]):
                pairwise_score = pairwise_score + 1
            elif(h[l]=='-' or h[k]=='-'):
                pairwise_score = pairwise_score + -1
            else:
                pairwise_score = pairwise_score + -1

    return(pairwise_score)

def Traceback_PA(array,s1,s2):

    Str = []
    str1 = []
    str2 = []
    i = len(array)-1
    j = len(array[0])-1

    while(not(i==0 and j==0)):
        #print(i,j)
        #print(array)
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
            str1.append(i-1)
            str2.append(j-1)
            i=i-1
            j=j-1
        elif(max(a,b,c) == b):
            str1.append('-')
            str2.append(j-1)
            j=j-1
        elif(max(a,b,c) == c):
            str2.append('-')
            str1.append(i-1)
            i=i-1

    var = len(s1)+len(s2)
    for i in range(var):
        temp = []
        Str.append(temp)

    '''print(str1)
    print(str2)'''

    for i in range(len(str1)):
        if str1[i] == '-' and str2[i] == '-':
            for j in range(len(s1)):
                Str[j].append('-')
            for j in range(len(s1),var,1):
                Str[j].append('-')
                
        elif str1[i] == '-' and not str2[i] == '-':
            for j in range(len(s1)):
                Str[j].append('-')
            for j in range(len(s1),var,1):
                Str[j].append(s2[j-len(s1)][str2[i]])
                
        elif str2[i] == '-' and not str1[i] == '-':
            for j in range(len(s1),var,1):
                Str[j].append('-')
            for j in range(len(s1)):
                Str[j].append(s1[j][str1[i]])    

        else:
            for j in range(len(s1)):
                Str[j].append(s1[j][str1[i]])
            for j in range(len(s1),var,1):
                Str[j].append(s2[j-len(s1)][str2[i]])
    
    return(Str)


def Prog_Align(l1,l2):

    array = []

    for i in range(len(l1[0])+1):
        temp = []
        for j in range(len(l2[0])+1):
            temp.append(0)
        array.append(temp);

    array[0][0] = 0

    for i in range(len(array)):
        for j in range(len(array[0])):
            if(i==0 and not(j==0)):
                array[i][j] = array[i][j-1]+MS(0,0,0,0)
            elif(j==0 and not(i==0)):
                array[i][j] = array[i-1][j]+MS(0,0,0,0)
            elif(not(j==0 and i==0)):
                array[i][j] = max(array[i-1][j-1]+MS(i-1,j-1,l1,l2),array[i-1][j]+MS(0,0,0,0),array[i][j-1]+MS(0,0,0,0))


    Str = Traceback_PA(array, l1, l2)
    for i in range(len(Str)):
        Str[i].reverse()
    return(Str)
'''
l1 = [['g','a','a','t','c'],['g','g','a','-','t']]
l2 = [['g','c','t','c'],['a','-','-','c']]
a = Prog_Align(l1,l2)
for i in range(len(a)):
    print(a[i])
'''
