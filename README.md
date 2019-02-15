# cloudagileops

## Features

- Setup a simple [Django](https://www.djangoproject.com) application 'ToDolist' as an exmaple for elaborating the whole cloudOps workflow 

## ToDoList App

*Please notice this app is only used as an example, please DONOT use in production.*

Please first install Django version 1.11.18 to your machine.

After checkout the codes, execute the following:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 
```

By default, a development server at http://127.0.0.1:8000/ would be launched. 
Open the demo app via http://127.0.0.1:8000/admin. There is a default admin user with usr/pwd - "admin/1234abcd". However, you can create your superuser with:
```bash
$ python manage.py createsuperuser
```


## License

Apache 2.0

