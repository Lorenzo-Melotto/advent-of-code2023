def read_file(file_name: str) -> list[str]:
    """Returns the lines in the file without the ending `\\n`"""
    lines: list[str] = []
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
    
    return lines

def is_digit(c: str) -> bool:
    """Returns true if the character `c` is a digit"""
    assert len(c) == 1, "Input provided is not a single character." 
    return ord(c) >= 48 and ord(c) <= 57