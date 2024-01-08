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
            if Q.search(v.id) and G.edges[(u.id,v.id)]<v.key:
                v.PI = u
                v.key = G.edges[(u.id,v.id)]
                #forgot that V does not point to the same place as G.vertices[v.id-1]
                G.vertices[v.id-1].PI = v.PI
                G.vertices[v.id-1].key = v.key
                #Q.elemnts[v.id] = the index of v.id in Q.heap.
                #Q.elements is a dictionary, where vertex id is the key,
                #and the value is the index of vertex.id in the heap.
                #CONFUSING, since I have ids, used to differentiate vertices,
                #and KEY, which is used to define the heap, and is not unique.
                Q.heap[Q.elemnts[v.id]].key = v.key
                Q._heapifyUp_(Q.elemnts[v.id])#updated key is guaranteed to be smaller
                #than previous key, so only way possible is up, not down.
            p = p.prev
        #done updating all of u viable neighbours, now I can extract it
        print(f"\nExtracted min: {Q.extractMin()}")