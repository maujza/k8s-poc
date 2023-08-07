import logging

# Create a custom logger
logger = logging.getLogger('simple_app')
logger.setLevel(logging.INFO)

# Create handlers
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Create a console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(log_format)
console_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
