import copy
import sys,resource
import time
class Heap:
    def __init__(self):
        self.heap={}
        self.heaplastindex=1
    def parent(self,c):
        return ((c)/2) if c!=1 else 1
    def leftchild(self,p):
        if (p)*2 in self.heap.keys():
            return (p)*2
        else:
            return -1
    def rightchild(self,p):
        if (p*2)+1 in self.heap.keys():
            return (p*2)+1
        else:
            return -1
    def swap(self,posa,posb):
        self.heap[posa],self.heap[posb]=self.heap[posb],self.heap[posa]
    def disp(self):
        print self.heap
    def insert(self,vertex,vertex2,djgreedyscore):
        heap=self.heap
        if len(heap)!=0:
            self.heaplastindex+=1
        heaplastindex=self.heaplastindex
        heap[heaplastindex]=[djgreedyscore,vertex,vertex2]
        indexiterator=heaplastindex
        while heap[indexiterator][0]<heap[self.parent(indexiterator)][0]:
            self.swap(indexiterator,self.parent(indexiterator))
            indexiterator=self.parent(indexiterator)
    def extractmin(self):
        rootindex=1
        heap=self.heap
        heaplastindex=self.heaplastindex
        self.swap(rootindex,self.heaplastindex)
        retelement=self.heap[self.heaplastindex]
        del(self.heap[self.heaplastindex])
        self.heaplastindex-=1
        cur=rootindex
        while 1:
            if ((self.rightchild(cur)!=-1) & (self.leftchild(cur)!=-1)):
                if self.heap[self.leftchild(cur)][0]<self.heap[self.rightchild(cur)][0]:
                    if self.heap[cur][0]>self.heap[self.leftchild(cur)][0]:
                        self.swap(cur,self.leftchild(cur))
                        cur=self.leftchild(cur)
                        continue
                    else:
                        break
                else:
                    if self.heap[cur][0]>self.heap[self.rightchild(cur)][0]:
                        self.swap(cur,self.rightchild(cur))
                        cur=self.rightchild(cur)
                        continue
                    else:
                        break
            if ((self.rightchild(cur)==-1) & (self.leftchild(cur)==-1)):
                return retelement
            if ((self.rightchild(cur)==-1) & (self.leftchild(cur)!=-1)):
                if self.heap[self.leftchild(cur)][0]<self.heap[cur][0]:
                    self.swap(cur,self.leftchild(cur))
                    cur=self.leftchild(cur)
                    continue
                else:
                    break
        return retelement        
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.h=Heap()
    def add_vertex(self,vertex1):
        self.vertices[vertex1]=[]
    def add_edge(self,vertex1,vertex2,edgelen):
        self.vertices[vertex1].append([vertex2,edgelen])
    def disp(self):
        for vertex in self.vertices.keys():
            print "-------------Edges of %d------------" %vertex
            for edge in self.vertices[vertex]:
                print edge
    def BFS_reachable(self,source):
        explored=[]
        queue=[]
        queue.append(source)
        while len(queue)>0:
            vertex=queue[0]
            explored.append(vertex)
            queue.pop(0)
            if vertex not in self.vertices.keys():
                continue
            for vertex2,edgelength in self.vertices[vertex]:
                if vertex2 not in explored:
                    if vertex2 not in queue:
                        queue.append(vertex2)
        return explored
    def extractminheap(self):
        return self.h.extractmin()
    def inserttoheap(self,vertex,vertex2,djgreedyscore):
        self.h.insert(vertex,vertex2,djgreedyscore)
    def heap_dijkstras(self,source):   #O(mlogn)
        selfvertices=self.vertices
        #selfvertices=self.vertices.copy()
        X=set([])
        allnodes=len(selfvertices)
        s=time.time()
        V=self.BFS_reachable(source)
        print "BFS "+str(time.time()-s)+" sec"
        n_reachable=len(V)
        A={i:1000000 for i in range(1,allnodes+1)}
        path={i:[] for i in range(1,allnodes+1)}
        A[source]=0
        path[source]=[source]
        X.add(source)
        V.remove(source)
        while len(X)<n_reachable:
            s=time.time()
            for vertex in X:
                for vertex2,edgelength in selfvertices[vertex]:
                    if vertex2 in V:
                        self.inserttoheap(vertex,vertex2,A[vertex]+edgelength)
                        selfvertices[vertex].remove([vertex2,edgelength])
            djlength,djsource,djwinner=self.extractminheap()
            if djlength<A[djwinner]:
                A[djwinner]=djlength
                #if djwinner not in X:
                X.add(djwinner)
                path[djwinner]=copy.copy(path[djsource])
                path[djwinner].append(djwinner)
                V.remove(djwinner)
            e=time.time()
            #print "finding a node in X  "+str(e-s)+" sec "+str(len(X))
        return A,path
if __name__=='__main__':
    if 0:
	    g=Graph({})
	    g.add_vertex(1)
	    g.add_vertex(2)
	    g.add_vertex(3)
	    g.add_vertex(4)
	    g.add_edge(1,2,1)
	    g.add_edge(1,3,4)
	    g.add_edge(2,3,2)
	    g.add_edge(2,4,6)
	    g.add_edge(3,4,3)
	    #g.disp()
	    x,p=g.heap_dijkstras(1)
	    print x
	    print p
    if 1:
        #g1=Graph()
        g={}
        resource.setrlimit(resource.RLIMIT_FSIZE,(resource.RLIM_INFINITY,resource.RLIM_INFINITY))#(2**30,2**31))
        resource.setrlimit(resource.RLIMIT_RSS,(resource.RLIM_INFINITY,resource.RLIM_INFINITY))#(2**30,2**31))
        resource.setrlimit(resource.RLIMIT_CPU,(resource.RLIM_INFINITY,resource.RLIM_INFINITY))#(2**30,2**31))
        resource.setrlimit(resource.RLIMIT_DATA,(resource.RLIM_INFINITY,resource.RLIM_INFINITY))#(2**30,2**31))
        resource.setrlimit(resource.RLIMIT_STACK,(resource.RLIM_INFINITY,resource.RLIM_INFINITY))#(2**30,2**31))
        s=time.time()
        if 0:
		with open("dijkstra_test20000.txt") as fd:
		    for line in fd:
			line=line.strip().split()
			vertex1=int(line[0])
			g1.add_vertex(vertex1)
			for edge in line[1:]:
			    #edge=edge.split(',')
			    [vertex2,edgelen]=map(int,edge.split(','))
			    g1.add_edge(vertex1,vertex2,edgelen)
        if 1:
		with open("dijkstraData.txt") as fd:
		    for line in fd:
			line=line.strip().split()
			#print line
			print int(line[0])
			for edge in line[1:]:
			    g.setdefault(int(line[0]),[]).append(map(int,edge.split(',')))
        e=time.time()
        print "Reading took "+str(e-s)+" Seconds"
        g1=Graph(g)
        #g1.disp()
        start=time.time()
        s,p=g1.heap_dijkstras(1)
        end=time.time()
        print "Running time of dj "+str(end-start)
        for i in [7,37,59,82,99,115,133,165,188,197]:
            if i not in s.keys():
                s[i]=1000000
            print 'Destination vertex is %d' %i
            print str(s[i])
            print p[i]

