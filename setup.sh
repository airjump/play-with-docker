apt-get -y install python-pip git python-dev
mkdir ~/src
cd ~/src
git clone https://github.com/airjump/play-with-docker.git setup
cd setup
pip install --upgrade ansible
