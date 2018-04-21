# Local development environment for backend

## Tools needed
1. Virtual Box
2. Hashicorp Vagrant
Vagrant box: centos/7

## Setup
This will create centos7 local VM and install mysql database on it. 
VM has 3306 port forwarded to connect to the mysql db from the host.
srb-setup-dev.sql will create 'remote-admin' user for test&dev purposes. 

```
vagrant up
```
Some manual steps are still required to finish the setup. Follow the echoed instructions on the screen.
