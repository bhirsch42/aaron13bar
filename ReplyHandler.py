from Handler import *

class ReplyHandler(Handler):
	def get(self):
		kids = ndb.gql("SELECT * FROM Kid")
		adults = ndb.gql("SELECT * FROM Adult")
		self.render('reply.html', kids=kids, adults=adults)