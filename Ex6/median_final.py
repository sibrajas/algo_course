from heap import Heap,MaxHeap
import numpy as np 
if __name__=='__main__':
    h=Heap()
    H=MaxHeap()
    median=[]
    rootindex=0
    with open('Median.txt') as fd:
    #with open('test10.txt') as fd:
        no=int(fd.readline())
        median.append(no)
        H.insert(no)
        no1=int(fd.readline())
        h.insert(no1)
        if no1>no:
            median.append(no)
        else:
            h.heap[0],H.heap[0]=H.heap[0],h.heap[0]
            median.append(no1)
        print median

        for line in fd:
	    no=int(line)
            if no<=H.heap[0]:
                H.insert(no)
            elif no>h.heap[0]:
                h.insert(no)
            else:
                H.insert(no)

            if len(H.heap)-len(h.heap)>1:
                reins=H.extractmax()
	        h.insert(reins)
            elif len(h.heap)>len(H.heap):
                reins=h.extractmin()
                H.insert(reins)

            tempmedian=H.heap[0]
#            print "Max and min "+str(tempmedian)
#            print H.heap
#            print h.heap
            print tempmedian
	    median.append(tempmedian)
    print sum(median)%(10000)
