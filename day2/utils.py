def read_file(file_name: str) -> list[str]:
    """Returns the lines in the file without the ending `\\n`"""
    lines: list[str] = []
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
    
    return lines