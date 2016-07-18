#!/usr/bin/python
import sys
import time
import fnmatch
import os
import re
import time
import re
from subprocess import call
from xml.dom.minidom import parseString

print " ______     __     ______   __         __  __     ______     ______     ______    "
print "/\  ___\   /\ \   /\__  _\ /\ \       /\ \_\ \   /\___  \   /\  ___\   /\  == \   "
print "\ \ \__ \  \ \ \  \/_/\ \/ \ \ \____  \ \____ \  \/_/  /__  \ \  __\   \ \  __<   "
print " \ \_____\  \ \_\    \ \_\  \ \_____\  \/\_____\   /\_____\  \ \_____\  \ \_\ \_\ "
print "  \/_____/   \/_/     \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/ /_/ "
print "#####################################################################################"
print "#                                                                                   #"
print "#          Credits: Sudhanshu Chauhan, Nutan Kumar Panda, Shubham Mittal            #"
print "#                                                                                   #"
print "#####################################################################################"

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

sys.stdout = Logger()

count=0
b = raw_input("Enter Your Git File Name: ")
print ""
print ""
print "Test started for "+b
if os.name == 'posix':
  call(['unzip',b])
else:
  print "This is not made for Windows!!!"
flist=[]
dirp=b.replace(".zip","")
rootpath="./"+dirp
ip = re.compile('((?:\d{1,3}\.){3}\d{1,3})')
email=re.compile('([\w.]+)@([\w.]+)')
# Add your keywords that you want to search in the codebase below
simlist=["pwlist","sql","dbconnect","dbname","username","pass","passwd","pwd","user","IMEI","connecTodb","dbname","server","API", "apikey","api","ftp:"]
relist=[ip,email]
for path,name,fname in os.walk(rootpath):
 for fn in fname:
     q=path+"/"+fn
     flist.append(q)
# Add the file extentions you want to skip
extrm=['.sh','.txt']
for sl in simlist:
 relist.extend([re.compile(sl)])

for fl in flist:
   if any(ext in fl for ext in extrm):    
    count=0 
    for line in open(fl, "r").readlines():
      count=count+1
      for lv in relist:
        match = lv.findall(line, re.IGNORECASE)
        for mat in match: 
          print "" 
          print 'File: ',fl
          print 'String ',"'",mat,"'",'at line number',count 
          print 'Line: ',line
             
print ""
print ""
print ""
print ""
print "-----------------------------------------------------------------------------------------------------"
print "Test Completed for "+b
print "-----------------------------------------------------------------------------------------------------"
print ""
print ""
