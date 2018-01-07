from channels.routing import route
from example.consumers import ws_connect, ws_disconnect

channel_routing = [
    route('websocket.connect', ws_connect, path=r'^/example/'),
    route('websocket.disconnect', ws_disconnect, path='^/example/')
]
