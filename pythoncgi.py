#!/usr/bin/python3 
# Importing the 'cgi' module 
import cgi 

print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
print("<h1> Hello Program! </h1>") 
# Using the inbuilt methods 

form = cgi.FieldStorage()
if form.getvalue("name"): 
	name = form.getvalue("name") 
	print("<h1>Hello" +name+"! Thanks for using my script!</h1><br>") 
if form.getvalue("happy"): 
	print("<p> Yayy! I'm happy too! </p>") 
if form.getvalue("sad"): 
	print("<p> Oh no! Why are you sad? </p>") 
if form.getvalue('maths'):
   math_flag = "ON"
else:
   math_flag = "OFF"

if form.getvalue('physics'):
   physics_flag = "ON"
else:
   physics_flag = "OFF"



# Using HTML input and forms method 
print("<form method='post' action='pythoncgi.py'>") 
print("<p>Name: <input type='text' name='name' /></p>") 
print("<input type='checkbox' name='happy' /> Happy") 
print("<input type='checkbox' name='sad' /> Sad") 
 
print("<br><h1>Checkbox - Third CGI Program</h1>")
print("<h2> CheckBox Maths is : %s </h2> "% math_flag)
print("<h2> CheckBox Physics is : %s </h2>" % physics_flag)
print("<input type = 'radio' name = 'subject' value = 'maths' /> Maths")
print("<input type = 'radio' name = 'subject' value = 'physics' /> Physics")
print("<input type = 'submit' value = 'Select Subject' />")
print("</form>")
######################################################################



#https://www.geeksforgeeks.org/cgi-programming-python/





