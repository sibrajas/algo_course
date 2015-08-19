import time
maxInterval=10000
if __name__=="__main__":
    hashtab={}
    start=time.time()
    with open('algo1_programming_prob_2sum.txt') as fd:
    #with open('2sum_test1M.txt') as fd:
    #with open('test.txt') as fd:
        for line in fd:
            value=int(line)
            #print value
            key=value/maxInterval if value>=0 else -(-value/maxInterval)
            hashtab.setdefault(key,[]).append(value)
            #print line
    end=time.time()
    print end-start
    print "File loaded" 
    resultsum={}
    for key1 in sorted(hashtab.keys()):
        #print key1
        if key1>0:
            continue
        key2=[-key1-2,-key1-1,-key1,-key1+1]
        for val1 in hashtab[key1]:
            for key in key2:
                #try:
                if hashtab.has_key(key):
                    for val2 in hashtab[key]:
                        if abs(val1+val2)<=10000: # in set(range(-maxInterval,maxInterval+1)):
                            if val1!=val2:
                                #resultsum[val1+val2]=1
                                resultsum.setdefault(val1+val2,[]).append([val1,val2])
                #except KeyError:
                    #continue
    print len(resultsum)
    end1=time.time()
    print end1-start

