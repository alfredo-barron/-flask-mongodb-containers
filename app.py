from flask import Flask, request, render_template, redirect, url_for 
from pymongo import MongoClient 

app = Flask(__name__) 

# MongoDB connection setup 
client = MongoClient(host='mongodb', port=27017, 
					username='root', password='pass', authSource="admin") 
db = client.mytododb 
collectors_collection = db.collectors 


@app.route('/') 
def home(): 
	collectors = collectors_collection.find() 
	return render_template('index.html', collectors=collectors) 


@app.route('/add_collector', methods=['POST']) 
def add_collector(): 
	if request.method == 'POST': 
		collector_data = { 
			'key': request.form['key'],
			'name': request.form['name'], 
			'address': request.form['address'], 
			'city': request.form['city'],
			'telephone': request.form['telephone'],
			'manager': request.form['manager'],
			'email': request.form['email']
		} 
		collectors_collection.insert_one(collector_data) 
	return redirect(url_for('home')) 


if __name__ == '__main__': 
	app.run(host='0.0.0.0', debug=True) 
