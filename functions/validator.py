from simpleValidatorForConsoleApp import validator as validatorPackage
from models.constants import *
import os

class Validator():
    
    def __init__(self, language:Language) -> None:
        self.language = language

    def validate_string(self, question:str) -> str:
        '''summary_ Valida uma resposta para que não seja vazia.

        Args:
            question (str): Pergunta

        Returns:
            str: Resposta
        '''

        return validatorPackage.validate_string(
            question,
            self.get_message(MessageKey.VALIDATE_STRING)
        )

    def validate_int(self, question:str) -> int:
        '''summary_ Valida uma resposta para que seja um inteiro.

        Args:
            question (str): Pergunta

        Returns:
            int: Resposta
        '''

        return validatorPackage.validate_int(
            question,
            self.get_message(MessageKey.VALIDATE_INT)
        )

    def validate_choices(self, data:tuple[str, list[str]]) -> int:
        '''summary_ Valida uma resposta para que seja um inteiro dentro das opções

        Args:
            title (str): Título do menu
            choices (list[str]): Lista de opções

        Returns:
            int: Opção escolhida
        '''

        choice = validatorPackage.validate_option(
            data[0],
            data[1],
            self.get_message(MessageKey.VALIDATE_OPTION_QUESTION),
            f'{self.get_message(MessageKey.VALIDATE_OPTION_ERROR)}{len(data[1])}.'
        )
        print()
        return choice

    def validate_path(self) -> str:
        '''summary_ Valida uma resposta para que seja um caminho de um arquivo que exista e seja um executável ou um atalho

        Returns:
            str: Caminho válido
        '''

        while True:
            answer = validatorPackage.validate_string(
                self.get_message(MessageKey.VALIDATE_PATH_QUESTION),
                self.get_message(MessageKey.VALIDATE_STRING)
            )
            if answer.startswith('"') and answer.endswith('"'):
                answer = answer[1:-1]
            if os.path.exists(answer):
                if answer.endswith('.exe') or answer.endswith('.lnk'):
                    break
                else:
                    print(self.get_message(MessageKey.VALIDATE_PATH_FORMAT))
                    continue
            else:
                print(self.get_message(MessageKey.VALIDATE_PATH_EXISTS))
        return answer

    def get_message(self, message:MessageKey) -> str:
        '''summary_ Consegue uma mensagem na constante dedicada

        Args:
            message (MessageKey): Chave no dicionário das mensagens

        Returns:
            str: Mensagem
        '''

        return MESSAGES[message][self.language.value]

    def get_choices(self, choice:ChoiceKey) -> tuple[str, list[str]]:
        '''summary_ Consegue uma lista de opções na constante dedicada

        Args:
            message (ChoiceKey): Chave no dicionário das opções

        Returns:
            tuple[str, list[str]]: Título do menu e lista de opções
        '''
        
        return (
            CHOICES[choice][self.language.value][0],
            CHOICES[choice][self.language.value][1]
        )
