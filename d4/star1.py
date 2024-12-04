input = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

total = 0

# Trouver le mot XMAS, en diagonale haut gauche, haut droit, bas gauche, bas droite, en haut, en bas, à gauche, à droite
def findCarac(caracSearch, line):
    pos = []
    start = 0

    while start < len(line):
        position = line.find(caracSearch, start)
        if position == -1:
            return [];
        
        pos.append(position)
        print(f"Caractère '{caracSearch}' => position {position}.")
        start = position + len(caracSearch)

    return pos

def searchInHorizontal(line, posFind): 
    countXmas = 0
    for p in posFind:
        print(len(line) - p)
        if(len(line) - p >= 4):
            # Regarder à droite
            if(line[p+1] == "M"):
                if(line[p+2] == "A"):
                    if(line[p+3] == "S"):
                        print(f"--find droite {line[p]} {line[p+1]} {line[p+2]} {line[p+3]}")
                        countXmas += 1
            # Regarder à gauche 
            if(line[p-1] == "M"):
                if(line[p-2] == "A"):
                    if(line[p-3] == "S"):
                        print(f"--find gauche {line[p]} {line[p-1]} {line[p-2]} {line[p-3]}")
                        countXmas += 1
    return countXmas

for i, line in enumerate(input):
    print(f"ligne {i}")
    posFind = findCarac("X", line)
    if(len(posFind) > 0):
        total += searchInHorizontal(line, posFind)

print(f"total: {total}")    
