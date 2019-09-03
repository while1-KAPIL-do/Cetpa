#------------------------ Phone Directory Mangement System ------------------
print("\n"*3,"\t"*2,"Question\n\n"*1)

# create a phone directory
# 1. add valyue through user
# 2. Search by name
##############################################

def createPhoneDir(n):
    d={}
    for i in range(0,n):
        value = input("Name\t\t:")
        key = int(input("Phone no\t:"))
        d[key] = value
        print()
    return d
##############################################  
    
def searchByName(mydir,myname):
    b = True
    for number,name in mydir.items():
        if name == myname:
            b = False
            return number,name
    if b:
        print("Item is not Present in Dir...!")
##############################################  
    
def searchByNumber(mydir,mynum):
    b = True
    for number,name in mydir.items():
        if mynum == number:
            b = False
            return number,name
    if b:
        print("Item is not Present in Dir...!")
##############################################
        
def deleteByNumber(mydir,mynum):
     if mynum in mydir:
         mydir.pop(mynum)
         return mydir
     else:
         print("Item is not present in dir...!")
##############################################
        
def deleteByName(mydir,myname):
     for number,name in mydir.items():
        if myname == name:
            mydir.pop(number)
            return mydir
##############################################
        
def addItemInDir(mydir,name,number):
    mydir[number]=name
    return mydir
##############################################

def ViewAllContact(mydir):
    print("\n\n\t\tPHONE DIRECTORY\n")
    print("\nName\t:\tPhone\n")
    for number,name in mydir.items():
       print(name,"\t:\t",number)
##############################################


# Create Dir
mydir = createPhoneDir(int(input("Size : ")))

while True:
    print("\n\n\t\t\tMENU")
    print(" 1. Search by name")
    print(" 2. Search by number")
    print(" 3. Delete by name")
    print(" 4. Delete by number")
    print(" 5. Add item in phone dir ")
    print(" 6. View All Contacts")
    print(" 0. Exit\n")
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        # Search by name
        number,name = searchByName(mydir,input("Enter Name : "))
        print(name,"\t:",number)
    
    elif choice == 2:
       number,name = searchByNumber(mydir,int(input("Enter Number : ")))
       print(name,"\t:",number)
        
    elif choice == 3:
        mydir = deleteByName(mydir,input("Enter Name : "))
       
    elif choice == 4:
        # Delete by Name
        mydir = deleteByNumber(mydir,int(input("Enter Number : ")))
       
        
    elif choice == 5:
        mydir = addItemInDir(mydir,input("Enter Name : "),int(input("Enter Number : ")))
        
    elif choice == 6:
        ViewAllContact(mydir)
        
    elif choice ==0:
        print("End...")
        break
    else:
        print("Invalid choice...!")
