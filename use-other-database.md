## how to use another database in your project instead of sqlite :
here is a quick look how to change settings.py to make project ready to use other databases :

* using postgresql :
```
// settings.py

DATABASES = {
  'default' : {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME' : 'your-desired-database-name',
    'HOST' : 'if you are in localhost leave it empty and if you are using a host add the host ip here',
    'USERNAME' : 'username of the database',
    'PASSWORD' : 'password of the database'
  }
}

```
note : to use postgresql you need to install `psycopg2` package.


* using mysql :
```
// settings.py
DATABASES = {
  'default' : {
    'ENGINE': 'django.db.backends.mysql',
    'NAME' : 'your-desired-database-name',
    'HOST' : 'if you are in localhost leave it empty and if you are using a host add the host ip here',
    'USERNAME' : 'username of the database',
    'PASSWORD' : 'password of the database'
  }
}
```
note : to use postgresql you need to install `mysqlclient` package.
