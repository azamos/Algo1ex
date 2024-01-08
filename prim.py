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
        #u = Q.extractMin()
        u = Q.observeMin()#above line was source of BUG.
        #for v in u.neighbours:
        p = u.neighbours.head
        while p is not None:
            v = p.value
            if v.id==5:
                print("breakpoint")
            if Q.search(v.id) and G.edges[(u.id,v.id)]<v.key:
                v.PI = u
                v.key = G.edges[(u.id,v.id)]
                #forgot that V does not point to the same place as G.vertices[v.id-1]
                G.vertices[v.id-1] = v
            p = p.prev
        #done updating all of u viable neighbours, now I can extract it
        u = Q.extractMin()