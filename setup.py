import os

if os.name  == 'posix':
    os.system('python -m venv .venv')
    os.system('cd .venv/bin/activate')
    os.system('pip install --no-index --find-links=./wheel/ -r requirements.txt')
    os.system('docker-compose up --build')
    