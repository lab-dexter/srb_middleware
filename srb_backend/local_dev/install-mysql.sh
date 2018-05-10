#!/bin/bash

MYSQL=mysql57-community-release-el7-11.noarch.rpm

sudo yum update -y
sudo yum install wget vim -y
wget https://dev.mysql.com/get/${MYSQL}
sudo yum localinstall ${MYSQL} -y
sudo yum install mysql-server -y

sudo systemctl start mysqld
sudo systemctl status mysqld

sudo grep 'temporary password' /var/log/mysqld.log

echo "==============================================="
echo "After provisioning some manual steps to be done:"
echo "==============================================="
echo "1. vagrant ssh"
echo "2. sudo mysql_secure_installation"
echo "3. Paste temporary password from above and follow instructions."
echo "4. cd /vagrant/"
echo "5. Login with root user to mysql: 'mysql -u root -p'"
echo "6. Create DB and tables: 'source srb-setup-dev.sql'"
echo "7. Load dummy data: 'source srb-insert-data-dev.sql'"
# sudo mysql_secure_installation