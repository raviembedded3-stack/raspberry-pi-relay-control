# ============================================
# Project  : Raspberry Pi Relay Control
# Author   : C. P. Ravi
# Company  : Aislyn Technologies Pvt. Ltd.
# Description: Controls 3 relays using GPIO 
#              pins on Raspberry Pi
# Board    : Raspberry Pi
# ============================================

import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Define relay GPIO pin numbers
relay1 = 17  # Relay 1 connected to GPIO 17
relay2 = 27  # Relay 2 connected to GPIO 27
relay3 = 22  # Relay 3 connected to GPIO 22

# Configure relay pins as OUTPUT
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)

# Turn ON all relays (LOW = ON for relay module)
print("Turning ON all relays...")
GPIO.output(relay1, GPIO.LOW)
GPIO.output(relay2, GPIO.LOW)
GPIO.output(relay3, GPIO.LOW)

# Wait for 3 seconds
time.sleep(3)

# Turn OFF all relays (HIGH = OFF for relay module)
print("Turning OFF all relays...")
GPIO.output(relay1, GPIO.HIGH)
GPIO.output(relay2, GPIO.HIGH)
GPIO.output(relay3, GPIO.HIGH)

# Cleanup GPIO pins after use
GPIO.cleanup()
print("GPIO Cleanup done. Program ended.")
