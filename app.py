# 1. Create a flask
from flask import Flask ,render_template, request, redirect, url_for
import json
import requests
import mlab
from user_input import User_input
from quote import Quote
from random import choice

app = Flask(__name__)
mlab.connect()

# topic_list = ['age', 'alone', 'amazing', 'anger', 'anniversary', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday', 'brainy', 'business', 'car', 'chance', 'change', 'christmas', 'communication', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'diet', 'dreams', 'easter', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fathersday', 'fear', 'finance', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'gardening', 'god', 'good', 'government', 'graduation', 'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'independence', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'memorialday', 'men', 'mom', 'money', 'morning', 'mothersday', 'motivational', 'movies', 'movingon', 'music', 'nature', 'newyears', 'parenting', 'patience', 'patriotism', 'peace', 'pet', 'poetry', 'politics', 'positive', 'power', 'relationship', 'religion', 'respect', 'romantic', 'sad', 'saintpatricksday', 'science', 'smile', 'society', 'space', 'sports', 'strength', 'success', 'sympathy', 'teacher', 'technology', 'teen', 'thankful', 'thanksgiving', 'time', 'travel', 'trust', 'truth', 'valentinesday', 'veteransday', 'war', 'wedding', 'wisdom', 'women', 'work']
topic_list = ['amazing', 'attitude', 'beauty', 'best', 'chance', 'change', 'cool', 'courage', 'dreams', 'experience', 'failure', 'faith', 'fear', 'forgiveness', 'freedom', 'future', 'god', 'good', 'great', 'happiness', 'hope', 'independence', 'inspirational', 'intelligence', 'knowledge', 'learning', 'life', 'love', 'morning', 'motivational', 'patience', 'peace', 'positive', 'power', 'respect', 'sad', 'smile', 'society', 'strength', 'success', 'sympathy', 'thankful', 'time', 'trust', 'truth', 'wisdom']

# 1.homepage.html
@app.route("/")
def home():
    return render_template('/index.html')
    

# 2. today_quote
@app.route("/today_quote/random")
def today_quote():
    topic = choice(topic_list)
    topic_quote = Quote.objects(topic=topic)
    quote = choice(topic_quote)
    content = quote.content
    author = quote.author

    url = 'https://api.unsplash.com/search/photos'
    payload = { 'client_id':'743e2fead95c6632e755212a9d4fc2dea8a9ab8de7f5fb90ae835a017834045f','query': topic}
    req = requests.get(url, params=payload)
    data = req.json()
    random_img = choice(data['results'])
    imgUrl = str(random_img['urls']['regular'] )
    

    return render_template("today_quote.html",content=content, author= author, imgUrl=imgUrl)

dic = {
    "excited": "courage",
    "happy": "happiness",
    "sad": "sad",
    "disappointed": "hope",
    "bored": "inspirational",
    "angry": "patience",
}


# 2.1 
@app.route("/today_quote/<topic>")
def today_quote_topic(topic):
    url = 'https://api.unsplash.com/search/photos'
    payload = { 'client_id':'743e2fead95c6632e755212a9d4fc2dea8a9ab8de7f5fb90ae835a017834045f','query': topic}
    req = requests.get(url, params=payload)
    data = req.json()
    random_img = choice(data['results'])
    imgUrl = str(random_img['urls']['regular'] )
    if topic in dic.keys():
        quote_list = Quote.objects(topic=dic[topic])
        quote = choice(quote_list)
        content = quote.content
        author = quote.author
        return render_template("today_quote.html",content=content, author= author,imgUrl=imgUrl)
    else:
        return redirect(url_for("today_quote"))


# 3. get_message
@app.route("/get_message")
def get_message():
    quote_list = User_input.objects()
    quote = choice(quote_list)
    content = quote.content
    author = quote.author
   
    return render_template("get_message.html",content=content, author= author)

# 4. send_message
@app.route("/send_message",methods=["GET","POST"])
def sent_message():
    if request.method =="GET":      
        return render_template("send_message.html")
    elif request.method =="POST":
        form = request.form
        author = form['author']
        content = form['content']
        new_quote = User_input(author=author, content=content, topic="message", priority=0)
        new_quote.save()
        return redirect('/thankyou')

# 5. thank you
@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

# 3. Run app
if __name__ == "__main__" :
    app.run(debug=True)