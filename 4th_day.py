#---------------------------------- Lambda Function ---------------------------
#1
double = lambda x:x*2
print(double(2))
#2
qv = lambda x:x*x*x
print(qv(2))

#---------------------------------- Filter ------------------------------------
li = [1,2,4,6,8,9,9,5,3,2,4]
fl = list(filter(lambda x:(x%2!=0),li))
print(fl)

#---------------------------------- Map ---------------------------------------


s = 1
nl=[]
for i in li:
    s=s+i
    nl.append(s)
    
print(s,nl)

from functools import reduce
li = [1,2,4,6,8,9,9,5,3,2,4]
fl = (reduce(lambda x,y:x+y,li))
print(fl)

