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

def print_all_records(table, cursor):
	cursor.execute("SELECT deleted,id,guest_id,facility_id,notes FROM " + config.table)
	print("<table>")
	print("<tr><th>id</th><th>guest_id</th><th>facility_id</th><th>notes</th></tr>")
	for row in cursor.fetchall():
		if row[0] == 1:
			print("<tr bgcolor=\"#FF0000\">")
		else:
			print("<tr>")
		print("<td>" + str(row[1]) + "</td><td>" + str(row[2]) + "</td><td>" + str(row[3]) + "</td><td>" + row[4] + "</td></tr>")
	print("</table>")

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
	print("<h1>All Records</h1>")
	print_all_records(config.table, cur)
elif( mode == "delete_record" ):
	print("test2")
else:
	print("<h1>Main Menu</h1>\n")
	# print instructions, list of facility_id -> facility names and other fields until dropdowns implemented
	# print form to enter new record
