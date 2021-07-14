class Data:
    """
    Save all the sentences can be searched in a dictionary format that includes all the word as the keys
    """

    def __init__(self):
        self.__list = []

    def get_sentence(self, index):
        return self.__list[index]

    def add(self, sentence):
        self.__list.append(sentence)
        return len(self.__list) - 1
