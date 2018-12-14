import os
import time
from slackclient import SlackClient
from handlers import *

BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"

slack_client = SlackClient(os.environ.get("SLACK_BOT_TOKEN"))

def handle_command(command, channel):
    """
    Delegates commands to various handlers
    """
    # TODO: add logic for handling different commands for different channels
    # hint: use groups.list and channel.list API call
    #if command.startswith("isc17"):
    #    response = check_isc17_coding_challenge()
    #else:
    response = pick_a_quotation()
    slack_client.api_call("chat.postMessage", channel=channel,
            text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    """
    Parse slack output to get command and channel
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("Enigma connected and running...")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed...")
