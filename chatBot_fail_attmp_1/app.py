from flask import Flask, render_template
from flask_socketio import SocketIO, send #piece will bind fron and back 

app.config['SECRET_KEY'] = "secretkey123"

socketio = SocketIO(app,cors_allowed_origin="*")


@socketio.on('message')
def handle_message(message):
    print('Received message: '+message)
    if message != "User connected!":
        send(message, broadcast= True)
        

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    # userText = request.args.get('msg')
    # return str(chatbot.get_response(userText))
    pass

if __name__ == "__main__":
    # app.run()
    socketio.run(app,host="localhost")#will be change once lindoe is ready