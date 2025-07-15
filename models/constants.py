from enum import Enum

# Enums
class Language(Enum):
    PT_BR = 0
    ENG = 1

class MessageKey(Enum):
    VALIDATE_STRING = 0
    VALIDATE_INT = 1
    VALIDATE_OPTION_QUESTION = 2 
    VALIDATE_OPTION_ERROR = 3
    VALIDATE_PATH_QUESTION = 4
    VALIDATE_PATH_FORMAT = 5
    VALIDATE_PATH_EXISTS = 6
    INSTRUCTIONS_OPEN_TEAMS = 7
    INSTRUCTIONS_STOP_TEAMS = 8
    INSTRUCTIONS_EXIT_PROGRAM = 9
    INSTRUCTIONS_EXCEPTION = 10

class ChoiceKey(Enum):
    MAIN = 0
    LANGUAGE = 1

# Consts
MESSAGES = {
    MessageKey.VALIDATE_STRING: (
        'Digite algo.', 'Type something.'
    ),
    MessageKey.VALIDATE_INT: (
        'Digite um valor.', 'Type a number.'
    ),
    MessageKey.VALIDATE_OPTION_QUESTION: (
        'Digite uma opção: ', 'Choose an option: '
    ),
    MessageKey.VALIDATE_OPTION_ERROR: (
        'Digite uma opção entre 1 e ', 'Choose an option between 1 and '
    ),
    MessageKey.VALIDATE_PATH_QUESTION: (
        'Digite o caminho para o atalho: ', 'Type the shortcut path: '
    ),
    MessageKey.VALIDATE_PATH_FORMAT: (
        'Digite o caminho de um arquivo .exe ou .lnk.', 'Type an path of an .exe or .lnk file.'
    ),
    MessageKey.VALIDATE_PATH_EXISTS: (
        'Digite um caminho que exista.', 'Type an path that exists.'
    ),
    MessageKey.INSTRUCTIONS_OPEN_TEAMS: (
        'Abrindo o Teams...\n', 'Opening Teams...\n'
    ),
    MessageKey.INSTRUCTIONS_STOP_TEAMS: (
        'Parando o programa...', 'Stopping the program...'
    ),
    MessageKey.INSTRUCTIONS_EXIT_PROGRAM: (
        'Pressione ENTER para finalizar o programa...', 'Type ENTER to close the program...'
    ),
    MessageKey.INSTRUCTIONS_EXCEPTION: (
        'Algo deu errado: "', 'Something went wrong: "'
    )
}

CHOICES = {
    ChoiceKey.MAIN: (
        ('---> Opções', [
            'Iniciar o programa',
            'Mudar idioma',
            'Mudar caminho do atalho do Teams',
            'Sair'
        ]),
        ('---> Options', [
            'Start program',
            'Change language',
            'Change Teams shortcut path',
            'Exit'
        ])
    ),
    ChoiceKey.LANGUAGE: (
        ('---> Idiomas', ['Português (Brasileiro)', 'Inglês']),
        ('---> Languages', ['Braziliam Portuguese','English'])
    )
}
