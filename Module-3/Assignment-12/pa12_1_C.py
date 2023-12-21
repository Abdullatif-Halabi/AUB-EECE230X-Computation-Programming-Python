from graph import DiGraph,buildGraphFromFile
# import matplotlib.pyplot as plt
def transpose(G):
    adj_1 = {}
    for u in G.adj:
        if u not in adj_1:
            adj_1[u] = [] 
        for v in G.adj[u]:
            if v not in adj_1:
                adj_1[v] = []
            adj_1[v].append(u)
    G_t = DiGraph()
    G_t.adj = adj_1
    return G_t

# G = buildGraphFromFile("pa12Files\DiGraph1.txt", undirected = False)
# # DiGraph1.txt is available in compressed folder associated with this assignment
# plt.figure(1)
# plt.clf()
# G.draw()
# GTranspose = transpose(G)
# plt.figure(2)
# plt.clf()
# GTranspose.draw()
# plt.show()
# print(G)
# print(GTranspose)