from graph import buildGraphFromFile , UndirectedGraph
from circularQueue import Queue

def extractPath(t,parent):
    def makeList(t,parent , L): 
        if isinstance(parent[t], list):
            L.append(t)
            prev = parent[t][1]
            parent[t] = None
            return makeList(prev,parent,L)
        if parent[t] is None:
            if len(L) != 0 :
                L.append(t)
                L = L[::-1]
                return L
            else : 
                return []
        L.append(t)
        return makeList(parent[t] , parent,L)
    return makeList(t , parent,[])

def BFS(G,s,t):
   """ Breadth First Search function
       Assumes G is a directed or undirected graph and u is node in G
       Returns dict distance  mapping each node u (key) to the length of the  shortest 
                    path from source s to u (value) 
           and dict parent mapping each node (key) to its parent (value) in shortest path to source """
   """ But this time the algorithm stops bulding the two dictionnaries once the target is found """

   assert s in G.adj, "node not in graph"
   parent = {s:None} 
   distance = {s:0} 
   # Initialize Q of max size the number of nodes in G: len(G.adj)
   Q = Queue(len(G.adj))
   Q.enqueue(s)
   found = False
   while not Q.isEmpty():
       u = Q.dequeue()
       for v in G.adj[u]:
            if v==s==t:
                parent[s] = [None]
                parent[s].append(u)
                found = True
                break
            if v not in distance:
                distance[v]=distance[u]+1
                parent[v]=u
                if v != t:
                    Q.enqueue(v)
                else: 
                    found = True
                    break            
       if found :break
   return (distance,parent)

def findShortestPath(G,s,t):
    __ , parent = BFS(G,s,t)
    #Handling the case when source == target
    if s == t:
        if s in G.adj[s] or G.adj[s] == [] :
            return [s,s]
        else: return extractPath(t,parent)

    if t not in parent:
        return []
    
    return extractPath(t,parent)


# G = UndirectedGraph()

# G.adj = {'a': ['q'], 'e': [], 'q': []}
# __,parent = BFS(G,'a' , 'a')
# print(parent)
# print(findShortestPath(G, s = 'a', t = 'a'))

#Runtime error "local variable 'v' referenced before assignment" while testing 
# G = buildGraphFromFile('My_sol_12\dext.txt',undirected=True)
# G.adj = {'a': [], 'q': [], 'l': ['q', 'l'], 'u': []}
# print(G)
# print(findShortestPath(G, s = 'q', t = 'a'))

# G = buildGraphFromFile("pa12Files/UndirectedGraph2.txt", undirected =True)
# print(G.adj)
# distance , parent = BFS(G,'A','F')
# print(parent)
# print(distance)
# print(extractPath('F',parent))
# print(findShortestPath(G,'A','F'))

# print('\n NOW SECOND TEST \n ')

# from pa12_1_B import buildGraphFromMaze
# import numpy
# M=[[True, False, True, True, False, True, True],
# [True, True, False, True, True, False, False],
# [False, True, True, True, True, True, True],
# [False, True, True, False, False, False, True],
# [False, True, False, True, True, False, True]]
# print("M:")
# print(numpy.matrix(M,int))
# GMaze= buildGraphFromMaze(M)
# print(findShortestPath(GMaze,(0,0),(4,6)))