from docker import DockerClient

from ScriptContainer import ScriptContainer


class PythonContainer(ScriptContainer):
    def __init__(self):
        super().__init__("python:3.9-alpine")
        self.command = "echo \"Internal server error\""#"python3 /tmp/code"

    def getName(self):
        return "Python"

    def create(self, client: DockerClient, isCode):
        if isCode:
            self.command = f'python3 /tmp/temp/{self.cid}'
        super().create(client, isCode)
