from graph import UndirectedGraph
import matplotlib.pyplot as plt

def buildCircleGraph(n):
    assert n >=3 , 'n should be bigger than or equal to 3'
    nodes = [x for x in range(1, n + 1)]
    G = UndirectedGraph()
    adj = {}
    for x in nodes:
        adj[x] = []

    G.adj = adj
    for i in range(len(nodes)):
        if i == n - 1:
            G.connect(nodes[-1],nodes[0])
        else:
            G.connect(nodes[i], nodes[i + 1])
    return G

# G = buildCircleGraph(5)
# print(G)
# plt.figure(1)
# plt.clf()
# G.draw()
