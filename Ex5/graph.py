class Graph:
    def __init__(self):
        self.vertices={}
    def add_vertex(self,vertex1):
        self.vertices[vertex1]=[]
    def add_edge(self,vertex1,vertex2,edgelen):
        if vertex1 in self.vertices.keys():
            self.vertices[vertex1].append([vertex2,edgelen])
        else:
            self.vertices[vertex1]=[vertex2,edgelen]
    def disp(self):
        for vertex in self.vertices.keys():
            print "-------------Edges of %d------------" %vertex
            for edge in self.vertices[vertex]:
                print edge
    def dijkstras(self,source):
        selfvertices=self.vertices.copy()
        print selfvertices
        X=[];A={}
        V=[v for v in self.vertices.keys()]
        A[source]=0
        X.append(source)
        V.remove(source)
        while len(V)>0:  #O(mn)
            minedgelength=100000
            for vertex in X:
                #print A[vertex]
                for vertex2,edgelength in self.vertices[vertex]:
                    nomoreedge=0
                    if vertex2 in V:
                        nomoreedge=1
                        if minedgelength>A[vertex]+edgelength:
                            minedgelength=A[vertex]+edgelength
                            minedge=[vertex,vertex2]
                    
            X.append(minedge[1])
            V.remove(minedge[1])
            A[minedge[1]]=minedgelength
            print X
            print A
            print V
            #print minedge
        print A
        print V
if __name__=='__main__':
    g=Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_edge(1,2,1)
    g.add_edge(1,3,4)
    g.add_edge(2,3,2)
    g.add_edge(2,4,6)
    g.add_edge(3,4,3)
    g.disp()
    g.dijkstras(3)
    g1=Graph()
    fd=open("dijkstraData.txt")
    lines=fd.readlines()
    for line in lines:
        line=line.strip().split()
        vertex1=int(line[0])
        g1.add_vertex(vertex1)
        for edge in line[1:]:
            edge=edge.split(',')
            [vertex2,edgelen]=map(int,edge)
            #map(int,edges.strip().split())
            #print vertex2,edgelen
            g1.add_edge(vertex1,vertex2,edgelen)
    #g1.disp()
    #g1.dijkstras(1)
