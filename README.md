# Discord compiler bot
This is an experiment where I try to safely execute code in docker containers

## Installation
to install use `install.sh` on ubuntu, on everyhing else you need to install manually those things:
```yaml
pip packages: discord.py python-dotenv docker
standalone programs: docker
docker images: python:3.9-alpine ubuntu:latest
```

## Usage
To setup this bot remove `.example` from `.env.example` and put your bot token there
and run `main.py` as root

## Note
If some IO errors are thrown try creating `logs` and `temp` folder in main project directory