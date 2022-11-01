
RASA: ALL OPEN SOURSE
tensorflow in USE

https://rasa.com/docs/rasa/installation/installing-rasa-open-source

rasa -help to see all the command the most important is rasa train to retrain data, be sure to delete the old one

rasa train

this for server to run a front end to people can write the wiget 
activate api, sometime will need to enable cors => 
rasa run --enable-api 
rasa run --enable-api --cors="*"


python3 -m http.server to run index.html in the directory

cross origin resource sharing => cors


Make reponses and varables based resoens 

https://github.com/RasaHQ/helpdesk-assistant     doc
https://www.youtube.com/watch?v=k2uA5gxTM80     demo
