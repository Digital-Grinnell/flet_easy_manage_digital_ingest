# enhanced_logger.py

# A more advanced logging setup with multiple handlers and formatting created by PerplexityAI from:
#   Create a Python module and class that adds functionality to my Python logger.

import logging

class EnhancedLogger:

    page = None

    def __init__(self, name, log_file=None, level=logging.INFO, page=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        # File Handler (optional)
        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        # Adding contextual information if page is provided
        if page is not None:
            self.page = page


    def info(self, msg):
        self.logger.info(msg)
        if self.page:   
            self.page.session.set("last_status", f"info: {msg}")

    def warning(self, msg):
        self.logger.warning(msg)
        if self.page:   
            self.page.session.set("last_status", f"warning: {msg}")

    def error(self, msg):
        self.logger.error(msg)
        if self.page:   
            self.page.session.set("last_status", f"error: {msg}")

    def debug(self, msg):
        self.logger.debug(msg)
        if self.page:   
            self.page.session.set("last_status", f"debug: {msg}")

    def set_level(self, level):
        self.logger.setLevel(level)
        if self.page:   
            self.page.session.set("last_status", f"set-level: Logging level set to {level}")
