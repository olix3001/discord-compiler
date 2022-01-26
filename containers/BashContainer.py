from docker import DockerClient

from ScriptContainer import ScriptContainer


class BashContainer(ScriptContainer):
    def __init__(self):
        super().__init__("ubuntu:latest")
        self.command = "echo \"Internal server error\""

    def getName(self):
        return "Ubuntu-bash"

    def create(self, client: DockerClient, isCode):
        if isCode:
            self.command = f'bash /tmp/temp/{self.cid}'
        super().create(client, isCode)
