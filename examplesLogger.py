# -*- coding: utf-8 -*-
import os, sys, subprocess

cwd = os.getcwd();
logDir = cwd + "/../../build/logs";
rootUrl = "http://autotest.bioeng.auckland.ac.nz/opencmiss-build/"

if not os.path.isdir(logDir):
  os.mkdir(cwd + "/../../build")
  os.mkdir(logDir);
os.putenv('HOME', '/home/autotest')
f = open(logDir+'/build.log',"r")
logs = f.readlines()
f.close()
os.remove(logDir+'/build.log')

def logExample(path) :
   global logDir,logs;
   intellibrarylog=[]
   gnulibrarylog=[]
   intelexamplelog=[]
   gnuexamplelog=[]
   inteltestlog=[]
   gnutestlog=[]
   for log in logs :
     if log.startswith('intel_library_build') :
       intellibrarylog=log.split('|');
     if log.startswith('gnu_4.4_library_build') :
       gnulibrarylog=log.split('|');
#     if log.startswith('intel_'+path+'_build') :
#       intelexamplelog=log.split('|');
     if log.startswith('gnu_4.4_'+path+'_build') :
       gnuexamplelog=log.split('|');
#     if log.startswith('intel_'+path+'_test') :
#       inteltestlog=log.split('|');
     if log.startswith('gnu_4.4_'+path+'_test') :
       gnutestlog=log.split('|');
   newDir = logDir;
   for folder in path.split('/') :
     newDir = newDir + '/' + folder
     if not os.path.isdir(newDir):
       os.mkdir(newDir)
   os.chdir(logDir+"/"+path)
   if os.path.exists(newDir + "/history.html") :
     os.remove(newDir + "/history.html")
   f = open(newDir + "/history.html","w")
   f.write("<h2>Testing Status:</h2>\n")
   f.write("<table><tr><td/><td>Status</td><td>Latest Execution Time</td></tr>\n")
   f.write("<tr><td><b>Intel Build</b></td><td/><td/></tr>")
   f.write("<tr><td><a href='"+rootUrl+"logs_x86_64-linux/build-intel'>OpenCMISS Library</a></td>")
   if(intellibrarylog[1].startswith('success')) :
     f.write("<td><font color='green'>Success</font></td>")
   else :
     f.write("<td><font color='red'>Fail</font></td>")
   f.write("<td>"+intellibrarylog[2]+"</td></tr>")
#   f.write("<tr><td><a href='"+rootUrl+"logs_x86_64-linux/"+path+"/build-intel'>Example Build</a></td>")
#   if(intelexamplelog[1].startswith('success')) :
#     f.write("<td><font color='green'>Success</font></td>")
#   else :
#     f.write("<td><font color='red'>Fail</font></td>")
#   f.write("<td>"+intelexamplelog[2]+"</td></tr>")
#   if(len(inteltestlog)>1) :
#     f.write("<tr><td><a href='"+rootUrl+"logs_x86_64-linux/"+path+"/test1-intel'>Example Test</a></td>")
#     if(inteltestlog[1].startswith('success')) :
#       f.write("<td><font color='green'>Success</font></td>")
#     else :
#       f.write("<td><font color='red'>Fail</font></td>")
#     f.write("<td>"+inteltestlog[2]+"</td></tr>")
   
   f.write("<tr><td><b>GNU Build</b></td><td/><td/></tr>")
   f.write("<tr><td><a href='"+rootUrl+"logs_x86_64-linux/build-gnu_4.4'>OpenCMISS Library</a></td>")
   if(gnulibrarylog[1].startswith('success')) :
     f.write("<td><font color='green'>Success</font></td>")
   else :
     f.write("<td><font color='red'>Fail</font></td>")
   f.write("<td>"+gnulibrarylog[2]+"</td></tr>")
   f.write("<tr><td><a href='"+rootUrl+"logs_x86_64-linux/"+path+"/build-gnu_4.4'>Example Build</a></td>")
   if(gnuexamplelog[1].startswith('success')) :
     f.write("<td><font color='green'>Success</font></td>")
   else :
     f.write("<td><font color='red'>Fail</font></td>")
   f.write("<td>"+gnuexamplelog[2]+"</td></tr>")
   if(len(gnutestlog)>1) :
     f.write("<tr><td><a href='"+rootUrl+"logs_x86_64-linux/"+path+"/test1-gnu_4.4'>Example Test</a></td>")
     if(gnutestlog[1].startswith('success')) :
       f.write("<td><font color='green'>Success</font></td>")
     else :
       f.write("<td><font color='red'>Fail</font></td>")
     f.write("<td>"+gnutestlog[2]+"</td></tr>")
   
   f.write("</table>")
   f.close()
   return;

for log in logs :
  if log.startswith('gnu_4.4_') :
    paths=log.split('|');
    if(paths[0].endswith('_build') and (not log.startswith('gnu_4.4_library_build')))  :
      logExample(path=paths[0].replace('gnu_4.4_','').replace('_build',''));
