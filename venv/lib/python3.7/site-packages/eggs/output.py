"""
Define logger
"""
WARN = 'Warn'
ERROR = 'Error'


def output(message, level='info'):
    if level == 'error':
        print(message)
    elif level == 'warn':
        print(message)
    else:
        print(message)
