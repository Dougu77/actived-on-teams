from models.enums import Language
from .validator import Validator

class Instructions():
    
    def __init__(self):
        self.language = Language.PT_BR
        self.validator = Validator(self.language)
    
    def print_line(self, size:int) -> None:
        print('-' * size)

    def print_start(self) -> None:
        match self.language:
            case Language.PT_BR:
                self.print_line(101)
                print(f'{'-' * 43} Ativo no Teams {"-" * 42}')
                self.print_line(101)
                print('\nEsse programa é responsável por mover o mouse pelos cantos da tela para simular estar ativo no Teams.\n')
            case Language.ENG:
                self.print_line(91)
                print(f'{"-" * 37} Actived on Teams {"-" * 36}')
                self.print_line(91)
                print('\nThis program moves the mouse cursor to the screen edges to simulate being actived on Teams.\n')

    def print_main_menu(self) -> int:
        match self.language:
            case Language.PT_BR:
                title = 'Opções'
                choices = [
                    'Iniciar o programa',
                    'Mudar idioma',
                    'Mudar caminho do atalhdo do Teams',
                    'Sair'
                ]
            case Language.ENG:
                title = 'Options'
                choices = [
                    'Start program',
                    'Change language',
                    'Change Teams shortcut path',
                    'Exit'
                ]
        return self.validator.validate_choices(title, choices)
        

    def print_open_teams(self):
        match self.language:
            case Language.PT_BR:
                print('Abrindo o Teams...\n')
            case Language.ENG:
                print('Opening Teams...\n')

    def print_stop(self):
        match self.language:
            case Language.PT_BR:
                print('Parando o programa...\n')
            case Language.ENG:
                print('Stopping the program...\n')

    def input_end(self):
        match self.language:
            case Language.PT_BR:
                input('Pressione ENTER para finalizar o programa...')
            case Language.ENG:
                input('Type ENTER to close the program...')
