#!/usr/bin/env python3
import json 
import websocket

############# SETTINGS #########################
# Room to join (Your stream's username)
CONST_BROADCASTER = ""
# Username (Your bot's username)
CONST_USERNAME = ""
# Token (Your bot's access token - see README.md) 
CONST_TOKEN = ""
################################################

wss_url = "ws://api.gaminglive.tv/chat/%s?nick=%s&authToken=%s"
