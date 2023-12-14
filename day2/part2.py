from utils import read_file

def main() -> int:
    NEG_INF: int = int(-1e12)
    games: list[str] = read_file("./input.txt")

    tot: int = 0
    for g in games:
        max_red: int = NEG_INF
        max_green: int = NEG_INF
        max_blue: int = NEG_INF

        sets: list[str] = g.split(":")[1].split(";") # get sets only
        for s in sets:
            # get extracted cubes in curr set
            extracted: list[str] = s.split(",") 
            for cubes in extracted:
                cubes = cubes.lstrip(" ") # remove trailing space
                num: int = int(cubes.split(" ")[0]) # "5 green" -> [5, "green"]
                if "red" in cubes and num > max_red:
                    max_red = num
                elif "green" in cubes and num > max_green:
                    max_green = num
                elif "blue" in cubes and num > max_blue:
                    max_blue = num
        tot += max_red * max_green * max_blue
    return tot

if __name__ == "__main__":
    res: int = main()
    print(f"The result is: {res}")