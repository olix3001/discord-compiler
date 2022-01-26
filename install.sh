# Install dependencies
sudo pip install discord.py python-dotenv docker

# Uninstall old docker versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install docker
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt-get install docker-ce=5:20.10.12~3-0~ubuntu-focal docker-ce-cli=5:20.10.12~3-0~ubuntu-focal containerd.io

# Pull docker images used by this program
sudo docker pull python:3.9-alpine
sudo docker pull ubuntu:latest

# Print instructions
echo "Everything should be Installed correctly, make sure to run main.py as root"