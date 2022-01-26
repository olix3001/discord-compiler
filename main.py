import asyncio
import os

import discord
from dotenv import load_dotenv

from Hypervisor import Hypervisor
from ScriptContainer import ScriptContainer
from containers.BashContainer import BashContainer
from containers.PythonContainer import PythonContainer

lang_containers = {
    'python': PythonContainer,
    'bash': BashContainer
}

hypervisor = Hypervisor()

async def runCode(container: ScriptContainer, code: str = None):
    return await hypervisor.run(container, 2, code=code)


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    client = discord.Client()


    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')


    @client.event
    async def on_message(message):
        if message.content.startswith(os.getenv("PREFIX")):
            parts = message.content.split()
            if len(parts) < 3:
                await message.reply("Usage: `compile <lang> <code>`")
                return
            cmd = parts[0][len(os.getenv("PREFIX")):]
            lang = parts[1]
            code = message.content[len(parts[0])+len(lang)+2:].split('\n')[1:]
            code = '\n'.join(code[:-1])
            if cmd == "compile":
                if lang in lang_containers:
                    res = await runCode(lang_containers[lang](), code=code)
                    resT = res.decode("utf-8")
                    await message.reply(f'```\n{resT[:1900]}{"[...]" if len(resT)>1900 else ""}\n```')


    client.run(TOKEN)
