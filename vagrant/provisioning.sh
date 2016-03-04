#!/usr/bin/env bash

# Store vagrant shared directory for reference
SHARED_DIRECTORY=/vagrant

# Store project directory for reference
PROJECT_DIRECTORY=$SHARED_DIRECTORY/surveys_rest_api

echo 'Resynchronizing package indexes'
apt-get update > /dev/null

echo 'Installing python development packages'
apt-get install -y python-setuptools python-dev > /dev/null

echo 'Installing pip python package manager'
easy_install pip > /dev/null

echo 'Installing Pillow (images processing library) dependencies'
apt-get install -y libtiff4-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk > /dev/null

echo 'Installing Django extensions dependencies'
apt-get install -y graphviz-dev graphviz pkg-config > /dev/null

echo 'Installing Git version control system'
apt-get install -y git > /dev/null

echo 'Installing full version of vim text editor'
apt-get install -y vim > /dev/null

echo 'Installing PostgreSQL database'
apt-get install -y postgresql libpq-dev > /dev/null

echo 'Creating vagrant PostgreSQL user'
sudo su - postgres -c 'createuser -s vagrant'

echo 'Creating vagrant database'
sudo su - postgres -c 'createdb vagrant'

echo 'Installing project dependencies (requirements file)'
pip install -r $SHARED_DIRECTORY/requirements/development.txt > /dev/null

# The following line fix the bug of flake8 not calling pyflakes
pip install --upgrade setuptools

echo 'Running project migration files'
sudo su - vagrant -c "python $PROJECT_DIRECTORY/manage.py migrate" > /dev/null

echo 'Prepending .bashrc_additions file to guest operating system .bashrc'
sudo su - vagrant -c 'sed -i "1i source ~/.bashrc_additions" ~/.bashrc'

