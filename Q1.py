# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 16:36:50 2015

@author: Mak

"""
import fileinput
from sets import Set

#%%
#Question 1
listoflists = []
alist=[]
i=0
with open('actor_movies.txt') as f:
   for l in f:
       alist= l.strip().split("\t\t")
#       print l.strip().split("\t\t")
       i=i+1
       if(i%10000==0):
           print(i)
       if(len(alist)>10):
           listoflists.append(alist)
           
           
i=0
alist=[]
with open('actress_movies.txt') as f:
   for l in f:
       alist= l.strip().split("\t\t")
#       print l.strip().split("\t\t")
       i=i+1
       if(i%10000==0):
           print(i)
       if(len(alist)>10):
           listoflists.append(alist)
           
#%%
#Question 2 

movmap={} 
mamap={}        
count=0  
for l in listoflists:
    movmap[l[0]]=Set([])
    count=count+1
    for i in range(1,len(l)):
        movmap[l[0]].add(l[i])
        if(l[i] not in mamap):
            mamap[l[i]]=Set([])            
        mamap[l[i]].add(l[0])

cllistoflists = []
count=0
for l in listoflists:
    count=count+1
    if(count%10000 == 0):
        print(count)
    for k in movmap[l[0]]:
        for m in mamap[k]:
            if(m != l[0]):
                clalist=[]
                temp=len(movmap[l[0]].intersection(movmap[m]))
                if(temp>0):
                    clalist.append(l[0])
                    clalist.append(m)
                    weight=float(float(temp)/float(len(movmap[l[0]])))
                    clalist.append(weight)
                    cllistoflists.append(clalist)
           
           
           