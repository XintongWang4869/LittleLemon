django-admin startproject littlelemon

cd littlelemon
python3 manage.py runserver

python3 manage.py startapp restaurant

add the app to INSTALLED_APPS in settings.py

push to git



build two APIs. One API to order food using the Menu API. You need to build the Table booking API to facilitate reserving a table for dining in the restaurant on a specific date and for a certain number of people.


project下的urls.py: url dispatcher



mysql installed in windows whereas django project is in wsl2 (**the following code is less secure**):
* In MYSQL command line client:
```
CREATE USER 'root'@'%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

* In MYSQL configuration file (my.cnf), set bind-address to 0.0.0.0 to allow connections from any IP address.
```
[mysqld]
bind-address = 0.0.0.0
```

You can also use `cat /etc/resolv.conf | grep nameserver` to find the IP address of your Windows host (eg. 192.168.16.1).  
In this case, use the specified address instead of wild card '%', and change bind-address to the specific address.  
But MySQL does not support specifying multiple bind-address values directly in the configuration file. But you can set the bind-address to 0.0.0.0, and use firewall rules to restrict access to specific IP addresses.



Revoke Privileges (otherwise they will remain in effect even after the MySQL server is shut down and restarted)

```
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'root'@'%';
FLUSH PRIVILEGES;
```