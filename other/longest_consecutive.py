from heap import MaxHeap
arr=[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
arr=[1, 9, 3, 10, 4, 20, 2]
arrlength=len(arr)
h=MaxHeap()
count=1 if arrlength>0 else 0
cons=[]
maxcount=count
while len(arr)>0:
    element=arr.pop()
    h.insert(element)
maxi=h.extractmax()
cons.append(maxi)
new=0
for i in range(arrlength-1):
    sec_maxi=h.extractmax()
    if sec_maxi==maxi-1:
        count+=1
        if count>maxcount:
            maxcount=count
        if new==1:
            cons.append(maxi)
            new=0
        cons.append(sec_maxi)
    else:
        count=1
        new=1
        cons=[]
    maxi=sec_maxi
print maxcount
print cons
