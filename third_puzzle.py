import re

def parse_line(line):
    do = True
    regex_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)"
    match = re.search(regex_pattern, line)
    res = 0
    while match:
        instruction = match.group()
        index_end = match.end()

        if instruction == "do()":
            do = True
        elif instruction == "don't()":
            do = False
        
        elif do:
            multiplication = re.split(r"\(|\)|,", instruction)
            
            res += int(multiplication[1]) * int(multiplication[2])

        line = line[index_end:]
        match = re.search(regex_pattern, line)
    
    return res



def main():
    # Input parsing

    nb_safe_reports = 0
    with open("data/input_3.txt") as f:
        total = 0
        total += parse_line(f.read())
        print(total)


if __name__ == "__main__":
    main()