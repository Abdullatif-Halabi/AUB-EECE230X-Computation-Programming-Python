# from graph import DFSVisit, buildGraphFromFile
# import matplotlib.pyplot as plt

def extractPath(t,parent):
    def makeList(t,parent , L): 
        if parent[t] is None:
            L.append(t)
            L = L[::-1]
            return L
        L.append(t)
        return makeList(parent[t] , parent,L)
    return makeList(t , parent,[])

def DFSVisit(G,u,parent):
    """ Recursive Depth First Search function 
        Assumes G is a directed or undirected graph and u is node in G
        parent is a dict mapping each node (key) to its parent (value) in DFS traversal    """
    for v in G.adj[u]:
        if v not in parent:
            # If not visited yet, to avoid getting stuck in cycles
            parent[v]=u
            DFSVisit(G,v,parent)
   
def findAPath(G,s,t):
    parent = {s:None}
    DFSVisit(G,s,parent)
    if t not in parent:
        return []
    L = extractPath(t,parent)

    return L
    


# G = buildGraphFromFile("pa12Files/UndirectedGraph2.txt", undirected =True)
# # UndirectedGraph2.txt is available in compressed folder associated with this assignment
# plt.figure(2)
# plt.clf()
# G.draw()
# plt.show()
# print(findAPath(G,'A','F'))
# print(findAPath(G,'A','I'))
