https://www.youtube.com/watch?v=PfYBXidENlg&t=986s helpful example

RASA: ALL OPEN SOURSE tensorflow in USE

https://rasa.com/docs/rasa/installation/installing-rasa-open-source

rasa -help to see all the command the most important is rasa train to retrain data, be sure to delete the old one

rasa train

Make reponses and varables based resoens

https://github.com/RasaHQ/helpdesk-assistant doc https://www.youtube.com/watch?v=k2uA5gxTM80 demo

This how to make button that give different action to be used like you ask, and it give two options https://forum.rasa.com/t/domain-yml-missing-text-or-custom-key-in-response-path/47215

https://github.com/Horizon733/rasa-webchat

=> example of using chatbot as on normal webpage => example of using chabot on a react component

this for server to run a front end to people can write the wiget activate api, sometime will need to enable cors =>

pip install pyngrok https://rasa.com/docs/rasa/messaging-and-voice-channels/




SERVER STUFF HTTP

ngrok http 5005; rasa run

pip install rasa_core

rasa run --enable-api


https://dev.to/petr7555/rasa-socket-io-integration-pfo

python3 -m http.server 8000

webchat termainal:  npx http-server .
rasa main terminal: rasa run --cors "*"
rasa main terminal: rasa run actions


rasa run --enable-api

port - p provide prot

cross origin resource sharing => cors

8000 //MY FRONT END IS ON 800 AND BACK IS ON 5005        
python3 -m http.server 
npx http-server .