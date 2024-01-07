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
        self.vertices = [ Vertex() for i in range(1,n+1)]
        self.edges = []
    def addEdge(self,u,v,weight = 0):
        self.vertices[u-1].neighbours.addNode(DLLNode(v))
        self.edges.append(Edge(self.vertices[u-1],self.vertices[v-1],weight))
        m+=1
        if self.directed is False:
            self.vertices[v-1].neighbours.addNode(DLLNode(u))
            self.edges.append(Edge(self.vertices[v-1],self.vertices[u-1],weight))
            m+=1
    def printVertexEdges(self,u):
        #assumption: 1<=u<=n
        vertDll = self.vertices[u-1].neighbours
        p = vertDll.head
        while p is not None:
            print(f' ({u},{p.value})')
            p=p.prev
    def printGraph(self):
        for x in range(1,self.n+1):
            self.printVertexEdges(x)

class Vertex:
    def __init__(self) -> None:
        self.key = float("inf")#eventual minimum edge weight
        self.PI = None#from which other vertex the edge to this one came
        self.neighbours = DLL()#specifies the edges
class Edge:
    def __init__(self,src,dst,weight = 0) -> None:
        self.src = src
        self.dst = dst
        self.weight = weight