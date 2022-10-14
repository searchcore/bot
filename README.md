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
Just create venv in your bot's folder, activate it, install packages from 'requirements.txt'

### Setup
You can do it in two ways: OS specific and OS independent.  
##### First way, OS specific.  
You have to provide environment variables, listed in .env.dist  
  
Token from botfather  
`BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` 
  
DSN URL in SQLAlchemy format  
`BOT_DSN='sqlite+pysqlite:///:memory:'`  
  
Print additional info to console (True or False)  
`BOT_ECHO=False`  
  
##### Second way, OS independent.  
You can copy .env file with variables to installed bot folder, right next to cli.py  
If you made it by file and by environment, environment variables will be used. 


### Run
If you installed bot to venv, first activate it.
Then type `python -m bot` to console in your bot's folder.