#!/usr/bin/python3

import sqlite3
from DBConnector import DBConnector

class DBManipulation:

	def __init__(self, connection):
		self.connection = connection
		
	# This prime focus to create table in runtime
	def createTable(self, tableString):
		if tableString:
			conn = self.connection
			cursor = conn.cursor()
			cursor.execute(tableString)
			print('Table created successfully ...')
		else:
			print('Table creation failed ...')
			raise Exception('Table creation string is empty')

	#This used to insert the bulk data into the query table
	def queryExecutor(self, query, listOfData):
		if query:
			if listOfData == None:
				raise Exception('Crawling data was empty ...')
			conn = self.connection
			cursor = conn.cursor()
			cursor.executemany(query, listOfData)
			conn.commit()
			return True
		else:
			raise Exception('Query string is empty')	

if __name__ == "__main__" :
	conn = DBManipulation('')

