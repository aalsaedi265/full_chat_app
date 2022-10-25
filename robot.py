from chatterbot import ChatBot
from chatterbot.conversation import Statement

from chatterbot.trainers import ChatterBotCorpusTrainer #collection of words

# create ChatBot
chatBot = ChatBot('ChatBot')

# create ChatBot trainer
trainer = ChatterBotCorpusTrainer(chatBot)

# Train ChatBot with English language corpus
trainer.train("chatterbot.corpus.english")

# Greeting from chat bot
print("Hi, I am ChatBot")


#can be swapoed with pureChat folder chat bot, needs an parameter

# keep communicating with ChatBot
while True:
    # take user input/query
    query = input(">>>")
    # response from ChatBot
    # put query on Statement format to avoid runtime alert messages
    # Statement(text=query, search_text=query)
    print(chatBot.get_response(Statement(text=query, search_text=query)))
    
    #get responese is a maethod in the class
    #takes the questy searched and send a restult