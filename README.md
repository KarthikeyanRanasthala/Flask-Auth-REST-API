# Flask Authenication REST API

## Built With

- Flask
- JWT
- MySQL

## Usage

1. Clone the repository and change directory

```bash
git clone https://github.com/karthikeyanranasthala/Flask-Auth-REST-API.git
cd Flask-Auth-REST-API
```

2. Setup Python VirtualEnv and activate.

```bash
virtualenv -p <path_to_python_installation> venv
source venv/bin/activate
```

3. Install the required packages.

```bash
pip install -r requirements.txt
```

4. Setup environment variables in `.env` file.

```
MYSQL_USER="<username>"
MYSQL_PASSWORD="<password>"
MYSQL_DB="<database>"
JWT_SECRET_KEY="SomeRandomSecretPhrase"
```

5. Start the server.

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

## Features

- Register User
- Hash Password using PBKDF2
- Login User
