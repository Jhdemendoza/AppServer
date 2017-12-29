#!/usr/bin/python

import os

os.system("mkdir /mnt/nas")
os.system("mount -t glusterfs 10.1.4.21:/nas /mnt/nas")

os.system('curl -sL https://deb.nodesource/setup_8.x | bash -')
os.system('apt-get update')
os.system('apt-get install -y nodejs')

os.system('git clone https://github.com/CORE-UPM/CRM_2017.git')
os.chdir('./CRM_2017')
os.system('npm install')