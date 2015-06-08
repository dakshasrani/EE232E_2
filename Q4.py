# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 19:38:22 2015

@author: Mak
"""


import fileinput
from sets import Set

#Question 1
listoflists = []
alist=[]
i=0
with open('actor_movies.txt') as f:
   for l in f:
       alist= l.strip().split("\t\t")
       listoflists.append(alist)
       i=i+1
       if(i%10000==0):
           print(i)

           
i=0
alist=[]
with open('actress_movies.txt') as f:
   for l in f:
       alist= l.strip().split("\t\t")
       listoflists.append(alist)
       i=i+1
       if(i%10000==0):
           print(i)

#%% 
mamap={}        
count=0  
for l in listoflists:
    count=count+1
    if(count % 10000 == 0):
        print(count)
    for i in range(1,len(l)):
        if(l[i].replace(" ","") not in mamap):
            mamap[l[i].replace(" ","")]=Set([])            
        mamap[l[i].replace(" ","")].add(l[0].replace(" ",""))
    
        
#%%
i=0
for l in list(mamap.viewkeys()):
   if(len(mamap[l])<5):
       del mamap[l]
   i=i+1
   if(i% 10000 ==0):
       print(i)
       
#remove the null movie entry caused by actors without movies
     
del mamap[""]
       
#%%
mvmap={}
count=0
for l in list(mamap.viewkeys()):
    count=count+1
    if(count %10000 ==0):
        print(count)
    for i in mamap[l]:
        if(i.replace(" ","") not in mvmap):
            mvmap[i.replace(" ","")]=Set([])            
        mvmap[i.replace(" ","")].add(l.replace(" ",""))
        
    
#%%
        
cllistoflists = []
count=0
for l in list(mamap.viewkeys()):
    count=count+1
    if(count%10000 == 0):
        print(count)
    for k in mamap[l.replace(" ","")]:
        for m in mvmap[k]:
            if(l != m):
                clalist=[]
                temp=len(mamap[l].intersection(mamap[m]))
                if(temp>0):
                    clalist.append(l.replace(" ",""))
                    clalist.append(m)
                    den=len(mamap[l].union(mamap[m]))
                    weight=float(float(temp)/float(den))
                    clalist.append(weight)
                    cllistoflists.append(clalist)
#%%
i = 0
edgelist = Set([])
for l in cllistoflists:
    edgelist.add(l[0].replace(" ","")+' '+l[1].replace(" ","")+' '+str(l[2])+'\n')
    i=i+1
    if(i%10000==0):
        print(i)
   
#%%
i = 0
with open('temp2.txt', 'a') as export:
    for l in edgelist:       
        export.write(l)
        if(i%10000==0):
            print(i)
        i=i+1