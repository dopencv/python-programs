#!/usr/bin/python

class Node(object):

	def __init__(self,data):
		self.data = data
		self.next = Node(0)
