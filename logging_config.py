import logging

log_file = './messaging_system.log'

# Common logging configuration
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Create an in-memory log store
log_store = []

class InMemoryHandler(logging.Handler):
    def emit(self, record):
        log_store.append(self.format(record))

# Add the in-memory handler to the logger
in_memory_handler = InMemoryHandler()
in_memory_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logging.getLogger().addHandler(in_memory_handler)
