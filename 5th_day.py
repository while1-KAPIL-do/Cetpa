#------------------------------ File Handeling --------------------

# Create
f = open("G:/MOVIES/BOLLYWOOD/abc.txt","x")
f.write("")
f.close()

# Write
f = open("G:/MOVIES/BOLLYWOOD/abc.txt","w")
f.write("nnn")
f.close()

# Apend
f = open("G:/MOVIES/BOLLYWOOD/abc.txt","a")
f.write("Apended values")
f.close()

# Read
f = open("G:/MOVIES/BOLLYWOOD/abc.txt","r")
print(f.read())
f.close()

# rb / wb
f = open("G:/FM_001/DSC_0667.jpg","rb")
d = open("G:/FM_001/new.jpg","wb")
for i in f:
     d.write()
f.close()
d.close()

# rb / ab
f = open("G:/FM_001/DSC_0667.jpg","rb")
d = open("G:/FM_001/new.jpg","ab")
for i in f:
     d.write()
f.close()
d.close()


# Read CSV file
import pandas as pd
data = pd.read_csv("C:/Users/machine_learning/Desktop/Machine Learning A-Z/Part 1 - Data Preprocessing/Data.csv")
data

#------------------------------- Exception Han --------------------------------
# try , except , else , finally
try :
     int(input("Enter int :"))
except:
     print("Except block...")
finally:
     print("Finally block---")

# exception handeling in file handeling
try :
     f = open("G:/MOVIES/BOLLYWOOD/abc.txt","r")
     print(f.read())
     
except :
     print("File not found...!")
finally:
     f.close()
     
# Print Error
import sys
l = ['a',0,2]
c=0
for each in l:
     try:
          c = 2/each
          print(c)
          break
     except:
          print(sys.exc_info()[0])

          
# Date Time
          
import datetime
datetime_obj = datetime.datetime.now()
print(datetime_obj)

'''
date Class
time Class


'''  
from datetime import datetime, date, timedelta
t1 = date(year = 8769,month = 6, day =12)
t2 = date(year = 8769,month = 6, day =12)  
t3 = t1 - t2
print(t3)

t4 = datetime(year = 8769,month = 6, day =12,hour = 7,minute = 4, second = 33)
t5 = datetime(year = 2009,month = 4, day =2,hour = 4,minute = 4, second = 44)
t6 = t4-t5
print(t6)
print(type(t3))

t7 = timedelta(days =12,hours = 7,minutes = 4, seconds = 33)
t8 = timedelta(weeks = 5, days =2,hours = 4, seconds = 44)
t9 = t7-t8
print(t9)


















