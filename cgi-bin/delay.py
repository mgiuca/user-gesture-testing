#!/usr/bin/env python3

import cgi
import cgitb
import time

cgitb.enable(format='text')

form = cgi.FieldStorage()
try:
  delay = int(form.getvalue('delay'))
except (TypeError, ValueError):
  delay = 0;

# Delay by that many ms before returning.
time.sleep(delay / 1000)

print('Content-Type: application/json')
print()
print('{"delay": %d}' % delay)
