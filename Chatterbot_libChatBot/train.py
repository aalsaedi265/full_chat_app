from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatBot = ChatBot('ChatBot')
def workIt():
    trainer = ListTrainer(chatBot)

    trainer.train([      "cheapest watch",
                        "most afforrdale collection is the CommonFolk sets",
                        "cheap watch","commonFolk watchs",
                        "low tier watchs","commonfolk",
                        "affordable watches","the Peasent Watches are afforadable",
                        "what can I afford","if you want below $100 for for CommonFolk or Peasent, between $100 and $600 you can nearly all excep the prince watches, honestly depends on price range",
                        "affordable watch","depends on price range",
                        "most exansive watch", "most expansive is the Rouge Prince collection",
                        "newst watches","newest collection are Lanester watches",
                        "new watches","Lanester watches",
                        "what is the most popular",
                        "most popular are the Balerion watches","oldest watchs","Balerion set","old watch","Balerion collection","super collectables","Balerion watches", 'antiques',"Balerion set"
                        "which do you like","the coolest looking are the Targeriayn watches","historically collectable watches","Balerion set",
                        "what is the least popular", "the least popular are the Peasent Watches","worst watches","Peasent set, compared to the other here, you put peasent agains other not from the story and they are great",
                        "which one can i afford","best watches you can affored are the Lanester watches, that is for most middle class people, it all depends on the price range",
                        "what can you do" "STANISS" "can you clean",
                        "What the store can do is fit, clean, and modify a watchs you bought",
                        "anything speical about them",
                        "each Targeriayn and Prince watch has special properites about them, refer to item discription",
                        "hours of operation","hours of operation 24 hours as long the coud is alive",
                        'Hi',"What watch would like to buy",
                        "How are you","Fine, I am here to help sell you somehting you can afford",
                        "Good day","Hello, Caraxex here, what watch to you want","Hello",
                        "hello human, are you ready to buy",
                        "see you late","take care valued customer",
                        "I am leaving","till next time", 
                        "goodbye","bye", 
                        "so long","untill you come for another watch",
                        "Have a good day","I Caraxex, wish you well"
                     
                     
                        ])
    print('------------------worked it----------------------')
    