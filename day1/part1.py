from utils import read_file, is_digit

def main() -> int:
    lines: list[str] = read_file("./calibration_doc.txt")

    tot: int = 0
    for l in lines:
        num: str = ""
        # find first digit reading from left to right
        for c in l:
            if is_digit(c):
                num += c
                break
        # find the second digit reading from right to left
        for c in l[::-1]:
            if is_digit(c):
                num += c
                break
        assert len(num) == 2, f"Expected length 2, got {len(num)}"
        tot += int(num) 
    return tot

if __name__ == "__main__":
    res: int = main()
    print(f"The result is: {res}")