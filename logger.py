import logging


def init_logger(name):
    logger_ = logging.getLogger(name)
    format_ = '%(asctime)s -:- %(levelname)s -:- %(name)s -:- %(message)s'
    logger_.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter(format_))
    console.setLevel(logging.DEBUG)
    info_debug = logging.FileHandler(filename="logs/info_debug.log")
    info_debug.setFormatter(logging.Formatter(format_))
    info_debug.setLevel(logging.DEBUG)
    err_warning = logging.FileHandler(filename="logs/err_warning.log")
    err_warning.setFormatter(logging.Formatter(format_))
    err_warning.setLevel(logging.WARNING)
    logger_.addHandler(console)
    logger_.addHandler(info_debug)
    logger_.addHandler(err_warning)
    logger_.debug("Логгер инициализирован")


