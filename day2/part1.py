from utils import read_file

def get_game_id(game: str) -> int: 
    """Returns the game number"""
    return int(game[5 : game.index(":")])

def main() -> int:
    games: list[str] = read_file("./input.txt")

    tot_red: int = 12
    tot_green: int = 13
    tot_blue: int = 14

    games_id_sum: int = 0
    for g in games:
        game_id: int = get_game_id(g)
        sets: list[str] = g.split(":")[1].split(";") # get sets only
        is_game_possible: bool = True
        for s in sets:
            # get extracted cubes in curr set
            extracted: list[str] = s.split(",") 
            for cubes in extracted:
                cubes = cubes.lstrip(" ") # remove trailing space
                num: int = int(cubes.split(" ")[0]) # "5 green" -> [5, "green"]
                if "red" in cubes and num > tot_red:
                    is_game_possible = False
                    break
                elif "green" in cubes and num > tot_green:
                    is_game_possible = False
                    break
                elif "blue" in cubes and num > tot_blue:
                    is_game_possible = False
                    break
        if is_game_possible: games_id_sum += game_id
    return games_id_sum

if __name__ == "__main__":
    res: int = main()
    print(f"The result is: {res}")