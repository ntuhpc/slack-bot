# Slack bot

> The bot we deployed to our Slack team

## Development

Create a Python 3 virtual environment and install dependencies listed in `requirements.txt`.

```bash
$ python3 -m venv venv
$ pip install -r requirements.txt
```

## Deployment

First obtain the API token from Slack website. Then obtain the bot id by running `print_bot_id.py`.

```bash
$ SLACK_BOT_TOKEN=<the-token> python print_bot_id.py
```

Then run the main script `enigma.py`.

```bash
$ SLACK_BOT_TOKEN=<the-token> BOT_ID=<bot-id> python enigma.py```
