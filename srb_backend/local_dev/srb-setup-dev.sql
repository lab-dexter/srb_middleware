
CREATE IF NOT EXISTS USER 'remote-admin'@'localhost' IDENTIFIED BY 'Some-pass!23';
GRANT IF NOT EXISTS ALL PRIVILEGES ON *.* TO 'remote-admin'@'localhost' WITH GRANT OPTION;
CREATE IF NOT EXISTS USER 'remote-admin'@'%' IDENTIFIED BY 'Some-pass!23';
GRANT IF NOT EXISTS ALL PRIVILEGES ON *.* TO 'remote-admin'@'%' WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS `smart-recycling-bins`;
USE `smart-recycling-bins`;

-- Creating 3 sensor tables for ESP with MAC 00-00-00-00-00-00
CREATE TABLE IF NOT EXISTS `00-00-00-00-00-00_1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `distance` FLOAT,
  `timestamp` TIMESTAMP(3),
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `00-00-00-00-00-00_2` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `distance` FLOAT,
  `timestamp` TIMESTAMP(3),
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `00-00-00-00-00-00_3` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `distance` FLOAT,
  `timestamp` TIMESTAMP(3),
  PRIMARY KEY (`id`)
);

-- Creating 3 sensor tables for ESP with MAC 11-11-11-11-11-11
CREATE TABLE IF NOT EXISTS `11-11-11-11-11-11_1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `distance` FLOAT,
  `timestamp` TIMESTAMP(3),
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `11-11-11-11-11-11_2` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `distance` FLOAT,
  `timestamp` TIMESTAMP(3),
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `11-11-11-11-11-11_3` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `distance` FLOAT,
  `timestamp` TIMESTAMP(3),
  PRIMARY KEY (`id`)
);

