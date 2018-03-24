# Consumers are the counterpart to views

import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

# Decorator to get the user from the Django session
# If no logged-in user in existing session, username is empty.
# Browser should do proper processing of visualization when username is empty.
@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({ # Dump object to string; JavaScript counterpart is event.data in socket.onmessage;
            'username': message.user.username,
            'is_logged_in': True,
            'ws_event': 'connect'
        })
    })

# Decorator to get the user from the Django session
# Leaving web page will trigger a "disconnect" message from browser.
@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({ # Dump object to string; JavaScript counterpart is event.data in socket.onmessage;
            'username': message.user.username,
            'is_logged_in': False,
            'ws_event': 'disconnect'
        })
    })
    Group('users').discard(message.reply_channel)
