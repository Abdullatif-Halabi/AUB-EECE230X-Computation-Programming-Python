from graph import buildGraphFromFile , UndirectedGraph
import matplotlib.pyplot as plt

def DFVisitModified(G,u,index,count):
    if u not in index:
        index[u] = count
    for v in G.adj[u]:
        if v not in index:
            DFVisitModified(G,v,index,count)
    

def findConnectedComponents(G):
    count = -1   
    index = {} 
    for u in G.adj:
        if u not in index :
            count += 1
        DFVisitModified(G,u,index,count)
    print(index)    
    L = [[]]
    for x in index:
        if index[x] == len(L):
            L.append([])
        L[index[x]].append(x)

    return L


# G = UndirectedGraph()
# G.adj = {'a': ['b'], 'q': [], 'f': ['b'], 'b': ['f', 'a']}
# print(findConnectedComponents(G))

# # index = {}
# # DFSVisitModified(G,'A',index)
# G = buildGraphFromFile("pa12Files/UndirectedGraph4.txt", undirected =True)
# print(G.adj)
# print(findConnectedComponents(G))

# G = buildGraphFromFile("pa12Files/UndirectedGraph3.txt", undirected =True)
# plt.figure(2)
# plt.clf()
# G.draw()
# print(findConnectedComponents(G))
# G = buildGraphFromFile("pa12Files/UndirectedGraph1.txt", undirected =True)
# plt.figure(1)
# plt.clf()
# G.draw()
# print(findConnectedComponents(G))
# G = buildGraphFromFile("pa12Files/UndirectedGraph4.txt", undirected =True)
# plt.figure(3)
# plt.clf()
# G.draw()
# print(findConnectedComponents(G))

# plt.show()

