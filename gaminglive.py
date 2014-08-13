#!/usr/bin/env python3

import json 
import sys
import time
import websocket

############# SETTINGS #########################
# Room to join (Your stream's username)
CONST_BROADCASTER = "_CHANGE_ME_"

# Username (Your bot's username)
CONST_USERNAME = "_CHANGE_ME_"

# Token (Your bot's access token - see README.md) 
CONST_TOKEN = "_CHANGE_ME_"

# Show messages in console
CONST_CONSOLE_MSG = True
################################################

# Throttle or get banned from chat
time.sleep(3)


def generate_msg(message):
  structure = {"user": {"nick": CONST_USERNAME, "isHost": False, "isRegistered": True}, "message": message}
  return json.dumps(structure, sort_keys=False)

def on_gaminglive_msg_in(ws, message): 
  tmp = json.loads(message)
  out = tmp['message']
  user = tmp['user']['nick']
  if CONST_CONSOLE_MSG: print("\n[%s]: %s" % user, out)

  # Commands - Move this to a proper file later
  if out.lower() == '!help':
    ws.send(generate_msg("Welcome to glbot! You typed !help."))
  if out.lower() == '!ping':
    ws.send(generate_msg("pong"))
  if out.lower() == '!doge':
    ws.send(generate_msg("woof"))


def on_gaminglive_error(wsptr, error):
  print("--- Error: " + error)

def on_gaminglive_close(wsptr):
  print("=== Socket was closed. Goodbye.")

def on_gaminglive_open(wsptr):
  ws.send(generate_msg("glbot has connected! You should see this message in chat."))

wss_url = "ws://api.gaminglive.tv/chat/%s?nick=%s&authToken=%s" % (CONST_BROADCASTER, CONST_USERNAME, CONST_TOKEN)
print("=== Starting up: gaminglivebot/0.0.1\n=== github.com/dillpickle/gaminglive for updates")
if CONST_USERNAME == "_CHANGE_ME_": sys.exit("==== Please update your configuration.")

ws = websocket.WebSocketApp(wss_url,
                            on_message = on_gaminglive_msg_in,
                            on_error = on_gaminglive_error,
                            on_close = on_gaminglive_close) 

ws.on_open = on_gaminglive_open
ws.run_forever()
