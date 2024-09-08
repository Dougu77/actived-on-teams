# Actived on Teams

## Informações

- O programa abre o Microsoft Teams e mexe o mouse para simular estar ativo.
- Pressione "S" para encerrar o programa.
- Não é possível encontrar o executával do Teams, por isso, o programa abre o atalho na Área se Trabalho.
- Baixe o repositório, e abra ele na sua IDE.
- Modifique o caminho do atalho para onde ele está no seu PC, assim: ```subprocess.Popen(['cmd', '/c', 'C:\\Users\\SeuNome\\Desktop\\Teams.lnk'])```
- Escolha o idioma do programa na variável ```language```, em ```main.py```
- Crie o ```.venv``` com o comando ```python -m venv .venv```
- Ative o ```.venv``` com o comando ```.\.venv\Scripts\activate```
- Baixe os pacotes usados no projeto com ```pip install -r requirements.txt```
- Crie o executável com ```pyinstaller -F -n "Actived on Teams" -i "icon.ico" main.py```

## Informations

- The program opens Microsoft Teams and moves the mouse cursor to simulate being actived.
- Type "S" to stop the program.
- Since it's impossible to find the executable file of Teams, the program opens the desktop shortcut.
- Download the repository, and open it in your IDE.
- Change the path to the shortcut to where it's in your PC, like: ```subprocess.Popen(['cmd', '/c', 'C:\\Users\\YourName\\Desktop\\Teams.lnk'])```
- Choose the language of the program in the variable ```language```, on ```main.py```
- Create the ```.venv``` with the command ```python -m venv .venv```
- Active the ```.venv``` with the command ```.\.venv\Scripts\activate```
- Download the packages of the project with ```pip install -r requirements.txt```
- Create the executable with ```pyinstaller -F -n "Actived on Teams" -i "icon.ico" main.py```
