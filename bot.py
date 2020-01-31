#Imports
import os
import re
import slack

# This script is inspired by the
#   tutorial https://github.com/mattmakai/slack-starterbot/blob/master/starterbot.py
# and is adopted to slackclient v.2.x using
#   https://github.com/slackapi/python-slackclient/wiki/Migrating-to-2.x

#Globals
KEY_WORD = "?"  # The string we look for to match in a message
MENTION_REGEX = "^<@([WU].+)>(.*)"  # RegEx for parsing command

# don't forget to set the environmental variable SLACK_BOT_TOKEN using
# export SLACK_API_TOKEN='Your Bot User OAuth Access Token'
# or hardcode

slack_token = os.environ.get('5SbpC9r1QnJVboj4K5gr7snO')


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']

    # uncomment if you want to see metadata of all messages
    # print(data)

    if 'text' in data:  # some text is present, let's parse it
        msg_txt = data['text'] # data[] stores key/value pairs

        # uncomment if you want to see text of all messages
        print(msg_txt)

        is_the_message_for_me, cmd = parse_message(msg_txt) # is_the_message_for_me is a boolean, cmd is the second matching substring; parse_message returns two values, that's why it looks like that

        if is_the_message_for_me:
            cmd_result = handle_command(cmd) #takes in command, and changes string based on requirements (we need to make it check for if its a question)

            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']

            webclient = payload['web_client']
            webclient.chat_postMessage(
                channel=channel_id,
                text="Hi <@{}>! {}".format(user, cmd_result), # puts user and cmd result into the curley braces
                thread_ts=thread_ts
            )


def parse_message(message_text): # splits into 2 groups when it finds my userid, else return nothing
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the tuple [True, text of the command]
        If there is no direct mention, returns [False, None]
    """
    matches = re.search(MENTION_REGEX, message_text) # search returns true if any substring in message_text matches the regex
    if matches and matches.group(1) == my_user_id: # group(n) returns the n-th matching substring 
        return True, matches.group(2).strip()
    else:
        return False, None


def handle_command(cmd):
    """
    Process command and return a result to be printed in a message to a user
    """
    # Default response is help text for the user
    response = "Not sure what you mean. Try asking a question"

    # Finds and executes the given command, filling in response
    # This is where you start to implement more commands!
    if cmd.endswith(KEY_WORD):
        response = mock(cmd)

    return response


def get_my_user_id(slack_api_token):
    """
    Get bot user id as per https://api.slack.com/methods/auth.test
    """
    return slack.WebClient(slack_token).auth_test()['user_id']


# get user id of the bot
my_user_id = get_my_user_id(slack_token)

# start the bot
rtmclient = slack.RTMClient(token=slack_token)
rtmclient.start()

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
