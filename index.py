#!/usr/bin/python

# -*- coding: UTF-8 -*-# enable debugging
import cgitb, cgi
cgitb.enable()
print("Content-Type: text/html;charset=utf-8\n")

import MySQLdb
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="nopass",
                     db="sgk_project1169")
cur = db.cursor()

########################################################################################################################
# Function Definitions
########################################################################################################################

########################################################################################################################
# Main program
########################################################################################################################

arguments = cgi.FieldStorage()
if( arguments["mode"] == "view" ):
	# print all the data, kept separate since it will slow down as table size inceases and I want input to be snappy.
if( arguments["mode"] == "delete_record" ):
	# form to delete record, kept on separate page to avoid accidents
else:
	# We assume the user has already been validated elsewhere and has full access, so we want to encourage functionality.
	# Thus, we fall through to the main menu.
	print("<h1>Main Menu</h1>\n")
	# print instructions, list of facility_id -> facility names and other fields until dropdowns implemented
	# print link to view data
	# print link to delete record
	# print form to enter new record
