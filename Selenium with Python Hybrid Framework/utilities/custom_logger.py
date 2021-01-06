import logging


class LogGen:

    @staticmethod
    def log_gen():
        logger = logging.getLogger()
        file_handler = logging.FileHandler(filename=".\\logs\\automation.log", mode='w')
        formatter = logging.Formatter(fmt="%(asctime)s: %(levelname)s: %(message)s",
                                      datefmt="%m%d%Y %I:%M:%S %p")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

        return logger
