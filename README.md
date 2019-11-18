# Reviews API

[![Build Status](https://travis-ci.org/rrgaya/review-api.svg?branch=master)](https://travis-ci.org/rrgaya/review-api) [![Coverage Status](https://coveralls.io/repos/github/rrgaya/review-api/badge.svg?branch=master)](https://coveralls.io/github/rrgaya/review-api?branch=master)

This project is simple API. 

## Getting Started

This documentation shows how to install the development enviroment. This is Python3 and Django based project.


### Tech Stack 

-	Python3
-	Django
-	Django Rest framework

## Prerequisites

This may differ between Linux and MacOs platform. So take a look on these links:

* [Python3] - Script programming language 
* [Pip3] - Package manager for python
* [git] - Source code version manager


## Configuring the enviroment 

If the Python2 is installed it will conflict with Python3, so you should create a virutal enviroment.


### STEP 1: Get the source code

Create a folder to be the working directory and execute a git clone. If you don't have *access* or *user*, contact the [Administrator].

```bash
#SSH
git@github.com:rrgaya/review-api.git

# HTTP 
https://github.com/rrgaya/review-api.git
```

### STEP 2: Creating the environment

Access the folder created by git on the terminal shell and you must run the following command, where env is the name of the base directory for pip3 will install all project library without conflict or affect the machine libraries. Also will assure that only python3 will be running in the virtual environment.


```bash
$ python3 -m venv venv
```

### STEP 3: Activating the virtual enviroment

Run this commmand in the same folder where the env folder is located.

```bash
$ source env/bin/activate

```

### STEP 4: Installing the requirements

It's a good practice upgrade pip for the first time

```bash
$ pip3 install pip --upgrade

``` 
For the sake of simplicity all the requirements are in the file *requirementes.txt*

```bash
$ pip3 install  -r requirements.txt
``` 


### STEP 5: Creating the tables

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### STEP 6: Creating a super user for Django

```bash
$ python manage.py createsuperuser
```

### STEP 7: Loading the initial data

All required data for running the project and testing the application will be loaded using the following code:

```bash
$ python manage.py loaddata reviews/fixtures/initial_data_4tests.yaml
```

## Running the project 	


Every time you need to start the development enviroment to programming or test follow the step: 

1. Activate the virutal env

```bash
$ source venv/bin/activate
```

2. To starting the project run this command.

```bash
$ python manage.py runserver
```


## Get Token API

```bash
$  http :8000/token/ username="" password="" 
```

Response:

```bash
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 52
Content-Type: application/json
Date: Mon, 18 Nov 2019 18:01:03 GMT
Server: WSGIServer/0.2 CPython/3.7.5
X-Frame-Options: SAMEORIGIN

{
    "token": "a8011880f073443f75dfe3e6bf7d1ff49c4fe3be"
}
```
Ignore this Token, because this is example. Get the your Token.


## Get Reviews in API

```bash
$ http :8000/api/ "Authorization:Token a8011880f073443f75dfe3e6bf7d1ff49c4fe3be"
```

## Post an new Review

```bash
$ http POST :8000/api/post/ "Authorization:Token ac93c31f0ca3e758479520084dc1e8f3e4e41c4e" \  
company=1 \
rating=5 \
sumary="Sumary Example" \
title="Title Example" \
```


[Python3]: <https://www.python.org/downloads>
[Pip3]: <https://pip.pypa.io/en/stable/installing>
[git]: <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
[Docker]: <https://docs.docker.com/v17.12/install/#time-based-release-schedule>
[Administrator]: <mailto:rodrigues.ismael@gmail.com>
[localhost]: <http://localhost:8000/admin>
[Gitflow]: <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>
[gitflow-avh]: <https://github.com/petervanderdoes/gitflow-avh/wiki/Installing-on-Mac-OS-X>