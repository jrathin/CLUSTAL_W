#Final Code including all induvidual components

from MSA import *
from Progressive_Align import *
from Neighbour_Join import *
import networkx as nx
import matplotlib.pyplot as plt

def Represent_as_Graph(matrix):
    g = nx.Graph()
    g.add_nodes_from([1,len(matrix)])
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j]>=1 and matrix[j][i]>=1):
                g.add_edge(i+1,j+1)
    return(g)

def CS(s1,s2):

    value = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            value = value+5
        elif s1[i] == '-' or s2[i] == '-':
            value = value-1
        else:
            value = value+1
    return(value)

def main():
    Seq = ['actct','agcat','agct','acttg','ctct']

    f_seq = []
    Score_Mat = []

    for i in range(len(Seq)):
        temp = []
        for j in range(len(Seq)):
            temp.append(0)
        Score_Mat.append(temp)

    for i in range(len(Seq)):
        for j in range(len(Seq)):
            if(not i == j):
                var = Needleman_Wunsch(Seq[i],Seq[j])
                f_seq.append(var)
                Score = CS(var[0],var[1])
                Score_Mat[i][j] = Score
                Score_Mat[j][i] = Score
            if(i==j):
                Score_Mat[i][j] = -1
                Score_Mat[j][i] = -1
        
    print(Score_Mat)
    tree,vert,phy_mat = NJ(Score_Mat)
    '''for i in range(len(phy_mat)):
        print(phy_mat[i])
    print(vert)
    '''
    #print(f_seq)
    A1 = []
    for i in range(len(Seq)):
        A1.append(list(Seq[i]))
        
    for i in range(len(phy_mat)):
        for j in range(len(phy_mat[i])):
            if(len(phy_mat[i][j])>1 and phy_mat[i][j] not in phy_mat[i-1] and not i==0):
                a = phy_mat[i][j].split('.')
                if(len(a[0])==1 and len(a[1])==1):
                    s = []
                    t = []
                    s.append(list(Seq[int(a[0])]))
                    t.append(list(Seq[int(a[1])]))
                    A1.append(Prog_Align(s,t))
                else:
                    if(len(a[0])==1):
                        s = []
                        s.append(list(Seq[int(a[0])]))
                        A1.append(Prog_Align(s,A1[vert.index(a[1])]))
                    elif(len(a[1])==1):
                        s = []
                        s.append(list(Seq[int(a[1])]))
                        A1.append(Prog_Align(A1[vert.index(a[0])]),s)
                    else:
                        A1.append(Prog_Align(A1[vert.index(a[0])],A1[vert.index(a[1])]))


    for j in range(len(A1)):
        for i in range(len(A1[j])):
            print(A1[j][i])
        print('\n')

    print(phy_mat)
    print(vert)
           
    g = nx.Graph()
    g = Represent_as_Graph(tree)
        
    nx.draw(g)
    plt.show()       
    

if __name__ == '__main__':
    main()
    
