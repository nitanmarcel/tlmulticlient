from telethon import TelegramClient, __name__ as __base_name__
from telethon.tl import TLObject
import asyncio
import logging
from telethon.events.common import EventBuilder


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
        tasks: list = list()
        for cli in self.clients:
            await cli.start()
            tasks.append(cli.run_until_disconnected())
        done, tasks = await asyncio.gather(*tasks)

    def to_dict(self):
        return {c.session_id: c for c in self.clients}

    def stringify(self):
        result = ['(', '\n']
        for session_id, client in self.to_dict().items():
            result.append('\t')
            result.append(session_id)
            result.append(' : ')
            result.append(TLObject.pretty_format(client.__dict__, indent=0))
            result.append(',\n')
        result.pop()
        result.append('\n')
        result.append('\t')
        result.append(')')
        return ''.join(result)

    def __iter__(self):
        return iter(self.clients)

    def __dict__(self):
        self.to_dict()

    def __str__(self):
        return self.stringify()