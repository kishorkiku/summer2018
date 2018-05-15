#!/usr/bin/python
import time 
import webbrowser
print "MENU LIST"
option= '''
print " press 1 : To  enter any string - split each word and search on google "
print " press 2 : To  enter any string - split each word and search on google find URL "
print " press 3 : To  enter any string - split each word and search on google and find  images answer  "
print " press 4 : current time and date "
print " press 5 : open default web browser"
print " press 6 : All network ip  "
print " press 7 : enter domain and check owner ,email, contact "
'''
print option

ch =raw_input("enter the choice")
if ch=='1':
    search_data=raw_input("enter data")
    final_data=search_data.strip()
    # above removing leading and trailing data
    done_data=final_data.split()
    # spliting each word by space
    for i in done_data:
    	webbrowser.open_new_tab('https://www.google.com/search?q='+i)
elif ch=='2':
      print ""

elif ch=='3':
     search_data=raw_input("enter data")
     final_data=search_data.strip()
    # above removing leading and trailing data
     done_data=final_data.split()
    # spliting each word by space
     for i in done_data:
    	  webbrowser.open_new_tab('https://www.google.co.in/search?q='+i+'&source=lnms&tbm=isch')

elif ch=='4':
      print time.ctime()
elif ch=='5':
      webbrowser.open_new_tab('https://www.google.co.in')
elif ch=='6':
     print " "
elif ch=='7':
   print ""
else:
   print "no choice"
