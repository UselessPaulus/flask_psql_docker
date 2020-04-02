from app import db

class human_data(db.Model):

	__tablename__ = 'humans'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String())
	manager = db.Column(db.String())
	start = db.Column(db.String())

	def __init__(self,name,manager,start):
		self.name = name
		self.manager = manager
		self.start = start
	def __repr__(self):
		return '<id{}>'.format
	def serialize(self):
		return{
			"id":self.id,
			"name":self.name,
			"manager":self.manager,
			"start":self.start
		}

