
# coding: utf-8

# In[4]:

class Treenode(object):
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def add_leftchild(self,obj):
        self.lchild=obj
    def add_rightchild(self,obj):
        self.rchild=obj
    def disproot(self):
        print self.data,
        if self.lchild:
            print self.lchild.data,
        else:
            print " ",
        if self.rchild:
            print self.rchild.data
        else:
            print " "
    def disp(self):
        q=[]
        q.append([None,"root",self])
        while len(q)!=0:
            parent,pos,node=q.pop(0)
            print parent,pos,node.data
            if node.lchild:
                q.append([node.data,"left",node.lchild])
            if node.rchild:
                q.append([node.data,"right",node.rchild])
    def maxsum(self,res):
        if self==None:
            return 0
        else:
            if self.lchild:
                [lsum,res]=self.lchild.maxsum(res)
            else:
                lsum=0
            if self.rchild:
                [rsum,res]=self.rchild.maxsum(res)
            else:
                rsum=0
            childsum=max(lsum,rsum)
            subtreesum=max(childsum+self.data,self.data)
            max_top=max(subtreesum,lsum+rsum+self.data)
            res=max(res,max_top)
            return [subtreesum,res]
        
if 0:            
    root=Treenode(10)
    l=Treenode(2)
    r=Treenode(10)
    r1=Treenode(1)
    l1=Treenode(20)
    r2=Treenode(-25)
    l3=Treenode(3)
    r3=Treenode(4)
    root.add_leftchild(l)
    root.add_rightchild(r)
    root.lchild.add_rightchild(r1)
    root.lchild.add_leftchild(l1)
    root.rchild.add_rightchild(r2)
    r2.add_leftchild(l3)
    r2.add_rightchild(r3)
    root.disp()
    print "Result is "
    [a,x]=root.maxsum(0)
    print x


#root.rchild.disp()
#root.lchild.disp()

