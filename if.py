#!/usr/bin/python
import time
print " press 1: "
print " press 2: "   
ch =int(raw_input("enter the choice"))
if ch==1:
   print"execute me"
elif ch==2 :
 print time.ctime() 
else:
   print"no chance"

