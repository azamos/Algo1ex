from graph import Graph
from prim import prim_spanning_tree,update_tree

N = 20
G = Graph(n=N)#creating a DIRECTED graph with vertices = {1,2,3....,18,19,20}

for i in range(1,G.n):#Adding succesive jumps of 1: 19 edges
    #(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,11),(11,12),(12,13)
    #(13,14),(14,15),(15,16),(16,17),(17,18),(18,19),(19,20)
    G.addEdge(i,i+1,1)

for i in range(2,G.n-1,2):#adding succesive jumps of 2: 18 edges
    #(2,4),(4,6),(6,8),(8,10),(10,12),(12,14),(14,16),(16,18),(18,20)
    G.addEdge(i,i+2,2)
    #(1,3),(3,5),(5,7),(7,9),(9,11),(11,13),(13,15),(15,17),(17,19)
    G.addEdge(i-1,i+1,2)

for i in range(3,G.n-2,3):#Adding succesive jumps of 3 = 17 edges 
    #(3,6),(6,9),(9,12),(12,15),(15,18)
    G.addEdge(i,i+3,3)
    #(2,5),(5,8),(8,11),(11,14),(14,17),(17,20)
    G.addEdge(i-1,i+2,3)
    #(1,4),(4,7),(7,10),(10,13),(13,16),(16,19)

#Now I have a total of 54 edges

G.printGraph()
#print("\n before activating prim algorithm, the default data is: \n")
#G.print_spanning_tree()#before activating prim
T = prim_spanning_tree(G)
print("After activating Prim algorithm to extract spanning tree...\n")
#G.print_spanning_tree()
T.printGraph()
# print("New edge added: (2,3) with weight 10. Should change nothing\n")
# update_tree(T,(2,3,10))
# T.printGraph()

# print("New edge added: (2,3) with weight 8. Should change only the key of 3 to 8, from 9\n")
# update_tree(T,(2,3,8))
# T.printGraph()