from logging import DEBUG, INFO, WARN
from logging.handlers import HTTPHandler
import json


class SlackHandler(HTTPHandler):
    def get_color(self, level):
        if level == DEBUG:
            return None
        elif level == INFO:
            return 'good'
        elif level == WARN:
            return 'warning'
        return 'danger'

    def mapLogRecord(self, record):
        message = {
            'attachments': [
                {
                    'color': self.get_color(record.levelno),
                    'text': self.format(record),
                },
            ]
        }
        return {"payload": json.dumps(message)}
