import logging





logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(formatter)

# Write the logs to a file
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
