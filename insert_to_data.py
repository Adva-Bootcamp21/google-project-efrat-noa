from open_folders import OpenFolders


class InsertToData:
    def __init__(self, data, trie, path):
        self.folders = OpenFolders(path)
        self.path = path
        self.data = data
        self.trie = trie

    def start(self):
        self.folders.create_list(self.path)
        for file in self.folders:
            for line in file:
                string = line.replace("\n", "")
                index = self.data.add(string)
                string.replace("@", "").replace("!", "").replace("%", "")\
                    .replace("#", "").replace("*", "").replace("$", "").replace("^", "") + f"${index}"
                self.trie.insert(string)

