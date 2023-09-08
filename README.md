# RasaFramework
Rasa Framework

Commands to run the application

Step 1- 

pip3 install 'rasa[full]'

pip install gunicorn flask

pip install "fastapi[all]"

pip install sentence-transformers

pip install pandas

Step 2 - rasa init  (RASA project will create)  --- not required this step

Step 3 - To train RASA changes

Rasa train

Step 4 - To run Action server to connect to backend

rasa run actions

Step 5 - To test the application

rasa run --enable-api --port 5005


Step 6 - Start the Flask server

gunicorn --bind 0.0.0.0:5000 ui_app:app


Step 7 - Start Fast Api Server

uvicorn restservice_app:app --reload


Step 8 - Try chat bot

http://localhost:5000


Step 9 - Test Fast API 

http://localhost:8000/docs




