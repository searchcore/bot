# Bot template
Bot template for aiogram~=3.0.0b4 with configured must-have modules:
- aiogram-dialog
- fluentogram
- SQLAlchemy (sync mode for now)

## Bot architecture
I tried to make bot architecture as clear as possible, however it's hard to isolate aiogram_dialog.  
So there is folder 'handlers/dialog' for your aiogram_dialog dialogs.  
Folder 'services' contains facades for localizator(fluentogram) and repository(SQLAlchemy's ORM-sessions).  
Also it contains 'integration' folder for code that should bind together aiogram extensions.  
__Be careful!__ there is a little mess with middlewares, so it's tricky to send data to dialogs.

## Bot features
- integration.LocaleText - my dummy realization of Text widget for aiogram_dialog with fluent_translator as 'text-backend'
    - __Be careful!__ there is a little mess with middlewares, so it's tricky to send data to dialogs. For example, when you press the button in dialog aiogram_dialogs tries to render it's content, but if you didn't provide callback_query - middleware dialog wont be able to get localizator and repo_user!
## Setup

### Installation

#### From folder
1. Go to root folder with pyproject.toml
2. Run `pip install ./`
4. Copy folder with locale files to your bot's directory (or anywhere you want)
#### From *.tar.gz
1. Go to folder with *.tar.gz
2. __Optional__ you can install bot to global environment or to virtual environment. If you want to place your bot into the current folder, do the following:  
    1. `python -m venv venv`
    2. [Activate your virtual environment](https://docs.python.org/3/tutorial/venv.html#:~:text=Once%20you%E2%80%99ve%20created%20a%20virtual%20environment%2C%20you%20may%20activate%20it.) (It depends on your OS)
3. `pip install path/to/bot.tar.gz`
4. Copy folder with locale files to your bot's directory (or anywhere you want)
__If you installed your bot with venv,__  
you have to activate your virtual env every time you want to run your bot.
When you stop your bot, it's recommended to execute `deactivate` to leave venv.

### Distribution
1. Go to root folder with pyproject.toml
2. Run `python -m build`
3. Use *.whl and *.tar.gz files under `./dist/` folder to install bot  
Don't forget to provide locale files!

### Setup
You can do it in two ways: OS specific and OS independent.  
First way, OS specific.  
You have to provide environment variables, listed in .env.dist  
  
Token from botfather  
`TGBOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` 
  
DSN URL in SQLAlchemy format  
`TGBOT_DSN='sqlite+pysqlite:///:memory:'`  
  
Print additional info to console (True or False)  
`TGBOT_ECHO=False`  
  
Absolute path to folder with bot's locale files  
`TGBOT_LOCALES_FOLDER='path/to/locales'`  
  
Second way, OS independent.  
You can copy .env file with variables to installed bot folder, right next to cli.py  
If you made it by file and by environment, environment variables will be used. 


### Run
If you installed bot to venv, first activate it.
Then type `tgbot` to console.
