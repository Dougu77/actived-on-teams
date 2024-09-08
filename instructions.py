supported_languages = ['pt-br', 'eng']

def print_start(language:str):
    if language not in supported_languages:
        language = 'pt-br'
    if language == 'pt-br':
        print('Começando o programa...\n')
    else:
        print('Starting the program...\n')

def print_open_teams(language:str):
    if language not in supported_languages:
        language = 'pt-br'
    if language == 'pt-br':
        print('Abrindo o Teams...\n')
    else:
        print('Opening Teams...\n')

def print_stop(language:str):
    if language not in supported_languages:
        language = 'pt-br'
    if language == 'pt-br':
        print('Parando o programa...\n')
    else:
        print('Stopping the program...\n')

def input_end(language:str):
    if language not in supported_languages:
        language = 'pt-br'
    if language == 'pt-br':
        input('Pressione ENTER para finalizar o programa...')
    else:
        input('Type ENTER to close the program...')
