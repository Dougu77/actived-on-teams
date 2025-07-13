import os
import pyautogui

class User():
    
    def __init__(self):
        self.path = f'C:\\Users\\{os.getlogin()}\\Desktop\\Teams.lnk'
        self.positions = self.get_cursor_positions()
    
    def get_cursor_positions() -> list[tuple[int, int]]:
        screen_width, screen_height = pyautogui.size()
        padding = 10
        positions = [
            (padding, padding),
            (screen_width - padding, padding),
            (screen_width - padding, screen_height - padding),
            (padding, screen_height - padding)
        ]
        return positions
