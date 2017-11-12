import datetime
import os
import sqlite3

def ArchiveBot():

	def __init__(self):
		self.conn = ''
		self.c = ''
		self.clientID = ''
		self.clientSecret = ''
		self.startDatabase()

	def startDatabase(self):
		self.conn = sqlite3.connect('archive-bot.db')
		self.c = self.conn.cursor()
		c.execute('create table if not exists users ()')
		c.execute('create table if not exists channels ()')
		c.execute('create table if not exists messages ()')

	def getUsers(self):

	def getChannels(self):

	def getMessages(self):

	def updateUsers(self):

	def updateChannels(self):

	def updateMessages(self):

	def sendRequest(self):
		url = 'https://slack.com/api/'
