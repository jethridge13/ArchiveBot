import datetime
import os
import sqlite3
import json

class ArchiveBot():

	def __init__(self):
		self.conn = ''
		self.c = ''
		self.clientID = ''
		self.clientSecret = ''
		self.vt = ''
		self.token = ''
		# self.startDatabase()
		try:
			keys = self.loadKey()
		except FileNotFoundError:
			print('ERROR: apikey.json not found.')
			return
		if keys.get('clientID'):
			self.clientID = keys['clientID']
		if keys.get('clientSecret'):
			self.clientSecret = keys['clientSecret']
		if keys.get('verificationToken'):
			self.vt = keys['verificationToken']

	def startDatabase(self):
		# TODO
		self.conn = sqlite3.connect('archive-bot.db')
		self.c = self.conn.cursor()
		c.execute('create table if not exists users ()')
		c.execute('create table if not exists channels ()')
		c.execute('create table if not exists messages ()')

	def getUsers(self):
		# TODO
		print()

	def getChannels(self):
		# TODO
		apiHook = 'channels.list'

	def getMessages(self):
		# TODO
		print()

	def updateUsers(self):
		# TODO
		print()

	def updateChannels(self):
		# TODO
		print()

	def updateMessages(self):
		# TODO
		print()

	def login(self):
		# TODO
		cID = self.clientID

	def sendRequest(self):
		# TODO
		url = 'https://slack.com/api/'

	def loadKey(self):
		try:
			with open ('apikey.json') as keys:
				j = json.load(keys)
				return j
		except FileNotFoundError as e:
			raise e

