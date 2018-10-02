from flask import Flask,request,redirect,url_for, render_template
import json
import requests #pip install requests
from random import choice
app = Flask(__name__)

@app.route('/<query>')
def getData(query):
    url = 'https://api.unsplash.com/search/photos'
    payload = { 'client_id':'743e2fead95c6632e755212a9d4fc2dea8a9ab8de7f5fb90ae835a017834045f','query': query}
    req = requests.get(url, params=payload)
    data = req.json()
    demo_img = "<img style='max-width:100%' src='" + data['results'][2]['urls']['full'] + "'>" 
    return demo_img


if __name__ == "__main__":
    app.run(debug=True) 