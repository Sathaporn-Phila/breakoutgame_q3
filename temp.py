#!/usr/bin/python3 
# Importing the 'cgi' module 

import cgi,csv
from time import localtime 

# function for create table and fill informations

def HTMLtable(type_sort):
    table = "<table style='width:50%'>" #config width of table
    table += "<tr><th>DAY</th><th>TIME</th><th>temp(C)</th></tr>"   # write head of table
    dicttemp = {}
    with open("demofile2.csv") as file_in:
        reader = csv.reader(file_in)
        for row in reader:
            daytime = str(row[0])+" "+str(row[1])
            temp = str(row[2])
            dicttemp[daytime] = float(temp)
        if type_sort == 'non-reverse' :
            sortTemp = sorted(dicttemp.values())
        elif  type_sort == 'reverse':
            sortTemp = sorted(dicttemp.values(),reverse=True)
        else:
            sortTemp = list(dicttemp.values())
        for i in sortTemp:
            datas = get_key(i,dicttemp).split()
            day = datas[0]
            time = datas[1]
            table = table+"\n<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(day,time,str(i)) # fill information in table
            del dicttemp[get_key(i,dicttemp)]
        table += "</table>"
        print(table)

def get_key(val,dic):
    for key, value in dic.items():
        if val == value:
            return key
    

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

# Using the inbuilt method# Using the inbuilt methodsrw
form = cgi.FieldStorage()

time = localtime()
if form.getvalue("name"):
    day = str(time.tm_mday) + "/" + str(time.tm_mon) + "/" + str(time.tm_year)  
    time = str(time.tm_hour) +":" + str(time.tm_min) + ":" + str(time.tm_sec)
    name = form.getvalue("name") 

# This block write file that contain day/month/year hour/miniute/second temperature
    with open("demofile2.csv", "a") as f:
        writer = csv.writer(f) 
        writer.writerow([day , time , name])
    

type_sort = form.getvalue("sort")
# This block show information on browser
HTMLtable(type_sort)


# create form that user can fill temperature
print("<form method='post' action='temp.py'>") 
print("<p>NUM: <input type='text' name='name'></p>")
print("<input type='radio' name='sort' value='non-reverse'>")
print("<label for='non-reverse'>Non-reverse</label>")
print("<input type='radio' name='sort' value='reverse'>")
print("<label for='reverse'>reverse</label>")  
print("<input type='submit' value='Submit'>") 
print("</form>")
print("</body></html>") 