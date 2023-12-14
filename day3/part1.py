from utils import read_file, is_digit
from dataclasses import dataclass

@dataclass
class num_coord():
    """Class that represents a digit and it's position
    + `digit`: the digit as a string
    + `r`: row
    + `c`: column
    """
    digit: str
    r: int
    c: int

def check_neigh(l: list[num_coord], es: list[str]) -> bool:
    """Checks if any neighbouring cell is a symbol. If so, returns `True`"""
    width: int = len(es)
    height: int = len(es[0])
    for e in l:
        for i in [-1, 0 , 1]:
            for j in [-1, 0 , 1]:
                new_i: int = (e.r+i) % height
                new_j: int = (e.c+j) % width
                el: str = es[new_i][new_j]
                if not is_digit(el) and el != ".":
                    return True
    return False

def main() -> int:
    es: list[str] = read_file("./input.txt")
    tot: int = 0
    acc: list[num_coord] = []
    for r in range(len(es)):
        for c in range(len(es[0])):
            if is_digit(es[r][c]):
                acc.append(num_coord(es[r][c], r, c))
            elif not is_digit(es[r][c]) and acc != []:
                if check_neigh(acc, es): 
                    num: str = ""
                    for e in acc: num += e.digit
                    tot += int(num)
                acc = []
    return tot
    
if __name__ == "__main__":
    res: int = main()
    print(f"The result is: {res}")