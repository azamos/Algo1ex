from graph import Graph
from minheap import Minheap
def prim_spanning_tree(G,r=0):
    Q = Minheap()
    for i in range(1,G.n+1):
        Q.insert(G.vertices[i-1])
    G.vertices[r].key = 0
    G.vertices[r].PI = None
    print("Initiated vertex r: \n")
    G.print_spanning_tree()
    while not Q.isEmpty():
        u = Q.extractMin()
        #for v in u.neighbours:
        v = u.neighbours.head
        while v is not None:
            #need to test the search functionality
            if Q.search(v.id) and G.edges[(u,v)]<v.key:
                v.PI = u
                v.key = G.edges[(u,v)]
                v = v.prev