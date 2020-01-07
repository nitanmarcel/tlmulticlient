# Multi Sessions addon for Telethon

## Installing:

```bash
pip3 install tlmulticlient
```

## How to use:

```python

# importing multiclient library and other required imports
from tlmulticlient import MultiClient
import asyncio
from telethon import events
# create the multiclient

client = MultiClient(api_id=12345, api_hash='my_api_hash', sessions=['list', 'of', 'str_sessions'])

# listenting to new messages

@client.on(events.NewMessage)
def listener(event):
    # Now we need to use `event.client.etc` instead of client.etc to be able to run a function on all the available clients!
    await event.client.send_message(event.chat_id, "Hello World!")

    # To find out from which session an event was triggered we use:
    id = event.client.session_id # session id is the name of the session attached to the client which received the event.
    if id == 'str_sessions':
        print('This event was triggered from the session named str_sessions')
    else:
        print('This event was triggered from the session named {0}'.format(id))

# iterate though all the clients

for c in client:
    print(c.session_id)

# run all the clients

loop = asyncio.get_event_loop()
client.run_all_clients(loop=loop)
```


