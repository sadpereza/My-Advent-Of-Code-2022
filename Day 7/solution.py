def main():
    parse()

def parse():
    puzzle = open("Day 7/input.txt", "r")
    root = directory("/")
    path = None
    for line in puzzle:
        if line[0] == "$":
            if line.re(r"$ (.+)"):
                pass
        else:
            pass

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
        self.contents.append(item)
    

if __name__ == "__main__": main()