import sys,resource
import time
def DFS(G,s,finishingtime):
    if s in G.keys():
        for val in G[s]:
            if val not in explored:
                explored.append(val)
                finishingtime=DFS(G,val,finishingtime)
        #f_times[s]=finishingtime
        f_times[finishingtime]=s
        finishingtime=finishingtime+1
    return finishingtime

def DFSloop(G):
    finishingtime=1
    for x in G.keys():
        #print str(x)+" key"
        if x not in explored:
            finishingtime=DFS(G,x,finishingtime)
    explored[:]=[]

def DFS_SCC(G,i,lead):
    explored.append(i)
    #leader[i]=lead
    count_lead[lead]+=1
    if i in G.keys():
        for val in G[i]:
            if val not in explored:
                DFS_SCC(G,val,lead)
    return

def DFSloop1(G):
    lead=-1
    for node_ftime in reversed(sorted(f_times.keys())):
        #print str(node_ftime)+" value "+" Node "+str(f_times[node_ftime])
        if f_times[node_ftime] not in explored:
            lead=f_times[node_ftime]
            count_lead[lead]=0
            DFS_SCC(G,f_times[node_ftime],lead)
    explored[:]=[]
    
if __name__=='__main__':
    start=time.time() 
    G={}
    f_times={}
    #leader={}
    count_lead={}
    explored=[]
    sys.setrecursionlimit(10**6)
    resource.setrlimit(resource.RLIMIT_STACK,(2**29,2**30))
    R=dict()
    G={i+1:[] for i in range(8)}
    R={i+1:[] for i in range(8)}
    #G={i+1:[] for i in range(875714)}
    #R={i+1:[] for i in range(875714)}
    with open("SCC1.txt") as f:
        for line in f:
            line=map(int,line.split())
            #if line[0] in adjlist:
            G[line[0]].append(line[1])
            R[line[1]].append(line[0])
            #else:
            #adjlist[line[0]]=[line[1]]
    #print G
    print "Done reading the input file" 
    DFSloop(R)
    #print f_times
    DFSloop1(G)
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
