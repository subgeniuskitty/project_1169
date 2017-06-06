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
	cursor.execute("SELECT deleted,id,guest_id,facility_id,notes FROM " + table)
	print("<table>")
	print("<tr><th>record_id</th><th>guest_id</th><th>facility_id</th><th>notes</th></tr>")
	for row in cursor.fetchall():
		if row[0] == 1:
			print("<tr class=\"deleted_record\">")
		else:
			print("<tr>")
		print("<td>" + str(row[1]) + "</td>")
		print("<td>" + str(row[2]) + "</td>")
		print("<td>" + str(row[3]) + "</td>")
		print("<td>" + row[4] + "</td>")
		print("</tr>")
	print("</table>")

def print_delete_form():
	print("<form method=\"post\" action=\"?mode=delete_record_execute\">")
	print("Record ID:<br />")
	print("<input type=\"text\" name=\"record_id\" />")
	print("<input type=\"submit\" value=\"Submit\" />")
	print("</form>")

def delete_record(table, cursor, database, record_id):
	cursor.execute("UPDATE " + table + " SET deleted=1,deleted_timestamp=CURRENT_TIMESTAMP WHERE id=" + record_id)
	database.commit()

def print_enter_form():
	print("<form method=\"post\" action=\"?mode=enter_record_execute\">")
	print("Guest ID:")
	print("<input type=\"text\" name=\"guest_id\" />")
	print("Facility ID:")
	print("<input type=\"text\" name=\"facility_id\" />")
	print("Notes:")
	print("<input type=\"text\" name=\"notes\" />")
	print("<input type=\"submit\" value=\"Submit\" />")
	print("</form>")

def enter_record(table, cursor, database, guest_id, facility_id, notes):
	cursor.execute("INSERT INTO " + table + " (guest_id,facility_id,notes) VALUES (\"" + guest_id + "\",\"" + facility_id + "\",\"" + notes + "\")")
	database.commit()

def print_html_header():
	print("<html>")
	print("<head>")
	print("<title>Project 1169</title>")
	print("<link rel=\"stylesheet\" type=\"text/css\" href=\"stylesheet.css\" />")
	print("</head>")
	print("<body>")
	print("<div id=\"main_body\">")

def print_html_footer():
	print("</div>")
	print("</body>")
	print("</html>")

def print_navigation_header():
	print("<div class=\"sub_body\">")
	print("<a href=\"?mode=enter_record\" class=\"button\">Enter</a>")
	print("<a href=\"?mode=view_records\" class=\"button\">View</a>")
	print("<a href=\"?mode=delete_record\" class=\"button\">Delete</a>")
	print("</div>")

########################################################################################################################
# Main program
########################################################################################################################

arguments = cgi.FieldStorage()
# We assume the user is authenticated and trusted at this point, so encourage functionality by falling through to 'enter records' page.
if "mode" not in arguments:
	mode = "enter_record"
else:
	mode = arguments["mode"].value

print_html_header()
print_navigation_header()

print("<div class=\"sub_body\">")
# Branch based on user page choice
if(mode == "view_records"):
	print("<h1>View Records</h1>")
	print_all_records(config.table, cur)
elif(mode == "delete_record"):
	print("<h1>Delete Records</h1>")
	print_delete_form()
elif(mode == "delete_record_execute"):
	print("<h1>Delete Records</h1>")
	delete_record(config.table, cur, db, arguments["record_id"].value)
	print("Delete instruction issued for record_id=" + str(arguments["record_id"].value) + ". Use navigation bar to continue.<br />")
elif(mode == "enter_record"):
	print("<h1>Enter Records</h1>")
	print_enter_form()
elif(mode == "enter_record_execute"):
	print("<h1>Enter Record</h1>")
	enter_record(config.table, cur, db, arguments["guest_id"].value, arguments["facility_id"].value, arguments["notes"].value)
	print("Insert instruction issued. Use navigation bar to continue.")
else:
	print("<h1>Nowhere</h1>\n")
	print("How did you get here?")
print("</div>")

print_html_footer()

cur.close()
db.close()
