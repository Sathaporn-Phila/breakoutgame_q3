#!/usr/bin/python3 
# Importing the 'cgi' module 

import cgi 

def HTMLtable(templist):
    table = "<table style='width:50%'>"
    table += "<tr><th>DAY</th><th>TIME</th><th>temp</th></tr>"
    for i in templist:
        table = table+"\n<tr><td>DAY</td><td>TIME</td><td>"+str(i)+"</td></tr>"
    table += "</table>"
    print(table)  


print("Content-type: text/html\r\n\r\n") 
print("<html>")
print("<head>")
print("<style>")
print("table,th,td { border: 1px solid black; }")
print("</style>")
print("</head>")
print("<body>") 
print("<h1> Hello Program! </h1>") 
# Using the inbuilt methodsrw



form = cgi.FieldStorage() 
if form.getvalue("name"): 
    name = form.getvalue("name") 
    f = open("demofile2.txt", "a")
    f.write(name+ " C\n")
    f.close()
    f = open("demofile2.txt", "r")
    day = "today"
    time = "is time"
    temp = f.read()
    print("<pre>"+temp+"</pre><br>") 
    with open("demofile2.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    HTMLtable(lines)
    f.close()

else:
    f = open("demofile2.txt", "r")
    day = "today"
    time = "is time"
    temp = f.read()
    print("<pre>"+temp+"</pre><br>") 
    with open("demofile2.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    HTMLtable(lines)
    f.close()

    # print("<table style='width:50%'>")
    # print("<tr>")
    # print("<th>DAY</th><th>TIME</th><th>TEMP</th>")
    # print("</tr>")

    # for i in f:
    #     print("<tr>")
    #     print("<td>"+day+"</td>")
    #     print("<td>"+day+"</td>")
    #     print("<td>"+day+"</td>")
    #     print("</tr>")
    # print("</table>")

    # print("<script>")
    # print(" document.write('<table style='width:50%;'>') ")
    # print("document.write('<tr>')")
    # print("document.write('<th>DAY</th><th>TIME</th><th>TEMP</th>')")
    # print("document.write('</tr>')")
    # print("document.write('</table>')")
    # print("</script>")

    

print("</body></html>") 

# Using HTML input and forms method 
print("<form method='post' action='w.py'>") 
print("<p>NUM: <input type='text' name='name'></p>") 
print("<input type='submit' value='Submit'>") 
print("</form>") 

