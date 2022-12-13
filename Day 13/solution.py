

def main():
    puzzle_input = open(r"Day 9/input.txt", "r")
    # TEST
    print("ABCDEFG"[0:7])
    parse_list("[3, 2, [1, 2, 3]]")
    puzzle_input.close()

def get_pair(file) -> tuple:
    line1 = file.readline()
    line2 = file.readline()
    file.readline() # skip blank line
    return (line1, line2)

def parse_list(line: str) -> list:
    line = line[1:-1] # strip off brackets
    
    temp = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            num = ""
            while i < len(line) and line[i].isdigit():
                num += line[i]
                i += 1
            temp.append(int(num))
        
        # pick out array, recurse
        elif line[i] == "[":
            start = i
            level = 0
            while not (line[i] == "]" and level == 1):
                if line[i] == "[": level += 1
                elif line[i] == "]": level += -1
                i += 1
            temp.append(parse_list(line[start:(i + 1)]))
        
        else: i += 1
    print(temp)
    return temp

    


# returns true if in correct order
def compare(list1: list, list2: list) -> bool:
    pass

if __name__ == "__main__": main()