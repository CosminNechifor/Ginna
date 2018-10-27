# Ginna

## Description

A telegram bot template ready to use for checking the status of your servers and webservices.

## How to install


### Manual

1. Clone the repo:
```
git clone https://github.com/CosminNechifor/Ginna
```

2. Read about Pipenv & Virtual Environments 
```
https://docs.python-guide.org/dev/virtualenvs/
```

3. Create a python3 venv and make sure you are in it by following the guide provided above

4. After creating a virtual env and making sure you are in it. Execute:

```
pip install -r requirements.txt
```

5. Add your telegram token to a file called token.txt

6. `` python main.py`` 


### Using a script(this was only tested on ubuntu18.04)

1. Clone the repo as mentioned above

2. Create a file named ``token.txt`` and paste your token there

3. Make sure you have docker installed, otherwise install it.

4. run the ``install.sh`` script 

## TODO

- Create Issues for every task that has to be implemented before starting working on it
- ~~Check if server is reachable~~ implemented in #2 
- ~~Perform requests to different webservices and return the text to the group chat that asked for the following requests~~ implemented in #4
- ~~Implement a request command to test services that are being developed~~ #4
- ~~Monitor different webservices on demand~~ implemented in #4
- ~~Having the one above create a project architecture that will be easy to extend on~~ No need, since it's only three files that have to be modified
- Ability to remove jobs 
- Create a CLI with the required options -> ``will be created when I decide what exactly should Gina do``
- Code refactor & exception handling ``will be done when we have more code``
- Create a testing moodule
- Create ``How to install ``
- ~~Automate deployment~~
- ~~Update description~~


## Future developement

- Monitoring prices over products available for sell in different shops and push notification on chat
- Security (allow only users with a specific token to use some of the functionalities)