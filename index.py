#!/usr/bin/python

# -*- coding: UTF-8 -*-# enable debugging
import cgitb, cgi
cgitb.enable()
print("Content-Type: text/html;charset=utf-8\n")

import config

import MySQLdb
db = MySQLdb.connect(host=config.host,
                     user=config.user,
                     passwd=config.password,
                     db=config.db)
cur = db.cursor()

########################################################################################################################
# Function Definitions
########################################################################################################################

########################################################################################################################
# Main program
########################################################################################################################

arguments = cgi.FieldStorage()
# We assume the user is authenticated and trusted at this point, so encourage functionality by falling through to menu.
if "mode" not in arguments:
	mode = "main"
else:
	mode = arguments["mode"].value

# Print the navigation bar
print("<a href=\"?mode=main\">Enter Records</a><br />")
print("<a href=\"?mode=view\">View Records</a><br />")
print("<a href=\"?mode=delete_record\">Delete Records</a><br />")

# Branch based on user page choice
if( mode == "view" ):
	print("test")
elif( mode == "delete_record" ):
	print("test2")
else:
	print("<h1>Main Menu</h1>\n")
	# print instructions, list of facility_id -> facility names and other fields until dropdowns implemented
	# print form to enter new record
