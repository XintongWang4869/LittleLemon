

build two APIs. One API to order food using the Menu API. You need to build the Table booking API to facilitate reserving a table for dining in the restaurant on a specific date and for a certain number of people.

By the end of this project, you will have built REST APIs for ordering food using the Menu API and reserving the table using the Booking API. 

project下的urls.py: url dispatcher

## Step-by-Step Guide

### Initial Setup

1. 创建remote repo

2. 创建并进入虚拟环境，安装 `django-admin`


3. `django-admin startproject littlelemon`  
    查看是否正常运行 cd littlelemon && python3 manage.py runserver

4. `python3 manage.py startapp restaurant`   
    add the app to **INSTALLED_APPS** in settings.py  
    push to git


### Models

1. Download [MySQL](https://www.mysql.com/downloads/).   

2. Using MYSQL Workbench to start running a local instance.

3. `pip3 install mysqlclient`      
    如这一步失败，可能需安装 sudo apt install default-libmysqlclient-dev    
    将 settings.py DATABASES 替换为 MYSQL   
    常见的MYSQL CLI commands: SHOW DATABASES; USE database_name; SHOW TABLES;

4. Declare models in models.py, and perform makemigrations & migrations. The corresponding tables will be created in the database (which can be confirmed by CLI or vscode extensions).

5. Import models in admin.py; Register the newly created models with the admin site using the `admin.site.register()`

Optionally: Create superuser with `python manage.py createsuperuser`; add data using the admin interface



## Troubleshooting

MySQL installed in windows whereas django project is in wsl2 (**the following code is less secure**):
* In MYSQL command line client:
```
CREATE USER 'root'@'%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

* In MYSQL configuration file (/etc/mysql/my.cnf), set bind-address to 0.0.0.0 to allow connections from any IP address.
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