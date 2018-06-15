sudo apt install python3-pip
sudo apt install virtualenv
sudo apt install postgresql-10 postgresql-contrib

echo -e "alias python=python3\nalias pip=pip3" ~/.bash_aliases	

sudo mkdir -m 777 /webapps
cd /webapps
virtualenv --python=python3 env

git clone git@github.com:rexzing/kolomthota_server.git

source env/bin/activate
pip install -r kolomthota_server/requirements.txt

echo "Pls setup the local_settings.py at kolomthota_server/ using the sample in kolomthota_server/local_settings.py.example"

