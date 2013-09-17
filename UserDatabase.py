from Handler import *

class Kid(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)

class Adult(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_luncheon = ndb.StringProperty(required=True)

def addKid(fname, lname, attendingp):
	kid = Kid(first_name=fname, last_name=lname, attending_party=attendingp)
	kid.put()

def addAdult(fname, lname, attendingl):
	adult = Adult(first_name=fname, last_name=lname, attending_luncheon=attendingl)
	adult.put()
