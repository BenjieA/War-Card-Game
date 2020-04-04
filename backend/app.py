from flask import Flask, request, jsonify, Response
import requests
from os import getenv


app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY') 


@app.route('/')
@app.route('/backend', methods=['GET', 'POST'])
def backend():
	resp_houseval = requests.get('http://housegen:5003/housegen')
	resp_userval = requests.get('http://usergen:5002/')
	houseval = str(resp_houseval.text)
	userval = str(resp_userval.text)

	houseval = houseval.split(",")
	house_card = houseval[0][13:-1]
	house_score = int(houseval[2][14:-1])
	house_value = houseval[4][14:-1]

	userval = userval.split(",")
	user_card = userval[0][13:-1]
	user_score = int(userval[2][14:-1])
	user_value = userval[4][14:-1]

	if user_score > house_score:
		win_card = user_card
		winner = 'player'
#sql create database matches
#add columns user, house, winner, card
#add user card for this round
#add house card
#add winner name
#add winner card value  userval[5][14:-4]
	else:
		win_card = house_card
		winner = 'house'

	return_arr = {'h_card': house_card, 'u_card': user_card, 'winn_c': win_card, 'winner': winner}

	return return_arr

if  __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5001)
