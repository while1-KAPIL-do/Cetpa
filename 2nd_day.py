#---------------------------------- Dictonary ---------------------------------
print("\n"*3,"\t"*2,"Dictonary\n\n"*1)


d = {"k007":"007","name":"Kapil","dob":"07/09/1996","rollno":"0904cs161006"}
print("name\t",d["name"])
print("dob\t",d["dob"])
print("rollno\t",d["rollno"])
print()

# list of keys and values
print(d.keys())
print(d.values())
print()

#sort
print(sorted(d.keys()))    
print(sorted(d.values()))
print()


#user define input
id = "k007" # str(input("enter your id\t"))
ps = "007" #str(input("enter your pass\t"))

if id in d and d[id] == ps:
    print("Id is valid")
else:
    print("Id is invalid ",d[id],ps)
print()


# pop
print(d.pop("dob"))
print(d)



#---------------------------------- Operators ---------------------------------
print("\n"*3,"\t"*2,"Operators\n\n"*1)

import operator
print("pow(5,5)\t\t",operator.pow(5,5))
print("abs(33)\t\t",operator.abs(33))
print("add(2,3)\t\t",operator.add(2,3))
print("eq(2,2)\t\t",operator.eq(2,2))
print("mod(23,8)\t\t",operator.mod(23,8))
print("neg(66)\t\t",operator.neg(66))
print("xor(22,55)\t\t",operator.xor(22,55))
print("sub(55,77)\t\t",operator.sub(55,77))
print()
# != < > == >= <= and or not 

# identity operator--> is / is not
print( 2 is 2)
print( 2 is not 2)




#---------------------------------- Operator Overloading ---------------------------------
print("\n"*3,"\t"*2,"Operator Overloading\n\n"*1)

# + (Strings)
x = "3" #input()
y = "23" #input()
z = x+y
print(z)
print()

# + (Interger/float)
x = 23  #int(input())
y = 32  #int(input())
z = x+y
print(z)
print()

# * behave as like a loop only for Tuples
t = (1,)
d = t*5
print(d) 



#---------------------------------- Replcement any() / all() ---------------------------------
print("\n"*3,"\t"*2,"Replcement\n\n"*1)
# any() all()
# single argument

print("any([False,False,False,False,False,True,False,False])\t",any([False,False,False,False,False,True,False,False]))
print("all([True,False,True,False,True,False,True,False])\t",all([True,False,True,False,True,False,True,False]))
print("all([True,True,True,True,True,True,True,True,True])\t",all([True,True,True,True,True,True,True,True]))


#---------------------------------- Data Frams ---------------------------------
print("\n"*3,"\t"*2,"Data Frams\n\n"*1)

import pandas as pd

d = {"name":["a","b","c"],"class":[1,2,3]}
df= pd.DataFrame(d)
print(df)
print()

print(type(df))



#---------------------------------- Type Casting ---------------------------------
print("\n"*3,"\t"*2,"Type Casting\n\n"*1)

# dict -> tuple 
s = dict(((1,2),(3,4)))
print(s) 

# float -> int
f = 33.376
i = int(f)
print(i)



#---------------------------------- Question ---------------------------------
print("\n"*3,"\t"*2,"Question\n\n"*1)

'''
l = list()
n = int(input("Enter the size of list : "))
for i in range(0,n):
    l.append(int(input()))
print(l)
'''
l = [11,22,66,88,44,77,99,33]
while True:
    print("\n\n\t\t\tMENU")
    print("\tL = ",l,end="\n\n")
    print(" 1. Append")
    print(" 2. Reverse")
    print(" 3. sort")
    print(" 4. insert")
    print(" 5. remove")
    print(" 6. delete")
    print(" 7. pop")
    print(" 8. pop(index)")
    print(" 9. count")
    print("10. Index")
    print(" 0. Exit\n")
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        l.append(int(input("Enter Value to append : ")))
        print("Updated list : ",l)
    
    elif choice == 2:
        l.reverse()
        print("Updated list : ",l)
    
    elif choice == 3:
        l.sort()
        print("Updated list : ",l)
    
    elif choice == 4:
        l.insert(int(input("Enter a postion :")),int(input("Enter Value :")))
        print("Updated list : ",l)
        
    elif choice == 5:
        l.remove(int(input("Enter Remove item :")))
        print("Updated list : ",l)
        
    elif choice == 6:
        sp = int(input("Enter the postion where you want to start deleting"))
        ep = int(input("Enter the postion where you want to end deleting"))
        del l[sp:ep]    
        print("Updated list : ",l)
        
    elif choice == 7:
        print("Popedm item : ",l.pop())
        print("Updated list : ",l)
    
    elif choice == 8:
        p = int(input("Enter position you want to delete : "))
        print("Popedm item : ",l.pop(p))
        print("Updated list : ",l)
    
    elif choice == 9:
        print("Repeatation : ",l.count(int(input("Enter the item you want to check : "))))
        print("Updated list : ",l)
    
    elif choice == 10:
        print("Index is : ",l.index(int(input("Enter the Value you want to check index : "))))
        print("Updated list : ",l)
    elif choice ==0:
        print("End...")
        break
    else:
        print("Invalid choice...!")
















