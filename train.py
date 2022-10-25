from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatBot = ChatBot('ChatBot')
def workIt():
    trainer = ListTrainer(chatBot)

    trainer.train([      "cheapest watch","most afforrdale collection is the CommonFolk sets",
                        "affordable watches", "our cheapest collection is the Peasent Watches",
                        "most exansive watch", "most expansive is the Rouge Prince collection",
                        "newst watches","news collection is are Lanester watches",
                        "what is the mose popular","most popular are the Balerion watches",
                        "which do you like","the coolest looking are the Targeriayn watches",
                     "what is the least popular", "the least popular are the Peasent Watches",
                     "which one can i afford","best watches you can affored are the Lanester watches",
                     "what can you do", "What we can do is fit, clean, and modify a watch","anything speical about them",
                     "each Targeriayn and Prince watch has special properites about them, refer to item discription",
                     "hours of operation","hours of operation 24 hours as long the coud is alive"
                     
                     
                        
                        
                ])
    print('------------------worked it----------------------')
    