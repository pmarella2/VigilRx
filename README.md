# VigilRx

## Setup Commands
Create and activate a Python environment (Linux):
```
python3 -m venv env
source env/bin/activate
```

Create and activate Python environment (Windows):
```
python3 -m venv env
source env\Scripts\activate.bat
```

Install Python dependences:
```
pip install -r requirements.txt
```

Install and run Ganache (Linux):
```
npm install ganache-cli web3
node_modules/.bin/ganache-cli
```

## Other Helpful Commands
Create a Django superuser:
```
python manage.py createsuperuser
```

Test migrations before making:
```
python manage.py makemigrations --dry-run
```

Make and apply Django migrations:
```
python manage.py makemigrations
python manage.py migrate
```

Install solc:
```
sudo add-apt-repository ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install solc
```
