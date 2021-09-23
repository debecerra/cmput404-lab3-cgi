#!/usr/bin/env python3
import os
from templates import login_page, after_login_incorrect, secret_page
print("Content-type: text/html")
print()
print("<Title>Test CGI</Title>")

# Q1
# print("<h1>Hello World!</h1>")
# print("<p>" + str(dict(os.environ)) + "</p>")

# # Q2 and Q3
# print()
# print(f"<p>Your query parameters are {os.environ.get('QUERY_STRING')}</p>")
# print(f"<p>Some info about your browser {os.environ.get('HTTP_USER_AGENT')}</p>")

print(login_page())