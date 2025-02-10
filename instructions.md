

This project has built two REST APIs:

* The Menu API: used to order food 
* the Table booking API: used to facilitate reserving a table for dining in the restaurant on a specific date and for a certain number of people.




## Step-by-Step Guide

### Initial Setup

1. 创建remote repo

2. 创建并进入虚拟环境，安装 `django-admin`


3. 创建project: `django-admin startproject littlelemon .`  
    查看是否正常运行 cd littlelemon && python3 manage.py runserver.

4. 在project中创建app: `python3 manage.py startapp restaurant`.   
    Add the app to **INSTALLED_APPS** in "settings.py".  

5. Commit and push to git repo.


### Declare Models

1. Install MySQL

* On Windows, download [MySQL](https://www.mysql.com/downloads/). Use MYSQL Workbench to start running a local instance. Start MYSQL CLI client to check the running instance (Commonly used commands: SHOW DATABASES; CREATE DATABASE USE database_name; USE database_name; SHOW TABLES;)   
* On Linux:   
    * `sudo apt install mysql-server` python3-dev default-libmysqlclient-dev build-essential   
    * 启动 MYSQL: sudo systemctl start mysql (WSL2: `sudo service mysql start`)
    * 查看服务器状态：sudo service mysql status
    * sudo mysql_secure_installation
    <!-- * sudo systemctl enable mysql (WSL2: sudo update-rc.d mysql defaults) -->

* On MacOS: 
    * brew install mysql
    * brew services start/stop mysql
    * mysql_secure_installation 
    * mysql -u root -p (log in to MySQL as the root user)


2. 在项目的虚拟环境中，`pip3 install mysqlclient`.      
    Windows系统中如这一步失败，可能需安装 'sudo apt install default-libmysqlclient-dev'  
    
3. 将 "settings.py" DATABASES 替换为 MYSQL    
    注意若 MySQL 与 django 在同一环境中，则为localhost; 但若 MySQL 安装在 Windows 而 django 在WSL2系统中，localhost地址不同   
    

4. Declare models in models.py, and perform makemigrations & migrations. The corresponding tables will be created in the database (which can be confirmed by CLI or vscode extensions).

5. Import models in admin.py; Register the newly created models with the admin site using the `admin.site.register()`

Optionally: Create superuser with `python3 manage.py createsuperuser`; add data using the admin interface

---

Trouble-shooting:
* Test Database Connection: `python3 manage.py dbshell`   
    * 需注意：检查 mysqld.cnf (例如socket, bind-address)    
        ```
        [mysqld]
        user = mysql
        socket = /var/run/mysqld/mysqld.sock
        bind-address = 0.0.0.0
        ```
* 如果MySQL用户目录不存在：
    ```
    sudo service mysql stop
    sudo usermod -d /var/lib/mysql mysql
    sudo service mysql start
    ```

---

### Build REST APIs

1. `pip3 install djangorestframework`

> **Django REST Framework (DRF)** serializes the view response into JSON format and returns it to the client.  
> _Serialization_ involves converting the model instances (complex data) to native Python datatypes (JSON or XML) so that they can be rendered into JSON format.  
> _Deserialization_ parses the data back into the model instance after first validating the incoming data.  
> DRF views:    
> * function-based views:   
>    * Need to provide separate views for each method such as GET, POST, PUT and DELETE.
> * class-based views   
> * mixins
> * generics view classes
>      * ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
> * viewsets
>   * Can handle GET, POST, PUT and DELETE requests.


2. Add `rest_framework` to INSTALLED_APPS in "settings.py". 


3. Create **"serializers.py"** file in the app folder (`from rest_framework import serializers`).     
    Also need to import models.     


4. Develop views for the API in **views.py**: using class-based views here as example.      
    * For function-based views: return render(request, template, {context}) 
    * For viewsets/generics: 需定义 **queryset** (指定了视图将操作的model对象集) 如 User.objects.all()，同时也需定义上一步的 **serializer_class**
    

5. Update the URL configuration of the app as well as the project.      
    注意project下的urls.py，相当于 url dispatcher，可以 include('my_app.urls')

<br>

### User Authentication

#### djoser

* session-based authentication
* token-based authentication: djoser (DRF's TokenAuthentication)

Modify credentials within admin interface:

1. pip3 install djoser

2. In settings.py, include:
    ```
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'rest_framework.authtoken',
        'djoser',
        ...
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
    }

    DJOSER = {
        "USER_ID_FIELD": "username"
    }
    ```

<!-- admin.py:

    ```
    from django.contrib import admin
    from rest_framework.authtoken.models import Token
    admin.site.register(Token)
    ``` -->

2. Enable djoser endpoints by adding the following URL routes in the project's URL patterns.    
    ```
    #add following lines to update urlpatterns list
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
    ```

3. Run server and go to http://127.0.0.1:8000/auth/token/login, use user name and password to generate a token.


#### Restrict a view only for authenticated users

Modify credentials outside the app:

1. Add the 'rest_framework.authtoken' app to the list of INSTALLED_APPS in the settings.py file
2. In views.py, 'from rest_framework.permissions import IsAuthenticated'. Secure a view by adding `permission_classes = [IsAuthenticated]`
3. In the app's url, 'from rest_framework.authtoken.views import obtain_auth_token', and add a new route p'ath('api-token-auth/', obtain_auth_token)'.
4. Use insomnia Post method (or just use curl -x POST) to send username and password to the url 'api-token-auth/'.   
To get the response from a secured URL, select the Auth tab in Insomnia, choose the Bearer token from the drop down, and enter the token generated in the previous step and then press the send button.



## Troubleshooting

MySQL installed in windows whereas django project is in wsl2 (**the following code is less secure**):
* In MYSQL command line client:
```
CREATE USER 'root'@'192.168.16.1' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.16.1' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

* In MYSQL configuration file (/etc/mysql/my.cnf), set bind-address to 0.0.0.0 to allow connections from any IP address.
```
[mysqld]
bind-address = 192.168.16.1
```

Use `cat /etc/resolv.conf | grep nameserver` (ip addr | grep eth0) to find the IP address of your Windows host (eg. 192.168.16.1).  
Otherwise, you can also use the wild card '%', and change bind-address to 0.0.0.0.  

But MySQL does not support specifying multiple bind-address values directly in the configuration file. But you can set the bind-address to 0.0.0.0, and use firewall rules to restrict access to specific IP addresses.



Revoke Privileges (otherwise they will remain in effect even after the MySQL server is shut down and restarted)

```
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'root'@'%';
FLUSH PRIVILEGES;
```