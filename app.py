# 1. Create a flask
from flask import Flask ,render_template, request, redirect, url_for
import mlab
from user_input import User_input
from quote import Quote
from random import choice

app = Flask(__name__)
mlab.connect()


# 1.homepage.html
@app.route("/")
def home():
    return render_template('/index.html')
    

# 2. today_quote
@app.route("/today_quote/random")
def today_quote():
    quote_list = Quote.objects()
    quote = choice(quote_list)
    content = quote.content
    author = quote.author

    return render_template("today_quote.html",content=content, author= author)

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
    if topic in dic.keys():
        quote_list = Quote.objects(topic=dic[topic])
        quote = choice(quote_list)
        content = quote.content
        author = quote.author
        return render_template("today_quote.html",content=content, author= author)
    else:
        return redirect(url_for("today_quote"))


# 3. get_message
@app.route("/get_message")
def get_message():
    quote_list = User_input.objects()
    quote = choice(quote_list)
    content = quote.content
    author = quote.author
    # return render_template("",content=content, author= author)

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