from telethon import TelegramClient, __name__ as __base_name__
import asyncio
import logging
from telethon.events.common import EventBuilder


# CLIENTS:list = list()

class MultiClient:
    def __init__(self, sessions: list, *args, **kwargs) -> TelegramClient:
        self.sessions: list = sessions
        self.clients: list = list()
        self.__default_log__ = logging.getLogger(__base_name__)
        self.__default_log__.addHandler(logging.NullHandler())
        for session in self.sessions:
            _cli = TelegramClient(session, *args, **kwargs)
            setattr(_cli, 'session_id', session)
            self.clients.append(_cli)

    def on(self: 'MultiClient', event: EventBuilder):
        def decorator(f):
            for cli in self.clients:
                cli.add_event_handler(f, event)

        return decorator

    def run_all_clients(self, loop=None):
        loop = loop if loop is not None else asyncio.get_event_loop()
        loop.run_until_complete(self._run_all_clients())

    async def _run_all_clients(self):
        for cli in self.clients:
            await cli.start()

        tasks: list = list()
        for cli in self.clients:
            tasks.append(cli.run_until_disconnected())
            done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
