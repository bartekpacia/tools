from ping import ping
from datetime import datetime

has_connection = ping("google.com")

time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{time_str}: {has_connection=}")
