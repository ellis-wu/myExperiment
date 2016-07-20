# PHP Application

透過字串的搬移產生負載，總共分為兩支 `PHP` 程式：
* stress.php
* load.php

## How to use

安裝所需套件
```sh
$ sudo apt-get install -y apache2 php5 libapache2-mod-php5 php5-mcrypt
```
安裝完成後，將 `stress.php` 與 `load.php` 放至 `/var/www/html` 底下即可
```sh
$ sudo mv stress.php /var/www/html
$ sudo mv load.php /var/www/html
```
