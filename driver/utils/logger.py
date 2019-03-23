import logging


class Logger:
    '''
    Logger Class
    <Constructor> Accepts filename for the log. If not provided, does not create a log file.
    <log> Accepts arguments to print in log
    '''

    logger = None

    def __init__(self, filename=None):
        self.logger = logging.getLogger("[AUTOBOTS]")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)s :: %(message)s')
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        if filename:
            file_handler = logging.FileHandler(filename)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def log(self, *args):
        args = map(str, args)
        msg = " :: ".join(args)
        self.logger.info(str(msg))
