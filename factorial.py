#!/usr/bin/python3 
import cgi
import time

print("Content-type: text/html\r\n\r\n") 
print("<html>")
form = cgi.FieldStorage()
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
    print("<p> Time : {} </p>".format(end - start))

print("<form method='post' action='factorial.py'>") 
print("<p>NUM: <input type='text' name='name'></p>")
print("<input type='submit' value='Submit'>") 
print("</form>")
print("</body></html>")