from Handler import *

class Kid(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_service = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)
	shirt_size=ndb.StringProperty(required=True)

class Adult(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_service = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)

def addKid(fname, lname, attendingp):
	kid = Kid(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp, shirt_size=shirt)
	kid.put()
	user = User(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp)
	user.put()

def addAdult(fname, lname, attendingl):
	intown = Intown(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp)
	intown.put()
	user = User(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp)
	user.put()