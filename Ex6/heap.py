import copy
class MaxHeap:
    def __init__(self):
        self.heap={}
        self.heaplastindex=0
    def parent(self,c):
        return ((c+1)/2)-1 if c!=0 else 0
    def leftchild(self,p):
        if (p+1)*2-1 in self.heap.keys():
            return (p+1)*2-1
        else:
            return -1
    def rightchild(self,p):
        if (p+1)*2 in self.heap.keys():
            return (p+1)*2
        else:
            return -1
    def swap(self,posa,posb):
        self.heap[posa],self.heap[posb]=self.heap[posb],self.heap[posa]
    def disp(self):
        print self.heap
    def insert(self,element):
        heap=self.heap
        if len(heap)!=0:
            self.heaplastindex+=1
        heaplastindex=self.heaplastindex
        heap[heaplastindex]=element
        indexiterator=heaplastindex
        while heap[indexiterator]>heap[self.parent(indexiterator)]:
            self.swap(indexiterator,self.parent(indexiterator))
            indexiterator=self.parent(indexiterator)
    def extractmax(self):
        if len(self.heap)==0:
            return None
        rootindex=0
        heap=self.heap
        heaplastindex=self.heaplastindex
        self.swap(rootindex,self.heaplastindex)
        retelement=self.heap[self.heaplastindex]
        del(self.heap[self.heaplastindex])
        if self.heaplastindex!=0:
            self.heaplastindex-=1 
        cur=rootindex
        while 1:
            if ((self.rightchild(cur)==-1) & (self.leftchild(cur)==-1)):
                return retelement
            if ((self.rightchild(cur)==-1) & (self.leftchild(cur)!=-1)):
                if self.heap[self.leftchild(cur)]>self.heap[cur]:
                    self.swap(cur,self.leftchild(cur))
                    cur=self.leftchild(cur)
                    continue
                else:
                    break
            if ((self.rightchild(cur)!=-1) & (self.leftchild(cur)!=-1)):
                if self.heap[self.leftchild(cur)]>self.heap[self.rightchild(cur)]:
                    if self.heap[cur]<self.heap[self.leftchild(cur)]:
                        self.swap(cur,self.leftchild(cur))
                        cur=self.leftchild(cur)
                        continue
                    else:
                        break
                else:
                    if self.heap[cur]<self.heap[self.rightchild(cur)]:
                        self.swap(cur,self.rightchild(cur))
                        cur=self.rightchild(cur)
                        continue
                    else:
                        break
        return retelement        
class Heap:
    def __init__(self):
        self.heap={}
        self.heaplastindex=0
    def parent(self,c):
        return ((c+1)/2)-1 if c!=0 else 0
    def leftchild(self,p):
        if (p+1)*2-1 in self.heap.keys():
            return (p+1)*2-1
        else:
            return -1
    def rightchild(self,p):
        if (p+1)*2 in self.heap.keys():
            return (p+1)*2
        else:
            return -1
    def swap(self,posa,posb):
        self.heap[posa],self.heap[posb]=self.heap[posb],self.heap[posa]
    def disp(self):
        print self.heap
    def insert(self,element):
        heap=self.heap
        if len(heap)!=0:
            self.heaplastindex+=1
        heaplastindex=self.heaplastindex
        heap[heaplastindex]=element
        indexiterator=heaplastindex
        while heap[indexiterator]<heap[self.parent(indexiterator)]:
            self.swap(indexiterator,self.parent(indexiterator))
            indexiterator=self.parent(indexiterator)
    def extractmin(self):
        if len(self.heap)==0:
            return None
        rootindex=0
        heap=self.heap
        heaplastindex=self.heaplastindex
        self.swap(rootindex,self.heaplastindex)
        retelement=self.heap[self.heaplastindex]
        del(self.heap[self.heaplastindex])
        if self.heaplastindex!=0:
            self.heaplastindex-=1 
        cur=rootindex
        while 1:
            if ((self.rightchild(cur)==-1) & (self.leftchild(cur)==-1)):
                return retelement
            if ((self.rightchild(cur)==-1) & (self.leftchild(cur)!=-1)):
                if self.heap[self.leftchild(cur)]<self.heap[cur]:
                    self.swap(cur,self.leftchild(cur))
                    cur=self.leftchild(cur)
                    continue
                else:
                    break
            if ((self.rightchild(cur)!=-1) & (self.leftchild(cur)!=-1)):
                if self.heap[self.leftchild(cur)]<self.heap[self.rightchild(cur)]:
                    if self.heap[cur]>self.heap[self.leftchild(cur)]:
                        self.swap(cur,self.leftchild(cur))
                        cur=self.leftchild(cur)
                        continue
                    else:
                        break
                else:
                    if self.heap[cur]>self.heap[self.rightchild(cur)]:
                        self.swap(cur,self.rightchild(cur))
                        cur=self.rightchild(cur)
                        continue
                    else:
                        break
        return retelement        
if __name__=='__main__':
    if 1:
        h=MaxHeap()
        h.insert(34)
        h.insert(26)
        h.insert(2)
        h.insert(21)
        h.insert(35)
        h.insert(24)
        h.insert(15)
        h.insert(33)
        h.insert(4)
        h.insert(12)
        h.insert(1)
        h.insert(23)
        h.insert(5)
        h.disp()
        while (len(h.heap)>0):
            print h.extractmax()
            print h.heap
        print h.extractmax()
        print h.heap
        print h.extractmax()
        print h.heap
        print h.extractmax()
        print h.heap
        print h.extractmax()
        print h.heap
        h.insert(34)
        h.insert(26)
        h.insert(2)
        h.insert(21)
        h.insert(35)
        h.insert(24)
        h.insert(15)
        h.insert(33)
        h.insert(4)
        h.insert(12)
        h.insert(1)
        h.insert(23)
        h.insert(5)
        h.disp()
        while (len(h.heap)>0):
            print h.extractmax()
            print h.heap

