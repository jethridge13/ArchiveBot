import datetime
import os
import sqlite3
import json
from urllib.request import urlopen

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
		if keys.get('token'):
			self.token = keys['token']

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

	def test(self):
		hook = 'auth.test'
		return self.sendRequest(hook)

	def sendRequest(self, hook):
		# TODO
		# Note: urllib.urlencode() for requests
		url = 'https://slack.com/api/' + hook
		url += '?token=' + self.token
		try:
			response = urlopen(url).read()
		except Exception as e:
			return {'error': 'An error occurred when sending the request'}
		return response

	def loadKey(self):
		try:
			with open ('apikey.json') as keys:
				j = json.load(keys)
				return j
		except FileNotFoundError as e:
			raise e

