import logging
import random
import time

# Configure logging
logging.basicConfig(
    filename="soc_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Example IP addresses
ips = [
    "192.168.1.5", "10.0.0.2", "185.22.33.44", "172.16.0.7",
    "203.0.113.15", "198.51.100.22", "185.99.11.12"
]

# Example usernames
users = ["admin", "root", "guest", "john", "mohamed", "eslam"]

# Log types
def generate_event():
    ip = random.choice(ips)
    user = random.choice(users)
    event_type = random.choice(["success", "fail", "suspicious", "malware", "ddos"])

    if event_type == "success":
        logging.info(f"User {user} login success from {ip}")
    elif event_type == "fail":
        logging.warning(f"Failed login attempt for {user} from {ip}")
    elif event_type == "suspicious":
        logging.error(f"Suspicious activity detected from IP {ip}")
    elif event_type == "malware":
        logging.critical(f"Malware detected on system - source {ip}")
    elif event_type == "ddos":
        logging.critical(f"Possible DDoS attack from {ip}")

# Generate logs continuously
if __name__ == "__main__":
    while True:
        generate_event()
        time.sleep(0.5)  # wait half a second to simulate real time
