import os
from flask import Flask,request,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import human_data

@app.route("/")

def hello():
	return"Hello, for start print addres:\nAdd form:127.0.0.1:5000/add/form\nSearch id:127.0.0.1:5000/get/id \nSearch all:127.0.0.1:5000/getall"
@app.route("/add")

def add_human():
	name=request.args.get('name')
	manager=request.args.get('manager')
	start=request.args.get('start')
	try:
		worker=human_data(
			name=name,
			manager=manager,
			start=start
		)
		db.session.add(worker)
		db.session.commit()
		return "Worker add. worker id={}".format(worker.id)
	except Exception as e:
		return(str(e))
@app.route("/getall")
def get_all():
	try:
		workers=human_data.query.all()
		return jsonify([e.serialize() for e in workers])
	except Exception as e:
		return(str(e))
@app.route("/get/<id_>")
def get_by_id(id_):
	try:
		worker=human_data.query.filter_by(id=id_).first()
		return jsonify(worker.serialize())
	except Exception as e:
		return(str(e))

@app.route("/add/form",methods=["GET","POST"])
def add_form():
	if request.method == "POST":
		name=request.form.get('name')
		manager=request.form.get('manager')
		start=request.form.get('start')
		try:
			worker=human_data(
				name=name,
				manager=manager,
				start=start
			)
			db.session.add(worker)
			db.session.commit()
			return "Worker added. worker id={}".format(worker.id)
		except Exception as e:
			return(str(e))
	return render_template('getdata.html')


if __name__ == "__main__":
	app.run()
