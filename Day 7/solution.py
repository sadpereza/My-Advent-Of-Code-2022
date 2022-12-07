from re import search as re

def main():
    parse()


def parse():
    puzzle = open("Day 7/input.txt", "r")
    root = directory("/")
    path = root
    for line in puzzle:
        print(path.name)
        if re(r"^\$ cd", line):
            target = re(r"^\$ cd (.+$)", line).group(1)
            path = path.get_item(target)


class directory:
    def __init__(self, name:str, parent = None, size = None):
        self.name = name
        self.size = size
        self.contents = None
    
    def get_size(self):
        if not self.contents: raise Exception(f"Contents of directory {self.name} not defined!")
        if self.size != None: return self.size

        temp = 0
        for item in self.contents:
            if type(item) == int:
                temp += item
            elif type(item) == directory:
                temp += item.get_size()
        self.size = temp
    
    def add_item(self, item):
        if self.contents == None: self.contents = []
        self.contents.append(item)
    
    def get_item(self, name):
        for item in self.contents:
            if type(item) == directory and item.name == name:
                return item
        raise Exception("Directory not found!")
    

if __name__ == "__main__": main()