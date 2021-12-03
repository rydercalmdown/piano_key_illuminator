#!/bin/bash
#!/bin/bash
# install_pi.sh

echo "Installing base dependencies"
sudo apt-get update
sudo apt-get install -y python-pip \
    python3-pip \
    python3-pil \
    python3-numpy \
    gcc \
    make \
    build-essential \
    libjack-dev \
    libasound2-dev \
    libasound2 \

cd ../

echo "Installing python dependencies";
python3 -m pip install virtualenv

python3 -m virtualenv -p python3 env
. env/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r src/requirements.txt


echo "Setup complete";
