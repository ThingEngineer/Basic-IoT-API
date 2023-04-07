# Basic-IoT-API (backend API, database and frontend web app) 
Basic Microcontroller API Consumption

This repository is part of a series on how to consume an API with a microcontroller. The other repository in the series is the microcontroller firmware: [Basic-ESP-IoT](https://github.com/ThingEngineer/Basic-ESP-IoT).

“Consume API” means to engage with the API, this is done by sending requests to the API and receiving responses. 

The API will respond to requests with data, which is often in the form of JSON. It will also respond to requests with a status code, which indicates whether the request was successful or not.

---
## Getting Started
### Python backend API, database and frontend web app
1) Clone this repository or download it as a zip file.
```sh
git clone https://github.com/ThingEngineer/Basic-IoT-API.git
```
2) Install the required packages. (sqlite3 is comes with Python 3.4+ but we will install it anyway) 
```sh
pip install Flask sqlite3
```
3) Run the API.
```sh
python api.py
```
4) Install curl. 

curl is a command line tool for sending requests to APIs. It is not required but it is helpful for testing the API. This is the linux command to install curl. If you are using Windows, you can download curl from [here](https://curl.haxx.se/windows/). On macOS, curl is already installed.
```sh
sudo apt install curl
```
4) Test the API with curl. Replace the IP address with the IP address of the computer running the API.

These are some examples of how to use curl to test the API. You can also use a tool like [Postman](https://www.postman.com) to test the API. These API endpoints are what the microcontroller and the web app will be using to communicate.

GET all temperature readings
```sh
curl -v http://127.0.0.1:5000/api/temperature
```
POST a new temperature reading
```sh
curl -d 'temperature=99' http://127.0.0.1:5000/api/temperature
```
GET the current message
```sh
curl -v http://127.0.0.1:5000/api/message
```
POST a new message
```sh
curl -d 'body=Hello World' http://127.0.0.1.22:5000/api/message
```
5) Open the web app in a browser. Replace the IP address with the IP address of the computer running the API.
```sh
http://127.0.0.1.22:5000
```
Here you can view the temperature readings and clear the temperature readings from the database. You can also add and update the message that is displayed on the microcontroller serial monitor.

---
## Reference
[Python Docs](https://docs.python.org/3/) - The official Python documentation.

[Flask Docs](https://flask.palletsprojects.com/en/1.1.x/) - A Python web framework.

[What is REST](https://restfulapi.net) - A brief introduction to REST.

[HTTP Status Codes](https://httpstatuses.com) - A list of HTTP status codes and what they mean.

[JSON](https://www.json.org/json-en.html) - JavaScript Object Notation, the most common data format used for APIs.

[SQLite](https://www.sqlite.org/index.html) - A lightweight database.

[SQLite Browser](https://sqlitebrowser.org) - A helpful tool for viewing and editing SQLite databases.

[Postman](https://www.postman.com) - A helpful tool for testing APIs.