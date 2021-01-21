#!/usr/bin/python3 
import cgi
import time

print("Content-type: text/html\r\n\r\n") 
print("<html>")
form = cgi.FieldStorage()

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("<p>Time Lapsed = {0}:{1}:{2}</p>".format(int(hours),int(mins),sec))

def factorial(num):
    result = 1
    for i in range(2,num+1):
        result *= i
    return result
print("<body>") 
if form.getvalue('name'):
    num = form.getvalue('name')
    start = time.time()
    answer = factorial(int(num))
    end = time.time()
    print("<p> Result : {} </p>".format(answer))
    time_convert(end-start)

print("<form method='post' action='factorial.py'>") 
print("<p>NUM: <input type='text' name='name'></p>")
print("<input type='submit' value='Submit'>") 
print("</form>")
print("</body></html>")