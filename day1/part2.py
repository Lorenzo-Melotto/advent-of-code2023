from utils import read_file, is_digit

def check_match(sub: str, nums: list[str]) -> bool:
    """Cheks whether or not the current substring is a possible
    spelled number. For example:

    ```python
    "thr" # is a possible substring of three
    "noz" # this substring cannot form any number
    ```
    """
    for k in nums:
        if k[:len(sub)] == sub:
            return True
    return False

def main() -> int:
    lines: list[str] = read_file("./calibration_doc.txt")
    tot: int = 0
    spelled_nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    spelled_nums_back = { k[::-1]: v for k, v in spelled_nums.items() }

    for l in lines:
        num: str = ""
        sub: str = ""
        # search from left to right
        for c in l:
            sub += c
            if not check_match(sub, list(spelled_nums.keys())):
                # if it's not a possibile substring, ditch all the 
                # other characters exept the one just read
                sub = sub[1:]
            if sub in spelled_nums.keys():
                num += spelled_nums[sub]
                break
            elif is_digit(c):
                num += c
                break
        sub: str = ""
        # search from right to left
        for c in l[::-1]:
            sub += c
            if not check_match(sub, list(spelled_nums_back.keys())):
                sub = sub[1:]
            if sub in spelled_nums_back.keys():
                num += spelled_nums_back[sub]
                break
            elif is_digit(c):
                num += c
                break
        assert len(num) == 2, f"Expected length 2, got {len(num)}"
        tot += int(num)
    return tot

if __name__ == "__main__":
    res: int = main()
    print(f"The result is: {res}")