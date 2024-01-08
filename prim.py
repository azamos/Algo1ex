from graph import Graph
from minheap import Minheap

def build_tree_from_graph(G):
    tree = Graph(G.n)
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
    #else do nothing.
    u_id = newEdge[0]
    v_id = newEdge[1]
    new_weight = newEdge[2]
    u = T.vertices[u_id-1]
    v = T.vertices[v_id-1]
    if u.key <= new_weight and v.key <= new_weight:
        #if both u,v keys are already lighter than new_weight, the tree remains the same
        return
    replacer = None 
    if u.key > new_weight and v.key > new_weight:
        #if both u and v can reduce key from newEdge, pick the one who will reduce the most
        replacer = u if u.key>=v.key else v
    elif u.key > new_weight and v.key <= new_weight:
        #if only u can reduce its key
        replacer = u
    elif u.key<=new_weight and v.key > new_weight:
        #if only v can reduce its key
        replacer = v
    #del T.edges[(replacer.PI.id,replacer.id)]#TODO: create a proper deleteEdge method in Graph
    #TODO: ...,which will require in turn to add a remove method to DLL. Status: DONE
    T.deleteEdge(replacer.PI.id,replacer.id)#TODO: test this to hell and back
    T.addEdge(u_id,v_id,new_weight)