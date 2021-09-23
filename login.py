#!/usr/bin/env python3
import cgi, cgitb, os
from templates import secret_page, after_login_incorrect
import secret

form = cgi.FieldStorage()

username_field = form.getvalue("username")
password_field = form.getvalue("password")

if username_field == secret.username and password_field == secret.password:
    print("Set-Cookie: dbecerra = YEP\r\n")
    logged_in = True
else: 
    logged_in = False

print("Content-type: text/html")
print()
# print("<body>")
# print(f"<p> Username: {username_field} </p>")
# print(f"<p> Password: {password_field} </p>")
# print("</body>")


cookies = os.environ.get('HTTP_COOKIE').split(";")
for c in cookies: 
    try:
        key, value = c.split("=")
        key, value = key.strip(), value.strip()
        if key=="dbecerra" and value=="YEP":
            logged_in = True
    except:
        pass


if logged_in: 
    print(secret_page(secret.username, secret.password))
else:
    print(after_login_incorrect())