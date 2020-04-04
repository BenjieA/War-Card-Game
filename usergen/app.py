from flask import Flask, request, jsonify, Response
import requests
import random

app = Flask(__name__)
@app.route('/')
@app.route('/usergen', methods=['GET', 'POST'])
def usergen():
        suits = [' spades', ' clubs', ' hearts', ' diamonds']
        value = ['Ace of', '2 of', '3 of', '4 of', '5 of', '6 of', '7 of', '8 of', '9 of', '10 of', 'Jack of', 'Queen of', 'King of', 'Ace of']

        #one service
        #selects a random card suit and value for user w/low ace.
        rand_selval = value[random.randrange(len(value)-1)] #version 2: randrange(1,len(value)  #high ace
        rand_selsuit = suits[random.randrange(len(suits))]
        user_card = rand_selval + rand_selsuit
        user_score = value.index(rand_selval) #version 2: rand_selval[:-2]
        return_arr = {'card': user_card, 'score' : str(user_score), 'value' : rand_selval[:-3], 'service':'usergen','port':'5002'}

        return  return_arr

if  __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5002)
