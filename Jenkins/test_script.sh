#!/bin/bash

sudo apt-get update
sudo apt install -y python3-pip

# Test Service 1
cd service_1
#python3 -m venv venv
#source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock flask_testing
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
#deactivate
cd ..

# Test Service 2
cd service_2
#python3 -m venv venv
#source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock flask_testing
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
#deactivate
cd ..

# Test Service 3
cd service_3
#python3 -m venv venv
#source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock flask_testing
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
#deactivate
cd ..

# Test Service 4
cd service_4
#python3 -m venv venv
#source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov requests_mock flask_testing
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
#deactivate
cd ..