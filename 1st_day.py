#---------------------------- String ----------------------------------
print("\n"*2)
print("\t"*2,"String")
print("\n"*1)

s = "Noida electronic City 18"

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.islower())
print(s.isupper())
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())

print(len(s))
print(min(s))
print(max(s))

# ASCI 
print(ord('a'))
print(chr(97))

for i in range(48,58):
    print(chr(i),end=",")
print()
for i in range(97,123):
    print(chr(i),end=",")
print()
for i in range(65,91):
    print(chr(i),end=",")
print()

# split
print(s[10:19])
print(s.split())
print(s.count("a"))


#-------------------------------- Tuple --------------------------------
print("\n"*3,"\t"*2,"Operators\n\n"*1)

t = (1,2,3,4,5,'a',"kapil",True,False)
print(t)
print(type(t))
print(t.count("a"))
print(len(t))
# if tuple have same data type then Max and Min function will work
t = (1,2,3,4,5)
print(min(t))
print(max(t))


t = (1,2,3,4,[3,4])
t[4][0] = 3
print(t)


#-------------------------------- List --------------------------------
print("\n"*3,"\t"*2,"Operators\n\n"*1)

l = [1,2,3,4,5,'a',"kapil",True,False]
print(l)
print(type(l))
print(l.count("kapil"))
print(len(l))

# if tuple have same data type then Max and Min function will work
l = [1,2,3,4,5]
print(min(l))
print(max(l))

# ----- Operations----
print("Original : ",l)

# appeds()
l.append(6)
print("append(6) : ",l)

# insert()
l.insert(3,3.5)
print("insert(3.5 at 3rd position) : ",l)

# pop()
print("poped item : ",l.pop())
print("pop : ",l)

# remove()
print("remove action(None/exeption) : ",l.remove(3.5))
print("after remove : ",l)

# reverse()
l.reverse()
print(l)

# sort()
l.sort()
print(l)

# pop(index)
l.pop(3)
print(l)

# del
del l[1:3]
print(l)

# --------------------------------- Question 1 ----------------------------
print("\n"*3,"\t"*2,"Operators\n\n"*1)


L = ['java','data science','python','ML','AI','DL','c','c++','AWS cloud']
print("List : ",L)

#1
L.insert(7,'c#')
print('\n\n#1 insert c# b/n c and c++ : ',L)

#2
L.append('cloud management')
print('\n\n#2 append cloud management : ',L)

#3
print('\n\n#3 Saprate Technologies : ',L)
print("Languages : ",L[0],L[2],L[6],L[7],L[8])
print("Technologies : ",L[1],L[3],L[4],L[5],L[9],L[10])

#4
L.remove("c")
L.remove("c++")
print("\n\n#4 remove c and c++ : ",L)

#5
L.sort()
print("\n\n#5 sort the list : ",L)

#6
print("\n\n#6 find position of data science : ",L.index("data science"))
      
      
#-------------------------------- SET (Mutable) -----------------------------------
print("\n"*3,"\t"*2,"Operators\n\n"*1) 

s1 = {1,2,3,4,5,33,45,11,23,6}
s2 = {1,76,4,5,66,6,55,4,3,2}
print("OR / Uniun / all elemets '|' : ",s1|s2)
print("AND / Intersaction /comman  '&' : ",s1&s2)
print("Symmitric values : ",s1^s2)
print(" : ",s1<s2)
print(" : ",s1>s2)
print("Type check : ",type(s1))

#-------------------------------- Frozen SET (Imutable) -----------------------------------
print("\n"*3,"\t"*2,"Operators\n\n"*1) 

f = frozenset("kapil")
print(f)
f1 = frozenset([1,2,3,4,5])
print(f1)
f2 = frozenset([2,6,9,0,4,5])
print(f2)

print(s1.union(s2))
print(s1.intersection(s2))


#-------------------------------- Nested List -----------------------------------
print("\n"*3,"\t"*2,"Operators\n\n"*1) 

L = [[1,2,3],['a','b','c'],['A','B','C'],[1.1,2.2,3.3]]

for i in L:
    for j in i:
        print(j,sep=",",end="")
    print()








