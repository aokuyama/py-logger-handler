from logging import StreamHandler, DEBUG, INFO, WARN
import requests

class SlackHandler(StreamHandler):
    def __init__(self, webhook_url=None) -> None:
        self.webhook_url = webhook_url
        return super().__init__()

    def emit(self, record):
        self.post_message(self.format(record), record.levelno)

    def post_message(self, text, level):
        message = {
            'attachments': [
                {
                    'color': self.get_color(level),
                    'text': text,
                },
            ]
        }
        requests.post(self.webhook_url, json=message)

    def get_color(self, level):
        if level == DEBUG:
            return None
        elif level == INFO:
            return 'good'
        elif level == WARN:
            return 'warning'
        return 'danger'
