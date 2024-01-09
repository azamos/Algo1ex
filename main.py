from graph import Graph
from prim import prim_spanning_tree,update_tree

N = 20
G = Graph(n=N)#creating a DIRECTED graph with vertices = {1,2,3....,18,19,20}

for i in range(1,G.n):#Adding succesive jumps of 1: 19 edges
    #(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,11),(11,12),(12,13)
    #(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),(19,20)
    G.addEdge(i,i+1,1)

for i in range(1,G.n-1):#adding succesive jumps of 2: 18 edges
    #(1,3),(3,5),(5,7),(7,9),(9,11),(11,13),(13,15),(15,17),(17,19)
    #(2,4),(4,6),(6,8),(8,10),(10,12),(12,14),(14,16),(16,18),(18,20)
    G.addEdge(i,i+2,2)

for i in range(1,G.n-2):#Adding succesive jumps of 3 = 17 edges
    #(1,4),(4,7),(7,10),(10,13),(13,16),(16,19) 
    #(2,5),(5,8),(8,11),(11,14),(14,17),(17,20)
    #(3,6),(6,9),(9,12),(12,15),(15,18)
    G.addEdge(i,i+3,3)
    
#Now I have a total of 54 edges(
print(f"|edges| = {len(G.edges.items())}")
print("G is: ")
G.printGraph()
print("_________________________")
T = prim_spanning_tree(G)
print("spanning tree of G: ")
T.printGraph()
print("_________________________")
G.addEdge(20,3,1000)
e = (20,3)
print(f"added new edge: w({e})={G.edges[e]}")
update_tree(T,(20,3,1000))#Should not affect the tree
print(f"tree after adding e = {e}: ")
T.printGraph()
print("_________________________")
G.addEdge(20,1,-15)
another_e = (20,1)
print(f"added another new edge: w({another_e})={G.edges[another_e]}")
update_tree(T,(20,1,-15))#Should affect the tree
print(f"tree after adding anther e = {another_e}: ")
T.printGraph()
print("_________________________")
print("END")