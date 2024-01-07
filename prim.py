from graph import Graph
from minheap import Minheap
def prim(G):
    Q = Minheap()
    G = Graph()
    for i in range(1,G.n+1):
        Q.insert(G.vertices[i-1].key)
    r = G.vertices[i-1]
    r.key = 0
    r.PI = None
    while not Q.isEmpty():
        u = Q.extractMin()
        for v in u.neighbours:
            #need to test the search functionality
            if Q.search(v.key) >=0 and G.edges[(u,v)]<v.key:
                v.PI = u
                v.key = G.edges[(u,v)]