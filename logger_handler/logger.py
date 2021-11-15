from logging import getLogger, StreamHandler, DEBUG, INFO, CRITICAL
from slack_handler import SlackHandler

def get_logger(name=None, level=INFO):
    logger = get_default_logger(name)
    if logger.hasHandlers():
        return logger
    handler = get_stream_handler(level)
    logger.addHandler(handler)
    logger.propagate = False
    return logger

def get_default_logger(name):
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    return logger

def get_stream_handler(level=INFO):
    handler = StreamHandler()
    handler.setLevel(level)
    return handler

def get_test_logger():
    return get_logger('test', CRITICAL)

def get_slack_handler(url, level=INFO):
    handler = SlackHandler(url)
    handler.setLevel(level)
    return handler 

if __name__ == '__main__':
    logger = get_logger(level=DEBUG)
    import os
    handler = get_slack_handler(os.getenv('SLACK_WEBHOOK_URL'), level=CRITICAL)
    logger.addHandler(handler)
    logger.debug('ok.')
    logger.warning('warn...')
    logger.critical('ng!')
