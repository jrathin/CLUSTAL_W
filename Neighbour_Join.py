#Neighbour Joining Method

import sys

def Min_Pos(matrix):

    Min = sys.maxsize
    x=-1
    y=-1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]>=0 and matrix[i][j]<Min:
                Min = matrix[i][j]
                x = i
                y = j
    return(x,y)
            
def Reconstruct(phy_mat,cost):
    
    tree = []
    vert = []
    count = 0
    
    for i in range(len(phy_mat)):
        for j in range(len(phy_mat[i])):
            if phy_mat[i][j].replace('.','') not in vert:
                vert.append(phy_mat[i][j].replace('.',''))
                count = count+1

    

    for i in range(count):
        temp = []
        for j in range(count):
            temp.append(0);
        tree.append(temp)

    for i in range(len(phy_mat)):
        for j in range(len(phy_mat[i])):
            if len(phy_mat[i][j])>1:
                a = phy_mat[i][j].split('.')
                tree[vert.index(phy_mat[i][j].replace('.',''))][vert.index(a[0])] = 1
                tree[vert.index(phy_mat[i][j].replace('.',''))][vert.index(a[1])] = 1
                tree[vert.index(a[0])][vert.index(phy_mat[i][j].replace('.',''))] = 1
                tree[vert.index(a[1])][vert.index(phy_mat[i][j].replace('.',''))] = 1

    '''for i in range(len(tree)):
        print(tree[i])
    print(vert)'''
    return(tree,vert)           

def NJ(matrix):

    var = len(matrix)
    phy_mat = []
    row_ref = []
    cost = []

    for i in range(len(matrix)):
        row_ref.append(str(i))

    phy_mat.append(row_ref[:])

    while len(matrix)>1:
       
        x,y = Min_Pos(matrix)
        cost.append(matrix[x][y])
        if x>y:
            q = y
            y = x
            x = q        

        temp = []
        for i in range(len(matrix)):
            matrix[i].append((matrix[i][x]+matrix[i][y])/2)
            temp.append((matrix[i][x]+matrix[i][y])/2)

        temp.append(-1) 
        matrix.append(temp)        

        for i in range(len(matrix)):
            del(matrix[i][y])
        
        for i in range(len(matrix)):
            del(matrix[i][x])

        del(matrix[y])
        del(matrix[x])

        row_ref.append(row_ref[x].replace('.', '')+'.'+row_ref[y].replace('.',''))
        del(row_ref[y])
        del(row_ref[x])
        phy_mat.append(row_ref[:])
    
    tree,vert = Reconstruct(phy_mat,cost)
    return(tree,vert,phy_mat)
    

matrix = [[-1,17,59,59,77],[17,-1,37,61,53],[59,37,-1,13,41],[59,61,13,-1,21],[77,53,41,21,-1]]
print(NJ(matrix))

