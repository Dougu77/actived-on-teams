from .enums import Language

supported_languages = ['', '']


def validate_string(question:str, language:Language) -> str:
    while True:
        answer = input(question).strip()
        if len(answer) > 0:
            break
        else:
            match language:
                case Language.PT_BR:
                    print('Digite algo.')
                case Language.ENG:
                    print('Type something.')
    return answer

def validate_int(question:str, language:Language) -> int:
    while True:
        answer = validate_string(question)
        if answer.isnumeric():
            break
        else:
            match language:
                case Language.PT_BR:
                    print('Digite um valor.')
                case Language.ENG:
                    print('Type a number.')
    return int(answer)

def validate_option(max_options:int, language:Language) -> int:
    match language:
        case Language.PT_BR:
            question = 'Digite uma opção: '
        case Language.ENG:
            question = 'Choose an option: '
    while True:
        answer = validate_int(question)
        if 0 < answer <= max_options:
            break
        else:
            match language:
                case Language.PT_BR:
                    print(f'Digite uma opção entre 0 e {max_options}.')
                case Language.ENG:
                    print(f'Choose an option between 0 and {max_options}.')
    return answer

def print_choice(choices:list[str]) -> int:
    for choice in choices:
        print(f'[ {choices.index(choice) + 1} ] {choice}')
    
    
def print_start(language:Language):
    match language:
        case Language.PT_BR:
            print('-' * 36)
            print(f'{'-' * 10} Ativo no Teams {"-" * 10}')
            print('-' * 36)
            print('\nEsse programa é responsável por mexer o mouse pelos cantos da tela para simular estar ativo no Teams.')
    if language == 'pt-br':
        print('Começando o programa...\n')
    else:
        print('Starting the program...\n')

def print_open_teams(language:Language):
    if language not in supported_languages:
        language = 'pt-br'
    if language == 'pt-br':
        print('Abrindo o Teams...\n')
    else:
        print('Opening Teams...\n')

def print_stop(language:Language):
    if language not in supported_languages:
        language = 'pt-br'
    if language == 'pt-br':
        print('Parando o programa...\n')
    else:
        print('Stopping the program...\n')

def input_end(language:Language):
    if language not in supported_languages:
        language = 'pt-br'
    if language == 'pt-br':
        input('Pressione ENTER para finalizar o programa...')
    else:
        input('Type ENTER to close the program...')
