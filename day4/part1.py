from utils import read_file

def main() -> int:
    cards: list[str] = read_file("./input.txt")
    tot: int = 0
    for card in cards:
        nums: str = card.split(":")[1]
        winning: list[str] = nums.split("|")[0].split(" ")
        winning = [w for w in winning if w != ""]
        my_num: list[str] = nums.split("|")[1].split(" ")
        my_num = [w for w in my_num if w != ""]
        curr_tot: int = 0
        for n in my_num:
            if n in winning:
                if curr_tot == 0: curr_tot = 1
                else: curr_tot *= 2
        tot += curr_tot
    return tot

if __name__ == "__main__":
    res: int = main()
    print(f"The result is: {res}")