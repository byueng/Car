# How to use
- In car_trade folder, `python .\car_backend\manage.py runserve <port [int]>`
- Or in car_backend folder, `python manage.py runserve <port [int]>`
```bash
System check identified no issues (0 silenced).
February 16, 2025 - 20:54:24
Django version 5.1.6, using settings 'car.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Any time these show server is OK.


# Folder structure
The root folder is `./car_trade`
> All commands contain file in this markdown file are **relative url**.
- car_trade: root
  - car_venv: python virtual environment
  - car_backend: backend using django
  - car_front: front mostly using Vue

## car_backend folder structure
- car_backend: backend root 
  - car: django apps settings 
  - cars: the app of folder contains car infomation
  - transaction: the app of folder contains transaction information
  - user_info: the app of folder contains user information


# environment setup
## Backend Python
**All the prerequisites(前提): python 3.13.1**
- First, create a virtual environment by `python -m venv <virtual name>`. If OS is Windows, then use `./<virtual name>/Scripts/Activate.ps1` in the folder which has ran the command of create virual environment, and use `source ./<virtual name>/bin/activate` in Linux.
- Second, install the third libaray by command `pip install -r requirements`, this command must be ran in the place where *requirements.txt* in.
- When install correctly, use `pip list` to viladate the status.
> All backend writen in `car_backend` folder and use django.

## backend x front


## Front Vue
- First, install Node.js. [https://nodejs.org/zh-cn](https://nodejs.org/zh-cn)
```bash
npm install -g @vue/cli
vue create my-project
```
All configurations are default.Then just run `npm run serve` and click the url.
- When modify the code, `npm run build` is needed.

## Mysql
- First, it must install **MySQL**, create relevant information in mysql:
In windows, it should run `net start mysql`, you need add `<mysql absolute path>/bin` in environment variables when the command errors.
Then, run `mysql -u <username> -p` then input password.
```mysql
create user 'username'@'%' identified by '';
grant all privileges on *.* to 'username'@'%';
flush privileges;
```

- Second, the settings file located in `./car_trade/car_backend/car/settings.py` in 78 lines. If want to modify, here's example:
```python
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'databasename',
        'USER': 'username',
        'PASSWORD': 'user password',
        'HOST': 'mysql client url', 
        'PORT': 'mysql client port',
    }
}
```
Or use the default `settings.py`.

- Third, run django server which says in Paragraph 1 **How to use** to validate whether mysql connect correctly.
If connections went right, then run command `python manage.py makemigrations` and `python manage.py migrate`

