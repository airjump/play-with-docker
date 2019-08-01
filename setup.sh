docker run -it debian
apt-get update
apt-get upgrade
apt-get install ansible git python-pip

mkdir ~/src
cd ~/src
git clone https://github.com/airjump/play-with-docker.git setup
cd setup
pip install --upgrade ansible
