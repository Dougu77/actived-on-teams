from models.enums import Language
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
        match self.language:
            case Language.PT_BR:
                title = 'Opções'
                choices = [
                    'Iniciar o programa',
                    'Mudar idioma',
                    'Mudar caminho do atalho do Teams',
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
        print()
        return self.validator.validate_choices(title, choices)
        

    def print_open_teams(self) -> None:
        match self.language:
            case Language.PT_BR:
                print('Abrindo o Teams...\n')
            case Language.ENG:
                print('Opening Teams...\n')

    def set_language(self) -> None:
        match self.language:
            case Language.PT_BR:
                title = 'Idioma'
                choices = [
                    'Português (Brasileiro)',
                    'Inglês'
                ]
            case Language.ENG:
                title = 'Language'
                choices = [
                    'Braziliam Portuguese',
                    'English'
                ]
        option = self.validator.validate_choices(title, choices)
        match option:
            case 1:
                self.language = Language.PT_BR
                self.validator.language = Language.PT_BR
            case 2:
                self.language = Language.ENG
                self.validator.language = Language.ENG

    def set_path(self) -> str:
        match self.language:
            case Language.PT_BR:
                question = 'Digite o caminho para o atalho: '
            case Language.ENG:
                question = 'Type the shortcut path: '
        return self.validator.validate_path(question)

    def print_stop(self) -> None:
        match self.language:
            case Language.PT_BR:
                print('Parando o programa...')
            case Language.ENG:
                print('Stopping the program...')

    def input_end(self) -> None:
        match self.language:
            case Language.PT_BR:
                input('Pressione ENTER para finalizar o programa...')
            case Language.ENG:
                input('Type ENTER to close the program...')

    def print_exception(self, exception:str) -> None:
        match self.language:
            case Language.PT_BR:
                print(f'Algo deu errado: "{exception}".')
            case Language.ENG:
                print(f'Something went wrong: "{exception}".')
        print()
