#!/usr/bin/python3

import sqlite3

class DBConnector:

	def __init__(self, connection, schemaName):
		self.connection = connection
		self.schemaName = schemaName

	# function to create the database connection
	def create(self):
		try:
			print('Sqlite DB Schema creating ... ')
			self.connection = sqlite3.connect(self.schemaName)
			return self.connection;
		except Exception as ex:
			print('Exception while creating DB connection ', ex)

	def getConnection(self):
		if self.connection != null :
			return self.connection
		else :
			self.create();

	def closeConnection(self):
		self.connection.close();

if __name__ == "__main__" :
	print('Function calling main')
	conn = DBConnector('',"SampleCrawlerDB.db")
	conn.create()

