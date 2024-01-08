from graph import Graph
from prim import prim_spanning_tree,update_tree

G = Graph(5)#creating a DIRECTED graph with vertices = {1,2,3,4,5}
G.addEdge(1,2,17)
G.addEdge(1,3,12)
G.addEdge(1,4,15)

G.addEdge(2,5,24)

G.addEdge(3,1,3)
G.addEdge(3,5,25)

G.addEdge(4,2,11)
G.addEdge(4,3,9)

#G.printGraph()
#print("\n before activating prim algorithm, the default data is: \n")
#G.print_spanning_tree()#before activating prim
T = prim_spanning_tree(G)
#print("After activating Prim algorithm to extract spanning tree...\n")
#G.print_spanning_tree()
T.printGraph()
print("New edge added: (2,3) with weight 10. Should change nothing\n")
update_tree(T,(2,3,10))
T.printGraph()

print("New edge added: (2,3) with weight 8. Should change only the key of 3 to 8, from 9\n")
update_tree(T,(2,3,8))
T.printGraph()