# Actived on Teams

## Informações

- O programa abre o Microsoft Teams e mexe o mouse para simular estar ativo.
- Não é possível encontrar o executával do Teams, por isso, o programa abre o atalho na Área se Trabalho.
- Baixe o repositório, e abra ele na sua IDE.
- Crie um arquivo ```.env``` e coloque ```TEAMS_PATH=Caminho/Do/Atalho```
- Crie o ```.venv``` com o comando ```python -m venv .venv```
- Ative o ```.venv``` com o comando ```.\.venv\Scripts\activate```
- Baixe os pacotes usados no projeto com ```pip install -r requirements.txt```
- Crie o executável com ```pyinstaller -F -n "Actived on Teams" -i "icon.ico" main.py```

## Informations

- The program opens Microsoft Teams and moves the mouse cursor to simulate being actived.
- Since it's impossible to find the executable file of Teams, the program opens the desktop shortcut.
- Download the repository, and open it in your IDE.
- Create an ```.env``` file and add ```TEAMS_PATH=Path/To/Shortcut```
- Create the ```.venv``` with the command ```python -m venv .venv```
- Active the ```.venv``` with the command ```.\.venv\Scripts\activate```
- Download the packages of the project with ```pip install -r requirements.txt```
- Create the executable with ```pyinstaller -F -n "Actived on Teams" -i "icon.ico" main.py```
