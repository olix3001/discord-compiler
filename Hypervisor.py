import asyncio
import os
import uuid
from datetime import datetime

from ScriptContainer import ScriptContainer
import docker


class Hypervisor():
    def __init__(self):
        self.client = docker.from_env()
        self.logs = open(f'logs/{uuid.uuid4()}.txt', 'a')

    async def run(self, container: ScriptContainer, lifespan: int, code: str = None):
        container.setID(str(uuid.uuid4()))
        self.logs.write(f'[{datetime.now().strftime("%H:%M:%S")}] Running {container.getName()} for {lifespan}s with id {container.cid}\n')
        self.logs.flush()
        container.create(self.client, code is not None)

        if code is not None:
            src = f'temp/{container.cid}'
            with open(src, 'w') as f:
                f.write(code)
            container.uploadFile('/tmp', src)
            os.remove(src)

        container.start()

        await asyncio.sleep(lifespan)

        return container.kill()
