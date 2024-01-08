class DLLNode:#is a DLL Node.
    def __init__(self,value,next = None) -> None:
        self.value = value
        self.next = None
        self.prev = None
class DLL:
    def __init__(self,first = None) -> None:
        self.head = first
    def addNode(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            self.head.next = newNode
            newNode.prev = self.head
            self.head = newNode

class Graph:
    def __init__(self,n,directed = True) -> None:
        self.n = n
        self.m = 0
        self.directed = directed
        self.vertices = [ Vertex(i) for i in range(1,n+1)]
        self.edges = {}#todo: swich to dict implementation of edges. say {(1,2):w(1,2),(1,5):w:(1,5)} and so forth
    def addEdge(self,u,v,weight = 0):
        self.vertices[u-1].neighbours.addNode(DLLNode(v))
        self.edges[(self.vertices[u-1].id,self.vertices[v-1].id)] = weight
        self.m+=1
        if self.directed is False:
            self.vertices[v-1].neighbours.addNode(DLLNode(u))
            self.edges[(self.vertices[v-1].id,self.vertices[u-1].id)] = weight
            m+=1
    # def printVertexEdges(self,u):
    #     #assumption: 1<=u<=n
    #     vertDll = self.vertices[u-1].neighbours
    #     p = vertDll.head
    #     while p is not None:
    #         print(f' ({u},{p.value})')
    #         p=p.prev
    # def printGraph(self):
    #     for x in range(1,self.n+1):
    #         self.printVertexEdges(x)
    def printGraph(self):
        for vertex in self.vertices:
            print(vertex.id)
        for edge in self.edges:
            print(f"w({edge})={self.edges[edge]}")

    def print_spanning_tree(self):
        for vertex in self.vertices:
            print(f"vertex.id = {vertex.id},vertex.key={vertex.key},vertex.PI={vertex.PI}")
            #print(f"self.id = {vertex.id }\nself.key ={vertex.key}\n self.PI = {vertex.PI.key}")

class Vertex:
    def __init__(self,index) -> None:
        self.key = float("inf")#eventual minimum edge weight
        self.PI = None#from which other vertex the edge to this one came
        self.neighbours = DLL()#specifies the edges
        self.id =  index