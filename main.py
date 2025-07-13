# Imports
from models.user import User
from functions.instructions import Instructions

import time
import keyboard
import pyautogui
import threading
import subprocess
from datetime import datetime

# Move cursor function
def move_cursor(positions:list[tuple[int, int]], instructions: Instructions) -> None:
    while not stop_event.is_set():
        for position in positions:
            try:
                pyautogui.moveTo(position)
                current_time = str(datetime.now())[11:19]
                print(f'{current_time} - X: {str(position[0]).ljust(4)} | Y: {str(position[1]).ljust(4)}')
            except Exception as exception:
                instructions.print_exception(exception)
            finally:
                time.sleep(1)
        print('')

# Check if the "S" key was pressed, and stop the program
def check_stop() -> None:
    global stop_event
    keyboard.wait('s')
    stop_event.set()

# Main
if __name__ == '__main__':
    
    user = User()
    instructions = Instructions()

    instructions.print_start(user.path)

    option = 0
    while option != 4:
        option = instructions.print_main_menu()
        match option:
            case 1:
            
                try:
                    # Open Teams
                    subprocess.Popen(['start', '', user.path], shell=True)
                    instructions.print_open_teams()

                    # Create the stop event
                    stop_event = threading.Event()

                    # Start the thread that moves the cursor
                    cursor_thread = threading.Thread(target=lambda: move_cursor(user.positions, instructions))
                    cursor_thread.start()

                    # Call check_stop() and wait until the user press "S"
                    check_stop()

                    # Wait until the cursor_thread terminates
                    cursor_thread.join()
                    instructions.print_stop()

                except Exception as exception:
                    instructions.print_exception(exception)
            
            case 2:
                instructions.set_language()
                instructions.print_start(user.path)
            
            case 3:
                user.path = instructions.set_path()
            
            case 4:
                instructions.input_end()
