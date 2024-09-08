import pyautogui
from datetime import datetime
import time
import keyboard
import subprocess
import threading
import instructions

# Define language (pt-br or eng)
language = 'pt-br'

# Define the 4 cursor positions
def define_cursor_positions():
    screen_width, screen_height = pyautogui.size()
    padding = 10
    positions = [
        (padding, padding),
        (screen_width - padding, padding),
        (screen_width - padding, screen_height - padding),
        (padding, screen_height - padding)
    ]
    return positions

# Move cursor function
def move_cursor(positions:list[tuple[int, int]]):
    while not stop_event.is_set():
        for position in positions:
            pyautogui.moveTo(position)
            horario = str(datetime.now())[11:19]
            print(f'{horario} - X: {position[0]} | Y: {position[1]}')
            time.sleep(1)
        print('')

# Check if the "S" key was pressed, and stop the program
def check_stop():
    global stop_event
    keyboard.wait('s')
    stop_event.set()

# Main
if __name__ == "__main__":

    # Start message
    instructions.print_start(language)

    # Set the positions list
    positions = define_cursor_positions()

    # Open Teams shortcut
    subprocess.Popen(['cmd', '/c', 'C:\\Users\\Douglas\\Desktop\\Teams.lnk'])
    instructions.print_open_teams(language)

    # Create the stop event
    stop_event = threading.Event()

    # Start the thread that moves the cursor
    cursor_thread = threading.Thread(target=lambda: move_cursor(positions))
    cursor_thread.start()

    # Call check_stop() and wait until the user press "S"
    check_stop()

    # Wait until the cursor_thread terminates
    cursor_thread.join()
    instructions.print_stop(language)
    
    # Wait for the user to press anything
    instructions.input_end(language)
