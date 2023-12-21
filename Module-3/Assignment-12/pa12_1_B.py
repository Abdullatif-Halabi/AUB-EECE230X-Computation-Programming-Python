from graph import UndirectedGraph

def adjacent(M,i,j): 
    m = len(M)
    n = len(M[0])
    adjCells = []
    if i<m-1 and M[i+1][j]: # down
        adjCells.append((i+1,j))
    if j<n-1 and M[i][j+1]: # right
        adjCells.append((i,j+1))  
    if i>0 and M[i-1][j]:  # up
        adjCells.append((i-1,j))  
    if j>0 and M[i][j-1]: # left
        adjCells.append((i,j-1))          
    return adjCells

def buildGraphFromMaze(M):
    G = UndirectedGraph()
    # Adding all available nodes in the maze to the dictionnary G.adj 
    # by using addNode() function and looping over each element
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j]:
                G.addNode((i,j))

    for (i,j) in G.adj:
        for (k,l) in adjacent(M,i,j):
            if (k,l) not in G.adj[(i,j)]:
                x = (i,j)
                y = (k,l)
                G.connect(x,y)   
    
    return G

# import numpy
# M = [[True, False, True],
# [True, True, True],
# [True, False, True]]
# print("M:")
# print(numpy.matrix(M,int))
# G= buildGraphFromMaze(M)
# print("G:")
# print(G)