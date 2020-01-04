# django-slack-app [![Build Status](https://travis-ci.com/startmatter/django-slack-utils.svg?branch=master)](https://travis-ci.com/startmatter/django-slack-utils) [![Coverage Status](https://coveralls.io/repos/github/startmatter/django-slack-utils/badge.svg?branch=master)](https://coveralls.io/github/startmatter/django-slack-utils?branch=master)

Django app with Slack API



## Installation
Enter code in terminal
```python
docker-compose up -d --build 
docker-compose up -d 
```
Installed ngrok, start in terminal
```
./ngrok http 8000
```
copy "Forwarding https://12a3d5g5f1.ngrok.io" and enter in `https://api.slack.com/apps/ARNQHCQBG/event-subscriptions?` 
text. Exception "https://12a3d5g5f1.ngrok.io/slack/events"
## Settings
#### Export Slack value

1. Rename .env.example to .env
2. Write the value of the Slack bot without quotes to the file
3. Export the variables in the terminal using the command 
```
export $ (grep -v '^ #' .env | xargs -0)
```
4. Start the server

## Usage
#### Send message in chat

1. In `http://127.0.0.1:8000/slack/endpoint` enter title, body and url image
( exception: https://sitechecker.pro/wp-content/uploads/2017/12/URL-meaning.png)

2. To receive a response from the chat, write "Hello"


