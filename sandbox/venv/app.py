from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

quarks = [ {'name': 'up', 'charge': '+2/3'},
	   {'name': 'down', 'charge': '-1/3'},
	   {'name': 'charm', 'charge': '+2/3'},
	   {'name': 'strange', 'charge': '-1/3'}
	  ]

@app.route('/', methods=['GET'])
def hello_world():
	return jsonify({'message': 'Hello, World!'})

@app.route('/quarks', methods=['GET'])
def returnAll():
	return jsonify({'quarks' : quarks})

@app.route('/quarks/<string:name>', methods=['GET'])
def returnOne(name):
	theOne = {}
	for i,q in enumerate(quarks):
		if q['name'] == name:
			theOne = quarks[i]
	return jsonify({'quarks': theOne})


#curl --data '{"name":"boom", "charge":"+2/3"}' -H "Content-Type: application/json" -X POST http://localhost:5000/quarks

@app.route('/quarks', methods=['POST'])
def addOne():
	new_quark = request.get_json()
	quarks.append(new_quark)
	return jsonify({'quarks' : quarks})

#curl --data '{"name":"down", "charge":"-7/3"}' -H "Content-Type: application/json" -X PUT http://localhost:5000/quarks/down

@app.route('/quarks/<string:name>', methods=['PUT'])
def editOne(name):
	new_quark = request.get_json()
	for i,q in enumerate(quarks):
		if q['name'] == name:
			quarks[i] = new_quark
	qs = request.get_json()
	return jsonify({'quarks' : quarks})


# curl --data '{"name":"down", "charge":"-6/3"}' -H "Content-Type: application/json" -X DELETE http://localhost:5000/quarks/strange
@app.route('/quarks/<string:name>', methods=['DELETE'])
def deleteOne(name):
	for i,q in enumerate(quarks):
		if q['name'] == name:
			del quarks[i]
	return jsonify({'quarks' : quarks})

if __name__ == "__main__":
	app.run(debug=True)
