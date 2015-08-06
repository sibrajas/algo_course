import sys,resource
import time
def DFS(G,s):
    #if s in G.keys():
    for val in G[s]:
        if val not in explored:
            explored.append(val)
            DFS(G,val)
    f_times.append(s)
    return 

def DFSloop(G):
    for x in range(1,n+1):
        if x not in explored:
            DFS(G,x)
    print explored
    explored[:]=[]

def DFS_SCC(G,i,lead):
    explored.append(i)
    count_lead[lead]+=1
    #if i in G.keys():
    for val in G[i]:
        if val not in explored:
            DFS_SCC(G,val,lead)
    return

def DFSloop1(G):
    for node_ftime in reversed(f_times):
        if node_ftime not in explored:
            lead=node_ftime
            count_lead[lead]=0
            DFS_SCC(G,node_ftime,lead)
    print explored
    explored[:]=[]
    
if __name__=='__main__':
    start=time.time() 
    #G={}
    #n=875714
    n=12
    lead=-1
    f_times=[]
    count_lead={}
    lead=-1
    explored=[]
    sys.setrecursionlimit(10**6)
    resource.setrlimit(resource.RLIMIT_STACK,(2**29,2**30))
    #R=dict()
    G=[[] for i in range(n+1)]
    R=[[] for i in range(n+1)]
    #G={i+1:[] for i in range(875714)}
    #R={i+1:[] for i in range(875714)}
    with open("SCC4.txt") as f:
        for line in f:
            line=map(int,line.split())
            G[line[0]].append(line[1])
            R[line[1]].append(line[0])
    #print G
    print "Done reading the input file" 
    DFSloop(R)
    print "Done on reverse graph" 
    DFSloop1(G)
    print "Done on forward graph"
    #print leader
    #print leader.values()
    leadtoppers=[x for x in reversed(sorted(count_lead.values()))]
    if len(count_lead)<=5:
        appnd=5-len(count_lead)
    for i in range(5,appnd-1,-1):
        leadtoppers.append(0)
    end=time.time() 
    print leadtoppers[:5]
    print end-start 
