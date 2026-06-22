import logging
import os

# Create logs folder if it does not already exist
os.makedirs('logs', exist_ok=True)

# Configure logging settings
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to record application activities in the log file
def log_action(msg):
    logging.info(msg)