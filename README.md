# Simple Django Websockets based chat app

## Features

- Registeration and authentication  
- Create new rooms or join already exiting ones
- Sending and recieving Private Messages


## Start your app

1- Creating a new virtual enviroment :
```
python3.9 -m venv myvenv
```

2- Activate the virtual enviroment :

**Windows**
```
myvenv/Scripts/activate
```

**Linux**
```
source myvenv/bin/activate
```

3- Install project requirements :
```
pip install -r requirements.txt
```

4- Make migrations :
```
python manage.py makemigrations
```

5- Migrate :
```
python manage.py migrate
```
6- Setup email sending service (to send activation tokens and reset password), by adding email and pasword in ecommerce/settings.py

7- Finally, run the development server :
```
python manage.py runserver 
```



