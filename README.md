
# Convin Assignment 

Designing a Django project to fetch details of salesforce.

# Hi, I'm Ponith! 👋


## What's this about?


This is a simple GET API build with django and MySQL to get some of details of the salesforce without using third part framework.
## Run Locally using Python
Basic requirement of Xampp, MySQL, Python above 3

Clone the project

```bash
  git clone https://github.com/ran93r1210/Convin_assignment.git
```

Go to the project directory

```bash
  cd my-project
```


Setting up virtual environment

```bash
  python -m venv my-name-virtual-env
  source my-name-virtual-env/bin/activate 
```
Install dependencies

```bash
  pip install -r requirements.txt
```
To integrate MySQL with Django

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```


## Installation

[Documentation](https://github.com/ran93r1210/Convin_assignment/blob/main/documentation.txt)

Installation process.




## Screenshots
Home Page view

![App Screenshot](https://github.com/ran93r1210/Convin_assignment/blob/main/assets/Home_View.png?raw=true)

Users data 
![App Screenshot](https://github.com/ran93r1210/Convin_assignment/blob/main/assets/Users_List.png?raw=true)

Account and Contact data 
![App Screenshot](https://github.com/ran93r1210/Convin_assignment/blob/main/assets/Account_Contact.png?raw=true)





## Reference

#### Details of users, accounts and contacts in salesforce

```http
  GET /search/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `search` | `string` | **Required** ConsumerKey, ConsumerID,Username,Password |

#### Adding Driver details to database


#### GET details of all cars and drivers in database
```http
  GET /result/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `result`      | `string` | **-** |




## Tech Stack

**Client:** HTML, CSS

**Server:** Django


## Lessons Learned

Working with Django, salesforce integrations with python, salesforce.


