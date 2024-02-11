import pywhatkit
import time

# Recipient number
recipient = '+917999785535'  # Replace with the desired recipient's number

# Message to be sent
message = 'Hello from Python'

# Specify the time for sending messages (24-hour format)
hour = 13
minute = 38

# Number of times to send the message
num_messages = 1

# Loop to send the message multiple times
for _ in range(num_messages):
    pywhatkit.sendwhatmsg(recipient, message, 13,39)
    time.sleep(1)  # Add a delay between messages to avoid issues

print(f"{num_messages} messages sent successfully.")