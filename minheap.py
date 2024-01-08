class Minheap:
    def __init__(self) -> None:
        self.heap = []#heap of Vertexes, sorted by Vertex.key, NOT by vertex.id
        self.n = 0
        self.elemnts = {}#extra memory, to get amortized time complexity of O(1)
                         #to detect if key is in the heap. Faster than O(logn).
                         #Needed for Prim algorithm.
    
    def isEmpty(self)->bool:
        return self.n==0

    def _swap_(self,i,j):
        tmp = self.heap[j]
        self.heap[j] = self.heap[i]
        self.heap[i] = tmp

    def _heapifyUp_(self,index) -> None:
        while index!=0 and self.heap[index//2].key>self.heap[index].key:
            self._swap_(index,index//2)
            index = index//2
    #For heapify down, to determine where to go down.
    def _smallerChild_(self,index):
        left_i = 2*index+1
        right_i = left_i+1
        if right_i < self.n and self.heap[right_i].key>self.heap[left_i].key:
            return right_i
        return left_i

    def _heapifyDown_(self,index=0):
        while index < self.n//2 and self.heap[index].key>self.heap[self._smallerChild_(index)].key:
            smallChild = self._smallerChild_(index)
            self._swap_(index,smallChild)
            index = smallChild
    def extractMin(self) -> float:
        self._swap_(0,self.n-1)
        ret = self.heap.pop()#First we swap minimum(index 0) with last cell of array, then pop it
        self.n-=1#source of bug. was after the call to self._heapifyDown(), caused
        #index out of bound exception
        del self.elemnts[ret.id]#test if working
        self._heapifyDown_()
        return ret
    
    def observeMin(self) -> float:
        return None if self.isEmpty() else self.heap[0]
    
    def insert(self,newVetrex):
        self.heap.append(newVetrex)
        self.n+=1
        self.elemnts[newVetrex.id] = newVetrex
        self._heapifyUp_(self.n-1)

    def search(self,id):
        return id in self.elemnts
                