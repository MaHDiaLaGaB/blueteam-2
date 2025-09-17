import logging

# Create logger
logger = logging.getLogger("CyberLogger")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("attacks.log")
file_handler.setLevel(logging.WARNING)  # Only warnings+ go to file

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Show everything on screen

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example logs
logger.debug("Scanning started...")
logger.info("Connection to server established")
logger.warning("Suspicious IP detected: 185.22.33.44")
logger.error("Failed login attempt from 185.22.33.44")
logger.critical("System breach detected!")
