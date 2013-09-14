from Handler import *

class KidsHandler(Handler):
	def get(self):
		self.render('kids.html')

	def post(self):
		first_name = self.request.get('first_name')
		last_name = self.request.get('last_name')
		attending_party = self.request.get('attending_party')
		# error check form
		if first_name == '' or last_name == '' or attending_party == '':
			self.render('kids.html', error=True)
		else:
			UserDatabase.addKid(first_name, last_name, attending_party)
			self.render('submitted.html')

class AdultsHandler(Handler):
	def get(self):
		self.render('adults.html')

	def post(self):
		first_name = self.request.get('first_name')
		last_name = self.request.get('last_name')
		attending_luncheon = self.request.get('attending_luncheon')
		# error check form
		if first_name == '' or last_name == '' or attending_luncheon == '':
			self.render('kids.html', error=True)
		else:
			UserDatabase.addAdult(first_name, last_name, attending_luncheon)
			self.render('submitted.html')

