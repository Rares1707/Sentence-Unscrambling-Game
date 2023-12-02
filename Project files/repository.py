
class Repository:
    def __init__(self, inputFileName):
        self._inputFileName = inputFileName
        self._data = []
        self._load()

    def _load(self):
        inputFile = open(self._inputFileName, 'r')
        for lineOfText in inputFile.readlines():
            self._data.append(lineOfText)
        inputFile.close()
    @property
    def data(self):
        return self._data

    def __len__(self):
        return len(self._data)





def _testRepository_init():
    inputFileName = 'input.txt'
    repository = Repository(inputFileName)
    assert len(repository) == 5

if __name__ == '__main__':
    _testRepository_init()