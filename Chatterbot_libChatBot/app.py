
from flask import Flask, request,render_template,jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from Chatterbot_libChatBot.train import workIt
# from pureChatBot.bot import ask_user_for_sentence_and_produce_outPut


app = Flask(__name__)


chatbot = ChatBot('ChatBot')
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")
workIt()
# ask_user_for_sentence_and_produce_outPut()

@app.route("/")
def home():
   # return jsonify({'Message':"success"})
    return render_template("index.html")



@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))



if __name__=='__main__':
    app.run()