#!/usr/bin/python
import time 
import webbrowser
option= '''
print " press 1 : enter any string "
print " press 2 : enter any string "
print " press 3 : enter any string "
print " press 4 : enter current date and time   "
print " press 5 : open default web browser"
print " press 6 : All network ip  "
print " press 7 : enter domain and check owner "
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
else:
   print "no choice"
