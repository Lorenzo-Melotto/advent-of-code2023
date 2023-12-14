from utils import read_file

def get_card_number(card: str) -> int:
    """Returns the card number"""
    card = card.split(":")[0][::-1] # get portion before ":" and reverse it
    card_num_rev: str = card[:card.index(" ")] # find first space
    return int(card_num_rev[::-1]) # reverse it again and parse to int

def main() -> int:
    cards: list[str] = read_file("./input.txt")
    tot_cards: dict[int, int] = { k + 1: 1 for k in range(len(cards)) }
    for card in cards:
        card_num: int = get_card_number(card)
        nums: str = card.split(":")[1]
        winning: list[str] = nums.split("|")[0].split(" ")
        winning = [w for w in winning if w != ""]
        my_num: list[str] = nums.split("|")[1].split(" ")
        my_num = [w for w in my_num if w != ""]
        matches: int = len(set(winning).intersection(set(my_num)))
        for i in range(card_num + 1, card_num + matches + 1):
            tot_cards[i] += 1 * tot_cards[card_num]
    return sum(tot_cards.values())

if __name__ == "__main__":
    res: int = main()
    print(f"The result is: {res}")
