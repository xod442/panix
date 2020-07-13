# panix - **P**alo **A**lto **N**etwork **I**nterface e**X**ecutor
A flask framework for automatinf Palo Alto firewalls

## Setup
You will need a fresh install of Ubuntu Mate **Desktop** not server.
```
sudo apt-get install -y mongodb
sudo apt-get install -y python-dev
sudo apt-get install -y python-pip
```
This will get the DB and the mongo clients loaded. PIP will be used to install the rest of the requirements.

For each firewall you will need a CSV file like this:

![CSV File](/static/assets/spreadsheet.png)

A = Management IP of the PA firewall
B = Network assigned to subinterface
C = Not used...don't ask :-)
D = full subnet mask with slash and bits
E = Vlan TAG
F = Comment
G = Zone


## Get the app:
```
git clone://https.github.com/xod442/panix.github
cd panix
pip install requirement -r requirements.txt
```

## Launch the app:(from the panix folder)
```
python manage.py runserver
```
Point your web broswer to localhost:5001. You will see the login screen. You will need
the credentials to an **active** firewall.

Upon successful login, it is highly recommended to look at the help section.

**Note:**
This application uses a mongo database.
**Note:**
On
