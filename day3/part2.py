from utils import read_file, is_digit

def extract_num(r: int, c: int, es: list[str]) -> int:
    width: int = len(es[0])
    num: str = ""
    # go back to first char that is not a digit
    while is_digit(es[r][c]):
        c -= 1
        if c < 0: break # stop at the beginning of the board
    c += 1

    # go forward untill a . or a * is reached
    while es[r][c] != "." and es[r][c] != "*":
        num += es[r][c]
        c += 1
        if c >= width: break # stop at the end of the board
    
    return int(num)

def get_neigh(r: int, c: int, es: list[str]) -> list[int]:
    neigh_nums: set[int] = set()
    height: int = len(es)
    width: int = len(es[0])
    # check 3x3 grid around the cog
    for i in [-1, 0, 1]: 
        for j in [-1, 0, 1]:
            new_i = (r+i) % height # wrap lines. Don't know if necessary
            new_j = (c+j) % width
            el: str = es[new_i][new_j]
            if is_digit(el):
                neigh_nums.add(extract_num(new_i, new_j, es))
    return list(neigh_nums)

def main() -> int:
    es: list[str] = read_file("./input.txt")
    tot_gr: int = 0
    height: int = len(es)
    width: int = len(es[0])
    for r in range(height):
        for c in range(width):
            if es[r][c] == "*":
                neigh_nums: list[int] = get_neigh(r, c, es)
                neigh_count: int = len(neigh_nums)
                if neigh_count == 2:
                    tot_gr += neigh_nums[0] * neigh_nums[1]
    return tot_gr

if __name__ == "__main__":
    res: int = main()
    print(f"The result is: {res}")