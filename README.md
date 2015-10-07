# BlockchainGambling [![Build Status](https://travis-ci.org/HarrisonGregg/BlockchainGambling.svg)](https://travis-ci.org/HarrisonGregg/BlockchainGambling)

This repository is for the Blockchain Gambling project for CS5356.

### Project Background

There are many sites that allow Bitcoin gambling, like Satoshibet, and making one (say for a different game of luck/skill) wouldn't be hard. But maybe we can use the public nature of the blockchain to determine winners (eg, pick winning lottery #s) in a transparently ungameable way?

### Project Management Tool

[Trello](https://trello.com/b/Daie0wKH/blockchain-gambling)

### Continuous Integration

On upload to GitHub, [Travis CI](https://travis-ci.org/HarrisonGregg/BlockchainGambling) automatically runs our Django unit tests and pushes all changes to Heroku if all tests pass.

### Development Server

[https://mighty-journey-2253.herokuapp.com/](https://mighty-journey-2253.herokuapp.com/)

### Developing Locally

1. Fork
2. Clone
3. Create virtual environment in cloned folder (python 3)
```
python -m virtualenv env
```
4. Install python requirements to virtual environment
```
env/bin/pip install -r requirements.txt
```
5. Start the server on localhost
```
env/bin/python manage.py runserver
```
6. Access at 127.0.0.1:8000