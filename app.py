
from flask import Flask, request,render_template,jsonify
from bot import test

test()
app = Flask(__name__)



@app.route("/")
def home():
   # return jsonify({'Message':"success"})
    return render_template("index.html")

# @app.route("/get")
# def get_response():
#     userText = request.args.get('msg')
#     return str(chatbot.get_response(userText))

if __name__=='__main__':
    app.run()