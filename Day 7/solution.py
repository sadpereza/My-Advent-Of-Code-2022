from re import search as re

def main():
    parsed_dirs = parse()
    print(get_total(parsed_dirs))
    
def parse():
    puzzle = open("Day 7/input.txt", "r")
    root = directory("/")
    path = root
    for line in puzzle:
        #print(line.strip())
        #print(path.name)

        m = re(r"^\$ cd (.+)$", line) # REGEX WIZARDRY
        if m: 
            target = m.group(1)
            #print(f"cding to {target}")
            path = path.get_item(target)

        m = re(r"^([0-9]+) ", line)
        if m:
            number = m.group(1)
            path.add_item(number)
        
        m = re(r"^dir (.+)$", line)
        if m:
            name = m.group(1)
            path.add_item(directory(name, path))

        #print("----------------")
    return root

def get_total(d, max_size = 100_000, running_sum = 0):
    size = d.get_size()
    if size <= max_size: running_sum += size
    for 
    return running_sum()

class directory:
    def __init__(self, name:str, parent = None, size = None):
        self.name = name
        self.parent = parent
        self.size = size
        self.contents = None
    
    def get_size(self):
        if self.size != None: return self.size
        if self.contents == None: raise Exception(f"Contents of directory {self.name} not defined!")

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
        if self.contents == None: raise Exception(f"Contents of directory {self.name} not defined!")
        if name == "..": return self.parent
        for item in self.contents:
            if type(item) == directory and item.name == name:
                return item
        raise Exception("Directory not found!")
    
    def sub_dirs(self):
        if self.contents == None: raise Exception(f"Contents of directory {self.name} not defined!")
    

if __name__ == "__main__": main()