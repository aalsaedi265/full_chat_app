# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionMusic(Action):

#      def name(self) -> Text:
#          return "action_music"

#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       
#          msg = { "type": "video",
#                 "payload": { "title": "Link name",
#                             "src": "https://www.youtube.com/watch?v=6IeAiaPNw7s" 
#                             } 
#                 }

#          dispatcher.utter_message(template = "utter_music",text="Check this video: ",attachment=msg)
         
#          return []
     

# class AskLeaveType(Action):

#      def name(self) -> Text:
#          return "askLeaveType"

#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         data= [{ "title": "Sick Leave", "description": "Sick leave is time off from work that workers can use to stay home to address their health and safety needs without losing pay." },
#                { "title": "Earned Leave", "description": "Earned Leaves are the leaves which are earned in the previous year and enjoyed in the preceding years. " },
#                { "title": "Casual Leave", "description": "Casual Leave are granted for certain unforeseen situation or were you are require to go for one or two days leaves to attend to personal matters and not for vacation." },
#                { "title": "Flexi Leave", "description": "Flexi leave is an optional leave which one can apply directly in system at lease a week before." } 
#                ]

#         message={ "payload": "collapsible", "data": data }

#         dispatcher.utter_message(text="You can apply for below leaves",json_message=message)






