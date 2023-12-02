import copy

from repository import Repository
import random


class Controller:
    def __init__(self, repository: Repository):
        self._repository = repository
        self._score = 0
        self._initialSentence = []
        self._scrambledSentence = []

        self._getRandomSentence()
        self._scrambleInitialSentence()
        self._previousStateOfScrambledSentence = copy.deepcopy(self._scrambledSentence)

    def _getRandomSentence(self):
        sentenceChosen = random.choice(self._repository.data).strip()
        self._initialSentence = sentenceChosen.split(' ')
        # self._scrambledSentence = self._initialSentence
        # self.saveSentence()
        self._computeInitialScore()
        return sentenceChosen

    def _scrambleInitialSentence(self):
        lettersToBeShuffled = []
        for word in self._initialSentence:
            for i in range(1, len(word) - 1):
                letter = word[i]
                lettersToBeShuffled.append(letter)
        random.shuffle(lettersToBeShuffled)

        indexOfLetterWhichNeedsToBeAddedToTheSentence = 0
        for word in self._initialSentence:
            numberOfNeededLetters = len(word) - 2
            scrambledWord = ''
            scrambledWord += word[0]
            for i in range(numberOfNeededLetters):
                scrambledWord += lettersToBeShuffled[indexOfLetterWhichNeedsToBeAddedToTheSentence]
                indexOfLetterWhichNeedsToBeAddedToTheSentence += 1
            scrambledWord += word[len(word) - 1]
            self._scrambledSentence.append(scrambledWord)

    def _updateScore(self):
        self._score -= 1

    def saveSentence(self):
        self._previousStateOfScrambledSentence = copy.deepcopy(self._scrambledSentence)

    def swapTwoLetters(self, firstWordId, firstLetterId, secondWordId, secondLetterId):
        if firstWordId < 0 or firstWordId >= len(self._scrambledSentence) or secondWordId < 0 or secondWordId >= len(self._scrambledSentence):
            raise ValueError
        if firstLetterId <= 0 or secondLetterId <= 0:
            raise ValueError
        if firstLetterId >= len(self._scrambledSentence[firstWordId]) - 1 or secondLetterId >= len(self._scrambledSentence[secondWordId]) - 1:
            raise ValueError

        self.saveSentence()
        letterFromFirstWord = self._scrambledSentence[firstWordId][firstLetterId]
        letterFromSecondWord = self._scrambledSentence[secondWordId][secondLetterId]
        self._scrambledSentence[firstWordId] = self._scrambledSentence[firstWordId][:firstLetterId] + letterFromSecondWord + \
                                               self._scrambledSentence[firstWordId][firstLetterId + 1:]
        self._scrambledSentence[secondWordId] = self._scrambledSentence[secondWordId][
                                               :secondLetterId] + letterFromFirstWord + \
                                               self._scrambledSentence[secondWordId][secondLetterId + 1:]
        self._updateScore()

    def _computeInitialScore(self):
        for word in self._initialSentence:
            for letter in word:
                self._score += 1

    def getWinner(self):
        winner = None
        if self._scrambledSentence == self._initialSentence:
            winner = 'player'
        elif self._score <= 0:
            winner = 'computer'
        return winner

    def undoLastSwap(self):
        self._scrambledSentence = copy.deepcopy(self._previousStateOfScrambledSentence)

    @property
    def scrambledSentence(self):
        sentenceAsString = ''
        for word in self._scrambledSentence:
            sentenceAsString += word + ' '
        return sentenceAsString.strip()

    @property
    def score(self):
        return self._score




def _test_Controller_Swap():
    inputFileName = 'input.txt'
    repository = Repository(inputFileName)
    controller = Controller(repository)
    controller._scrambledSentence = ['word', 'anotherWord']

    controller.swapTwoLetters(0, 1, 1, 3)
    assert controller.scrambledSentence == 'wtrd anooherWord'

def _test_Controller_Undo():
    inputFileName = 'input.txt'
    repository = Repository(inputFileName)
    controller = Controller(repository)
    controller._scrambledSentence = ['word', 'anotherWord']

    controller.swapTwoLetters(0, 1, 1, 3)
    controller.undoLastSwap()
    assert controller.scrambledSentence == 'word anotherWord'

def _test_Controller_scrambleInitialSentence():
    inputFileName = 'input.txt'
    repository = Repository(inputFileName)
    controller = Controller(repository)
    controller._initialSentence = ['1234', '12345678']
    controller._scrambledSentence = []
    controller._scrambleInitialSentence()

    assert len(controller._scrambledSentence[0]) == 4 and \
           len(controller._scrambledSentence[1]) == 8

def _test_Controller_updateScore():
    inputFileName = 'input.txt'
    repository = Repository(inputFileName)
    controller = Controller(repository)
    controller._score = 2
    controller._updateScore()
    assert controller._score == 1

def _test_Controller_getWinner():
    inputFileName = 'input.txt'
    repository = Repository(inputFileName)
    controller = Controller(repository)
    controller._initialSentence = ['word', 'anotherWord']
    controller._scrambledSentence = ['word', 'anotherWord']
    controller._score = 0
    assert controller.getWinner() == 'player'

    controller._scrambledSentence = ['word', 'another']
    assert controller.getWinner() == 'computer'

    controller._score = 1
    assert controller.getWinner() == None

if __name__ == '__main__':
    _test_Controller_Swap()
    _test_Controller_Undo()
    _test_Controller_scrambleInitialSentence()
    _test_Controller_updateScore()
    _test_Controller_getWinner()

