#!/usr/bin/python3 
# Importing the 'cgi' module 
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<p>%s</p>"% (message,))
print("</body>")
print("</html>")
