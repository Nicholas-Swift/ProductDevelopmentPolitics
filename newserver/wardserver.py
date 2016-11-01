import json
import math

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

import flask
from flask import Flask
from flask import request

# DATABASE STUFF
class DatabaseHelper:

	def __init__(self):
		client = MongoClient('localhost', 27017)
		self.db = client.my_database
		self.wards = self.db.wards

	def index_wards(self):
		return_wards = []
		for ward in self.wards.find(): #for post in posts.find({"author": "Mike"}):
			print(ward)
			return_wards.append(ward)
		return return_wards

	def show_ward(self, ward_id):
		return_ward = self.wards.find_one({'_id': ObjectId(ward_id)})
		return return_ward

	def create_ward(self, ward_dict):
		ward_id = self.wards.insert_one(ward_dict).inserted_id
		return ward_id

	def delete_ward(self, ward_id):
		self.wards.remove({"_id": ObjectId(ward_id)})

dbHelper = DatabaseHelper()


# FLASK STUFF
app = Flask(__name__)

# INDEX WARDS
@app.route('/wards', methods=['GET'])
def indexWards():

	# my_args = request.args
	# if 'province' in my_args.keys():
	# 	return_dict = {}
	# 	return_dict['status'] = 'Successfully index wards'

	# 	addr = request.args.get('province')

	# 	return_wards = []
	# 	wards = dbHelper.index_wards()
	# 	for i in range(0, len(wards)):
	# 		if 
	# 	for i in range(0, len(return_wards)):
	# 		return_wards[i]['_id'] = str(return_wards[i]['_id'])

	# 	return_dict['message'] = return_wards

	# 	return flask.jsonify(return_dict)
	# else:
	return_dict = {}
	return_dict['status'] = 'Successfully index wards'

	wards = dbHelper.index_wards()
	for i in range(0, len(wards)):
		wards[i]['_id'] = str(wards[i]['_id'])
	return_dict['message'] = wards

	return flask.jsonify(return_dict)

# CREATE WARD
@app.route('/wards', methods=['POST'])
def createWard():
	return_dict = {}

	# print("\n\n\n\n\n")
	# print("Request headers")
	# print(request.headers)

	# print("\n\n\n\n\n")
	# print("Request form")
	# print(request.form)

	# print("\n\n\n\n\n")
	# print("Request json")
	# print(request.json)

	# print(type(request.form))
	# print(type(request.json))

	if request.json == None:
		first_name = request.form.get('firstName')
		last_name = request.form.get('lastName')
		phone_number = request.form.get('phoneNumber')
		email_address = request.form.get('emailAddress')
		ward_number = request.form.get('wardNumber')
		province = request.form.get('Province')
		physical_address = request.form.get('PhysicalAddress')

		if first_name == None or last_name == None or phone_number == None or email_address == None or ward_number == None or province == None or physical_address == None:

			print(first_name)
			print(last_name)
			print(phone_number)
			print(email_address)
			print(ward_number)
			print(province)
			print(physical_address)

			return_dict['status'] = 'Failed. Please fill out all required body tags. firstName, lastName, phoneNumber, emailAddress, wardNumber, province'
			return flask.jsonify(return_dict)

		ward_dict = {
			'firstName': first_name,
			'lastName': last_name,
			'phoneNumber': phone_number,
			'emailAddress': email_address,
			'wardNumber': ward_number,
			'Province': province,
			'PhysicalAddress': physical_address
		}
		ward_id = dbHelper.create_ward(ward_dict)
		return_ward = dbHelper.show_ward(ward_id)
		return_ward['_id'] = str(return_ward['_id'])

		return_dict['status'] = 'Successfully created ward.'
		return_dict['message'] = return_ward

		return flask.jsonify(return_dict)

	first_name = request.json['firstName']
	last_name = request.json['lastName']
	phone_number = request.json['phoneNumber']
	email_address = request.json['emailAddress']
	ward_number = request.json['wardNumber']
	province = request.json['Province']
	physical_address = request.json['PhysicalAddress']

	if first_name == None or last_name == None or phone_number == None or email_address == None or ward_number == None or province == None or physical_address == None:

		print(first_name)
		print(last_name)
		print(phone_number)
		print(email_address)
		print(ward_number)
		print(province)
		print(physical_address)

		return_dict['status'] = 'Failed. Please fill out all required body tags. firstName, lastName, phoneNumber, emailAddress, wardNumber, province'
		return flask.jsonify(return_dict)

	ward_dict = {
		'firstName': first_name,
		'lastName': last_name,
		'phoneNumber': phone_number,
		'emailAddress': email_address,
		'wardNumber': ward_number,
		'Province': province,
		'PhysicalAddress': physical_address
	}
	ward_id = dbHelper.create_ward(ward_dict)
	return_ward = dbHelper.show_ward(ward_id)
	return_ward['_id'] = str(return_ward['_id'])

	return_dict['status'] = 'Successfully created ward.'
	return_dict['message'] = return_ward

	return flask.jsonify(return_dict)

# DELETE WARD
@app.route('/wards/<id>', methods=['DELETE'])
def deleteWard(id):
	return_dict = {}

	dbHelper.delete_ward(id)
	return_dict['status'] = 'Successfully deleted wards'
	return_dict['message'] = 'cool'

	return flask.jsonify(return_dict)


# MAIN STUFF
if __name__ == '__main__':
	app.run()
