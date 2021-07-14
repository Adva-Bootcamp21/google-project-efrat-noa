from data import Data
from trie import Trie
from insert_to_data import InsertToData


class Preparation:
    def __init__(self, data, trie, path):
        self.data = data
        self.trie = trie
        self.insert = InsertToData(data, trie, path)

    def start(self):
        self.insert.start()
