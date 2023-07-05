# Documentation for setting container environment

After deploying simplerisk image, you have to set some configuration so that the container can expose the mariaDB database.

## Deployment 
When deploying container, you have to use port-mapping 3307:3306, so that you can access to mariaDB of the container from localhost:3307.
- sudo docker run --name simplerisk -d -p 80:80 -p 443:443 -p 3307:3306 simplerisk/simplerisk

## Config MySQL config file and grant
After deploying container, you can only access to the database from in the container.
To access from localhost, you have to set bind address in the MySQL configuration file.
- The config file is /etc/mysql/mysql.conf.d/mysqld.cnf
- You have to change these variable so that you can access from localhost.
```Shell
user                    = mysql
bind-address            = 0.0.0.0
mysqlx-bind-address     = 0.0.0.0
```


## Summary Terminal Commands
```Shell
# Ubuntu terminal
$ sudo docker run --name simplerisk -d -p 80:80 -p 443:443 -p 3307:3306 simplerisk/simplerisk
$ docker exec -it [container id]  -- bash   # this command opens container terminal

# Container termianl
cd passwords
nano /etc/mysql/mysql.conf.d/mysqld.cnf   # here, change config file.
cat pass_mysql_root.txt   # this command shows the mysql root password. default password is uNTrIIwtCqcjLS64d7vJv
mysql -u root -p   # open mysql terminal. use default password to access.

# Here is mysql terminal
mysql> use mysql
mysql> CREATE USER 'simplerisk'@'%' IDENTIFIED BY 'simplerisk';
mysql> GRANT ALL ON *.* TO 'simplerisk'@'%';
mysql> FLUSH PRIVILEGES;

# Logout from Mysql terminal
service mysql restart   # restart mysql daemon

# Now, you can access to mariaDB in the container from localhost:3307 with user "simplerisk" and password "simplerisk"
```

## Run Python file

You can run python file to interact with the database.