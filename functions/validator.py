from models.enums import Language

class Validator():
    
    def __init__(self, language:Language):
        self.language = language

    def validate_string(self, question:str) -> str:
        '''summary_ Valida uma resposta para que não seja vazia.

        Args:
            question (str): Pergunta

        Returns:
            str: Resposta
        '''

        while True:
            answer = input(question).strip()
            if len(answer) > 0:
                break
            else:
                match self.language:
                    case Language.PT_BR:
                        print('Digite algo.')
                    case Language.ENG:
                        print('Type something.')
        return answer

    def validate_int(self, question:str) -> int:
        '''summary_ Valida uma resposta para que seja um inteiro.

        Args:
            question (str): Pergunta

        Returns:
            int: Resposta
        '''

        while True:
            answer = self.validate_string(question)
            if answer.isnumeric():
                break
            else:
                match self.language:
                    case Language.PT_BR:
                        print('Digite um valor.')
                    case Language.ENG:
                        print('Type a number.')
        return int(answer)

    def validate_option(self, max_options:int) -> int:
        '''summary_ Valida uma resposta para que seja um inteiro que esteja entre 1 e *max_options*.

        Args:
            max_options (int): Quantidade de opções

        Returns:
            int: Resposta
        '''

        match self.language:
            case Language.PT_BR:
                question = 'Digite uma opção: '
            case Language.ENG:
                question = 'Choose an option: '
        while True:
            answer = self.validate_int(question)
            if 0 < answer <= max_options:
                break
            else:
                match self.language:
                    case Language.PT_BR:
                        print(f'Digite uma opção entre 1 e {max_options}.')
                    case Language.ENG:
                        print(f'Choose an option between 1 and {max_options}.')
        return answer

    def validate_choices(self, title:str, choices:list[str]) -> int:
        '''summary_ Valida uma resposta para que seja um inteiro dentro das opções

        Args:
            title (str): Título do menu
            choices (list[str]): Lista de opções

        Returns:
            int: Opção escolhida
        '''
        print(f'---> {title}\n')
        for index, choice in enumerate(choices, start=1):
            print(f'[ {index} ] {choice}')
        print()
        return self.validate_option(len(choices))
