from controller import Controller

class Ui:
    def __init__(self, controller: Controller):
        self._controller = controller

    def printError(self):
        print("Incorrect command")

    def executeCommand(self, command):
        if command.strip() == 'undo':
            self._controller.undoLastSwap()
            return
        command = command.strip().split(' ')
        if len(command) != 6:
            self.printError()
            return
        if command[0] != 'swap':
            self.printError()
            return
        if command[3] != '-':
            self.printError()
            return
        try:
            firstWordId = int(command[1])
            firstLetterId = int(command[2])
            secondWordId = int(command[4])
            secondLetterId = int(command[5])
        except ValueError as error:
            print(str(error) + ' wrong input')
            return
        try:
            self._controller.swapTwoLetters(firstWordId, firstLetterId, secondWordId, secondLetterId)
        except ValueError:
            print('error: values outside of bounds')
            return

    def startGame(self):
        while True:
            print(self._controller.scrambledSentence + ' [score is: ' + str(self._controller.score) + ']')

            winner = self._controller.getWinner()
            if winner == 'computer':
                print('defeat!')
                return
            if winner == 'player':
                print('victory! your score is', self._controller.score)
                return

            userCommand = input()
            self.executeCommand(userCommand)





