from channels.routing import route
from channels.staticfiles import StaticFilesConsumer

channel_routing = [
    route('http.request', StaticFilesConsumer()),
    
    route('websocket.connect'   , 'userlist.consumers.ws_connect'   , path=r'^/userlist/'),
    route('websocket.disconnect', 'userlist.consumers.ws_disconnect', path=r'^/userlist/'),
    
    route('websocket.connect'   , 'chatroom.consumers.ws_connect'   , path=r'^/chatroom/'),
    route('websocket.disconnect', 'chatroom.consumers.ws_disconnect', path=r'^/chatroom/'),
    route('websocket.receive'   , 'chatroom.consumers.ws_receive'   , path=r'^/chatroom/'),
]
