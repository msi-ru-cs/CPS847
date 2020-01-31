import os
from slackclient import SlackClient
 
# CPS-847-Bot Slack
Bot_User_OAuth_Access_Token = '<Bot OAuth Here>'
SLACK_API_TOKEN = Bot_User_OAuth_Access_Token
 
# Hardcoded SLACK_API_TOKEN
slack_token = SLACK_API_TOKEN
client = SlackClient(slack_token)

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
 
def say_hello(data):
    if "text" in data and "user" in data:
        if data['text'].endswith("?"):
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']
    
            client.api_call('chat.postMessage',
                channel=channel_id,
                text="<@{}>!".format(user) + mock(data['text'])
            )
 
if client.rtm_connect():
    while client.server.connected is True:
        for data in client.rtm_read():
            if "type" in data and data["type"] == "message":
                say_hello(data)
else:
    print("Connection Failed")