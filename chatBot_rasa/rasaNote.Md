
RASA: ALL OPEN SOURSE
tensorflow in USE

https://rasa.com/docs/rasa/installation/installing-rasa-open-source

rasa -help to see all the command the most important is rasa train to retrain data, be sure to delete the old one

rasa train

Make reponses and varables based resoens 

https://github.com/RasaHQ/helpdesk-assistant     doc
https://www.youtube.com/watch?v=k2uA5gxTM80     demo


This how to make button that give different action to be used like you ask, and it give two options
https://forum.rasa.com/t/domain-yml-missing-text-or-custom-key-in-response-path/47215



https://github.com/Horizon733/rasa-webchat
 
 => example of using chatbot as on normal webpage
 => example of using chabot on a react component

this for server to run a front end to people can write the wiget 
activate api, sometime will need to enable cors => 

rasa run --enable-api 
rasa run --enable-api --cors="*"

port - p provide prot 

cross origin resource sharing => cors

python3 -m http.server to run index.html in the directory
