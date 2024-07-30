# Import necessary libraries
import pyautogui
import time
import math
import logging
import keyboard

# Set up logging to display messages in the console
logging.basicConfig(level=logging.INFO, format='%(message)s')

try:
    # Loop indefinitely until manually stopped
    while True:
        # Log a message to indicate the circle movement is starting
        logging.info('Moving mouse in a circle...')
        
        # Move mouse in a circle
        for i in range(360):
            # Check if Esc button is pressed
            if keyboard.is_pressed('esc'):
                # Log a message to indicate the script has been stopped
                logging.info('Mouse movement stopped.')
                exit()
            
            # Calculate x and y coordinates for the circle
            x = math.cos(math.radians(i)) * 10
            y = math.sin(math.radians(i)) * 10
            
            # Move mouse to the calculated coordinates
            pyautogui.moveTo(x + 640, y + 360, duration=0.01)
        
        # Log a message to indicate the circle movement is complete
        logging.info('Circle movement complete. Waiting for 1 second...')
        
        # Wait for 1 second before moving the mouse again
        time.sleep(1)
except KeyboardInterrupt:
    # Log a message to indicate the script has been stopped
    logging.info('Mouse movement stopped.')