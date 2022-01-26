import os
import tarfile

from docker import DockerClient


class ScriptContainer:
    def __init__(self, image):
        self.image = image
        self.container = None
        self.cid = None
        self.command = '/tmp/code'
        self.commands = []

    def setID(self, cid: str):
        self.cid = cid
        return self

    def getName(self):
        pass

    def uploadFile(self, path: str, file: str):
        print(f"Uploading file {file} to container {self.cid}")
        if self.container is None:
            return
        src = f'temp/{self.cid}.tar'
        with tarfile.open(src, 'w') as tar:
            tar.add(file)
        self.container.put_archive(path, open(src, 'rb').read())
        os.remove(src)

    def create(self, client: DockerClient, isCode):
        print(f"Creating new container {self.cid}")
        self.container = client.containers.create(self.image, self.command,
                                               name=f'{self.getName()}-{self.cid}',
                                               network_mode='none',
                                               detach=True,
                                               #auto_remove=True,
                                               cpu_shares=2,
                                               mem_limit="128m"
                                               )

    def start(self):
        if self.container is None:
            return
        print(f"Starting container {self.cid}")
        self.container.start()
        for cmd in self.commands:
            self.container.exec_run(cmd)

    def kill(self):
        if self.container is not None:
            l = ''
            try:
                l = self.container.logs()
                self.container.kill()
            except Exception:
                print(f"Cannot kill container {self.cid} (probably not working)")
            self.container.remove()
            return l
        return None
