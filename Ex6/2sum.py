if __name__=="__main__":
    hashtab={}
    with open("test.txt") as fd:
        for line in fd:
            line=line.strip()
            line=int(line)
            hashtab[line]=1
            #print line
    print 'File loaded' 
    totcount=0
    for t in range(-10000,10001):
        for line in hashtab.keys():
            #try:
                #if hashtab[t-line]:
            if hashtab.has_key(t-line):
                if t-line != line:
                    #print line,t-line
                    totcount+=1
		    print t
                    break
            else:
                    continue
            #except KeyError:
                #continue
    print totcount        

