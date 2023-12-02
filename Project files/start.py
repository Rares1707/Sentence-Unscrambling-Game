from repository import Repository
from controller import Controller
from ui import Ui


if __name__ == '__main__':
    inputFileName = 'input.txt'
    gameRepository = Repository(inputFileName)
    gameController = Controller(gameRepository)
    gameUi = Ui(gameController)
    gameUi.startGame()
