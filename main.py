from graph import Graph
from prim import prim_spanning_tree

G = Graph(5)#creating a DIRECTED graph with vertices = {1,2,3,4,5}
G.addEdge(1,2,17)
G.addEdge(1,3,12)
G.addEdge(1,4,15)

G.addEdge(2,5,24)

G.addEdge(3,1,3)
G.addEdge(3,5,25)

G.addEdge(4,2,11)
G.addEdge(4,3,9)

G.printGraph()
print("\n before activating prim algorithm, the default data is: \n")
G.print_spanning_tree()#before activating prim
prim_spanning_tree(G)
print("After activating Prim algorithm to extract spanning tree...\n")
G.print_spanning_tree()