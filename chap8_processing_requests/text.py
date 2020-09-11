import cgi

data = cgi.FieldStorage()

if data.getvalue("Future Web"):
    text=data.getvalue("Future Web")
else:
    text="Please enter text"

print("Content-type:text/html\r\n\r\n")
print("<!DOCTYPE HTML>")
print('<html lang="en">')
print("<head>")
print('<meta charset="UTF-8>"')
print('<title> Python Response </title>')
print('</head>')
print('<Body>')
print('<h1>',text,'</h1>')
print('<a href="text.html">Back</a>')
print('</body>')
print('</html>')