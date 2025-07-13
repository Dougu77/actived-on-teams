import os
import pyautogui

class User():
    
    def __init__(self) -> None:
        self.path = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Microsoft\\WindowsApps\\ms-teams.exe'
        self.positions = self.get_cursor_positions()
    
    def get_cursor_positions(self) -> list[tuple[int, int]]:
        width, height = pyautogui.size()
        padding = 10
        return [
            (padding, padding),
            (width - padding, padding),
            (width - padding, height - padding),
            (padding, height - padding)
        ]
