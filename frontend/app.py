from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)
from flask import Flask

@app.route('/', methods=['GET', 'POST'])
def index():
	resp_back = requests.get('http://backend:5001/')
	results = str(resp_back.text)

	draw = results.split(",")
	draw_house = draw[0][15:-1]
	draw_user = draw[1]
	draw_win_card = draw[2][15:-1]
	draw_win = draw[3][15:-4]

	return draw_house

if  __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
