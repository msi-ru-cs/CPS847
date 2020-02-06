import os
from slackclient import SlackClient
import requests
import json

# CPS-847-Bot Slack
Bot_User_OAuth_Access_Token = '<SLACK TOKEN>'
SLACK_API_TOKEN = Bot_User_OAuth_Access_Token

# SLACK_API_TOKEN
slack_token = SLACK_API_TOKEN
client = SlackClient(slack_token)

# Open Weather API
weather_dict = {}
WEATHER_API_KEY = '<WEATHER-API-KEY>'

image_url = "https://i.kym-cdn.com/entries/icons/original/000/022/940/mockingspongebobbb.jpg"
attachments = [{"title": "spongebob", "image_url": image_url}]

# Converts text to mocking text
def mock(cmd):
    store = ""
    toggle = True  # capitalize
    for char in cmd:
        if toggle:
            store += char.upper()
        else:
            store += char.lower()
        if char != ' ':
            toggle = not toggle
    return store

# Interacts with user when they ask a question and mocks them
def say_hello(data):
    if "text" in data and "user" in data:
        if data['text'].endswith("?"):
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']
    
            client.api_call('chat.postMessage',
                channel=channel_id,
                text="<@{}> ".format(user) + mock(data['text']),
                attachments=attachments
            )

# Returns current weather conditions for a few cities based on user input
def current_weather(data):
    city = ''
    msg = ''
    if "text" in data and "user" in data:
        user = data['user']
        if "weather" in data['text']:
            if "vancouver" in data['text'].lower():
                city = 'vancouver'
                channel_id = data['channel']
                weather_dict[city] = city_forecast(city)
                weather_descr = weather_dict[city]['weather'][0]['description']
                msg = "the weather in " + city + " is currently: " + weather_descr

            elif "ottawa" in data['text'].lower():
                city = 'ottawa'
                channel_id = data['channel']
                weather_dict[city] = city_forecast(city)
                weather_descr = weather_dict[city]['weather'][0]['description']
                msg = "the weather in " + city + " is currently: " + weather_descr
            
            elif "toronto" in data['text'].lower():
                city = 'toronto'
                channel_id = data['channel']
                weather_dict[city] = city_forecast(city)
                weather_descr = weather_dict[city]['weather'][0]['description']
                msg = "the weather in " + city + " is currently: " + weather_descr
            
            elif "seattle" in data['text'].lower():
                city = 'seattle'
                channel_id = data['channel']
                weather_dict[city] = city_forecast(city)
                weather_descr = weather_dict[city]['weather'][0]['description']
                msg = "the weather in " + city + " is currently: " + weather_descr

            else:
                channel_id = data['channel']
                msg = 'Please pick a city between: vancouver, ottawa, toronto and seattle instead! Support for other cities coming soon.'

    
            client.api_call('chat.postMessage',
                channel=channel_id,
                text="Hey <@{}> ".format(user) + msg
            )

# API call to openweathermap to get current weather
def city_forecast(city):
    #api endpoint
    URL = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + WEATHER_API_KEY
    
    # sending get request and saving the response as response object 
    r = requests.get(url = URL)

    return r.json()

# Bot connection to the slack client
if client.rtm_connect():
    print("Bot is running!")
    while client.server.connected is True:
        for data in client.rtm_read():
            if "type" in data and data["type"] == "message" and "weather" in data['text']:
                current_weather(data)

            elif "type" in data and data["type"] == "message":
                say_hello(data)
else:
    print("Connection Failed")