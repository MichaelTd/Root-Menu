import logging

class Logger:

    def __init__(self, class_name):
        self.logger = logging.getLogger(class_name)
        self.logger.setLevel(logging.INFO)

        self.file_handler = logging.FileHandler('system.log')
        self.file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(formatter)

        self.logger.addHandler(self.file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
