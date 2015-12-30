
# coding: utf-8

# In[56]:

from Treenode import Treenode
memo=[0 for i in range(1,30)]
print memo

def CountBinaryTrees(n):
    if n==1 or n==0:
        return 1
    else:
        sum=0
        for k in range(1,n+1):
            if memo[k-1]==0:
                memo[k-1]=CountBinaryTrees(k-1)
            left=memo[k-1]
            if memo[n-k]==0:
                memo[n-k]=CountBinaryTrees(n-k)
            right=memo[n-k]
            sum=sum+(left*right)
        memo[n]=sum
        return sum
        
for i in range(2,10):
    x=CountBinaryTrees(i)
    print x
#These are the catalan numbers 
#calculated with fact(2n)/(fact(n)*fact(n+1))
print memo


# In[55]:

def countbstdynamicprog(n):
    mat=[[0 for i in range(n+1)] for i in range(n+2)]
    for i in range(n+2):
        mat[i][0]=1
    for i in range(1,n+1):
        sum=0
        for j in range(1,i+1):
            mat[j][i]=mat[n+1][j-1]*mat[n+1][i-j]
            sum=sum+mat[j][i]
        mat[n+1][i]=sum
    print mat[n+1][1:]
def countbst(n):
    mat=[[0 for i in range(n+1)] for i in range(n+1)]
    catalan=[0 for i in range(n+1)]
    catalan[0]=1
    for i in range(n+1):
        mat[i][0]=1
    for i in range(1,n+1):
        sum=0
        for j in range(1,i+1):
            mat[j][i]=catalan[j-1]*catalan[i-j]
            sum=sum+mat[j][i]
        catalan[i]=sum
    print catalan[1:]    

countbst(10)
countbstdynamicprog(10)  #Damn how does this work in ipython


# In[33]:

for i in range(5):
    print i

