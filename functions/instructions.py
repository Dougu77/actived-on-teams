from models.constants import *
from .validator import Validator

class Instructions():
    
    def __init__(self) -> None:
        self.language = Language.PT_BR
        self.validator = Validator(self.language)
    
    def print_line(self, size:int) -> None:
        print('-' * size)

    def print_start(self, path:str) -> None:
        match self.language:
            case Language.PT_BR:
                self.print_line(104)
                print(f'{'-' * 44} Ativo no Teams {"-" * 44}')
                self.print_line(104)
                print('\n-> Esse programa é responsável por mover o mouse pelos cantos da tela para simular estar ativo no Teams.')
                print('-> Pressione "S" para encerrar a movimentação automatizada do mouse.')
                print(f'-> Caminho para o atalho: "{path}".')
            case Language.ENG:
                self.print_line(94)
                print(f'{"-" * 38} Actived on Teams {"-" * 38}')
                self.print_line(94)
                print('\n-> This program moves the mouse cursor to the screen edges to simulate being actived on Teams.')
                print('-> Press "S" to stop the mouse automatic moves.')
                print(f'-> Shortcut path: "{path}".')

    def print_main_menu(self) -> int:
        print()
        return self.validator.validate_choices(
            self.validator.get_choices(ChoiceKey.MAIN)
        )

    def print_open_teams(self) -> None:
        print(self.validator.get_message(MessageKey.INSTRUCTIONS_OPEN_TEAMS))

    def set_language(self) -> None:
        option = self.validator.validate_choices(
            self.validator.get_choices(ChoiceKey.LANGUAGE)
        )
        match option:
            case 1:
                self.language = Language.PT_BR
                self.validator.language = Language.PT_BR
            case 2:
                self.language = Language.ENG
                self.validator.language = Language.ENG

    def set_path(self) -> str:
        return self.validator.validate_path()

    def print_stop(self) -> None:
        print(self.validator.get_message(MessageKey.INSTRUCTIONS_STOP_TEAMS))

    def input_end(self) -> None:
        input(self.validator.get_message(MessageKey.INSTRUCTIONS_EXIT_PROGRAM))

    def print_exception(self, exception:str) -> None:
        print(f'{self.validator.get_message(MessageKey.INSTRUCTIONS_EXCEPTION)}{exception}".\n')
