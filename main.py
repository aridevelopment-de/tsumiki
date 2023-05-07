import os
import json
import random
import logging
import asyncio
import datetime

import discord
from dotenv import load_dotenv

from jsontypes import PeriodicEntry
load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("tsumiki.log"),
        logging.StreamHandler()
    ]
)


class Tsumiki(discord.Client):
    def __init__(self):
        super().__init__()
        self.voice_channel_id = os.environ["VOICE_CHANNEL_ID"]
        self.text_channel_id = os.environ["TEXT_CHANNEL_ID"]

    async def on_ready(self):
        logging.info('Logged on as {0}!'.format(self.user))
        self.loop.create_task(self.daily_rename_voice())

    @staticmethod
    async def __pick_random_element() -> PeriodicEntry:
        with open("periodictable.json", "r", encoding="utf-8") as fh:
            data = json.load(fh)

        return PeriodicEntry.from_dict(random.choice(data["elements"]))

    async def daily_rename_voice(self):
        while True:
            logging.info("Renaming voice and text channels")

            voice_element: PeriodicEntry = await self.__pick_random_element()
            voice_channel: discord.VoiceChannel = self.get_channel(int(self.voice_channel_id))

            await voice_channel.edit(
                name=voice_element.name,
                reason=f"Daily rename to {voice_element.name} ({voice_element.symbol})"
            )

            text_element: PeriodicEntry = await self.__pick_random_element()
            text_channel: discord.TextChannel = self.get_channel(int(self.text_channel_id))

            await text_channel.edit(
                name=f"general-{text_element.name.lower()}",
                topic=text_element.summary,
                reason=f"Daily rename to general-{text_element.name.lower()}"
            )

            remaining_seconds = 86400 - datetime.datetime.now().timestamp() % 86400
            logging.info(f"Sleeping for {remaining_seconds} seconds")

            await asyncio.sleep(remaining_seconds)


client = Tsumiki()
client.run(os.environ["TOKEN"])
