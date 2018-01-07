from channels.routing import route
from channels.staticfiles import StaticFilesConsumer

channel_routing = [
    route('http.request', StaticFilesConsumer()),
    route('websocket.connect', 'example.consumers.ws_connect', path=r'^/example/'),
    route('websocket.disconnect', 'example.consumers.ws_disconnect', path='^/example/'),
    route('websocket.connect', 'chatroom.consumers.ws_connect', path=r'^/chatroom/'),
    route('websocket.disconnect', 'chatroom.consumers.ws_disconnect', path=r'^/chatroom/'),
    route('websocket.receive', 'chatroom.consumers.ws_receive', path=r'^/chatroom/'),
]
