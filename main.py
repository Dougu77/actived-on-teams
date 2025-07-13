# Imports
from functions.instructions import Instructions
from models.user import User
import pyautogui
from datetime import datetime
import time
import keyboard
import subprocess
import threading

# Move cursor function
def move_cursor(positions:list[tuple[int, int]]) -> None:
    while not stop_event.is_set():
        for position in positions:
            pyautogui.moveTo(position)
            current_time = str(datetime.now())[11:19]
            print(f'{current_time} - X: {position[0]} | Y: {position[1]}')
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

    instructions.print_start()

    option = 0
    while option != 4:
        option = instructions.print_main_menu()
        match option:
            case 1:
                
                # Open Teams
                instructions.print_open_teams()
                subprocess.Popen(['cmd', '/c', user.path])

                # Create the stop event
                stop_event = threading.Event()

                # Start the thread that moves the cursor
                cursor_thread = threading.Thread(target=lambda: move_cursor(user.positions))
                cursor_thread.start()

                # Call check_stop() and wait until the user press "S"
                check_stop()

                # Wait until the cursor_thread terminates
                cursor_thread.join()
                instructions.print_stop()
                
                # Exit the while
                break
            
            case 2:
                print(option)
            
            case 3:
                print(option)
            
            case 4:
                print(option)
                
    # Wait for the user to press anything
    instructions.input_end()
