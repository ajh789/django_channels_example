# An example of using Django Channels

## Origin
See https://realpython.com/blog/python/getting-started-with-django-channels/

## Implementation
The implementation is not completely same as its origin.
There are some enhancements, especially in user list page.

Refer to Bootstrap 3.3 css https://getbootstrap.com/docs/3.3/css/ to beautify html elements.

## Add chatroom as a second app
See https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django

Fix a bug in original implementation of consumer function ws_connect, add an extremely important operation:
```
message.reply_channel.send({'accept': True})
```
