import sys,resource
import time
def DFS(G,s):
    #if s in G.keys():
    global explored
    for val in G[s]:
        if explored[val]==0:
            explored[val]=1
            DFS(G,val)
    f_times.append(s)
    return 

def DFSloop(G):
    global explored
    for x in range(1,n+1):
        if explored[x]==0:
            DFS(G,x)
    #print explored
    explored={i:0 for i in range(1,n+1)}

def DFS_SCC(G,i):
    global explored,lead
    explored[i]=1
    count_lead[lead]+=1
    #if i in G.keys():
    for val in G[i]:
        if explored[val]==0:
            DFS_SCC(G,val)
    return

def DFSloop1(G):
    global explored,lead
    for node_ftime in reversed(f_times):
        if explored[node_ftime]==0:
            lead=node_ftime
            count_lead[lead]=0
            DFS_SCC(G,node_ftime)
    #print explored
    explored={i:0 for i in range(1,n+1)}
    
if __name__=='__main__':
    start=time.time() 
    #G={}
    n=875714
    #n=12
    explored={i:0 for i in range(1,n+1)}
    f_times=[]
    count_lead={}
    lead=-1
    sys.setrecursionlimit(10**6)
    resource.setrlimit(resource.RLIMIT_STACK,(2**29,2**30))
    #R=dict()
    G=[[] for i in range(n+1)]
    R=[[] for i in range(n+1)]
    #G={i+1:[] for i in range(875714)}
    #R={i+1:[] for i in range(875714)}
    with open("SCC.txt") as f:
        for line in f:
            line=map(int,line.split())
            G[line[0]].append(line[1])
            R[line[1]].append(line[0])
    #print G
    end1=time.time()
    print "Done reading the input file"+str(end1-start)
    #print explored 
    DFSloop(R)
    end2=time.time()
    print "Done on reverse graph"+str(end2-start) 
    end3=time.time()
    DFSloop1(G)
    print "Done on forward graph"+str(end3-start)
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
