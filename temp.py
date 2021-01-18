#!/usr/bin/python3 
# Importing the 'cgi' module 

import cgi
from time import localtime 
import random

# function for create table and fill informations
def HTMLtable(templist):
    table = "<table style='width:50%'>" #config width of table
    table += "<tr><th>DAY</th><th>TIME</th><th>temp(C)</th></tr>"   # write head of table
    data = templist.split()
    day = data[0]
    time = data[1]
    temp = data[2]
    table = table+"\n<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(day,time,temp) # fill information in table
    table += "</table>"
    print(table)  

# This block setting style of table and show Hello Program!
print("Content-type: text/html\r\n\r\n") 
print("<html>")
print("<head>")
print("<style>")
print("table,th,td { border: 1px solid black; }")
print("</style>")
print("</head>")
print("<body>") 
print("<h1> Hello Program! </h1>")
print("<form action = 'temp.py' method = 'post'>")
print("<input type = 'radio' name = 'max-min' value = 'max-min' >max-min")
print("<input type = 'radio' name = 'min-max' value = 'min-max' >min-max") 

# Using the inbuilt method# Using the inbuilt methodsrw
form = cgi.FieldStorage() 
time = localtime()

if form.getvalue("name"):
    day = str(time.tm_mday) + "/" + str(time.tm_mon) + "/" + str(time.tm_year)  
    time = str(time.tm_hour) +":" + str(time.tm_min) + ":" + str(time.tm_sec)
    name = form.getvalue("name") 

# This block write file that contain day/month/year hour/miniute/second temperature
    f = open("demofile2.txt", "a")
    f.write(day+" "+time+" "+name+"\n")
    f.close()

# This block show information on browser
f = open("demofile2.txt", "r")
data_temp = f.read()
with open("demofile2.txt") as file_in:
    lines = []
    for line in file_in:      
        lines.append(line)
    Dic = {}
    sortList = []
    for temp in lines:
        data = temp.split()
        dayTime = data[0]+" "+data[1]
        Dic[str(dayTime)] = float(data[2])
        sortList.append(float(data[2]))
    sortList.sort()
    if form.getvalue('max-min'):
        sortList.reverse()
    for i in sortList:
        dt = list(Dic.keys())[list(Dic.values()).index(i)]
        tmp = str(dt)+" "+str(i)
        HTMLtable(tmp)
        del Dic[dt] 
f.close()
print("</body></html>") 

# create form that user can fill temperature
print("<form method='post' action='temp.py'>") 
print("<p>NUM: <input type='number' name='name'></p>") 
print("<input type='submit' value='Submit'>") 
print("</form>")
print("</body></html>") 

