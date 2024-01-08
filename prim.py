from graph import Graph
from minheap import Minheap

def build_tree_from_graph(G):
    tree = Graph(G.n)
    #print(tree.vertices)
    #Decided not to only make a special case for the root,
    #Since not all graphs are necessarily connected, thus
    #we can get v.PI = None for v's other than root
    #Though, I am not sure Prim takes that into consideration?TODO: check this.
    for i in range(1,G.n+1):
        #since key is a numerical value, simply copying it is all it takes.
        tree.vertices[i-1].key = G.vertices[i-1].key
        #PI is a bit more difficult, since in G it points to another vertex
        #in G, however in T, we need it to point to another vertex in T,
        #one with corresponding id to the one in G.
        G_vert_i_PI = G.vertices[i-1].PI
        if G_vert_i_PI is None:
            tree.vertices[i-1].PI = None
        else:
            tree.vertices[i-1].PI = tree.vertices[G_vert_i_PI.id-1]
    for v in G.vertices:
        if v.PI is not None:
            tree.addEdge(v.PI.id,v.id,v.key)
    return tree

def prim_spanning_tree(G,r=0):
    Q = Minheap()
    for i in range(1,G.n+1):
        Q.insert(G.vertices[i-1])
    G.vertices[r].key = 0
    G.vertices[r].PI = None
    #print("Initiated vertex r: \n")
    #G.print_spanning_tree()
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
        Q.extractMin()
        #print(f"\nExtracted min: {Q.extractMin()}")
    return build_tree_from_graph(G)

def update_tree(T,newEdge):#newedge = (u,v,w(u,v)). for example: (1,4,13)
    #TODO:1. when copying the vertices from the Graph into the tree,
    #need to update the PI field accordingly.
    #2.Bellow, make sure that replacer.PI is not NONE.
    #if it is, either make sure it takes the other vertex if its key < new_weight,
    #else do nothing.ON SECOND thoughts, logically, it should never be NONE.
    #Only for the root it maybe None, but the root is 0, the smallest possible weight
    u_id = newEdge[0]
    v_id = newEdge[1]
    new_weight = newEdge[2]
    v = T.vertices[v_id-1]
    if v.key > new_weight:
        #if we got here, it means that removing the edge (v.PI.id,v.id) from the graph
        #and replacing it with (u,v) will net us a lighter weight spanning tree
        #of the new G, which is G = (oldG(V),oldG(E) Union {(u,v)})
        T.deleteEdge(v.PI.id,v.id)#TODO: 
        T.addEdge(u_id,v_id,new_weight)