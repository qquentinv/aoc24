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

input = []

with open("input.txt", "r") as file:
    for line in file:
        input.append(line)

print(input)

total = 0

# Trouver le mot XMAS, en diagonale haut gauche, haut droit, bas gauche, bas droite, en haut, en bas, à gauche, à droite
def findCarac(caracSearch, line):
    pos = []
    start = 0

    while start < len(line):
        position = line.find(caracSearch, start)
        if position == -1:
            break;
        
        pos.append(position)
        print(f"Caractère '{caracSearch}' => position {position}.")
        start = position + len(caracSearch)

    return pos

def searchInHorizontal(line, posFind): 
    countXmas = 0
    for p in posFind:
        if(len(line) - p >= 4):
            # Regarder à droite
            if(line[p+1] == "M"):
                if(line[p+2] == "A"):
                    if(line[p+3] == "S"):
                        print(f"--find droite {line[p]} {line[p+1]} {line[p+2]} {line[p+3]}")
                        countXmas += 1
        if(p - 3 >= 0):
            # Regarder à gauche 
            if(line[p-1] == "M"):
                if(line[p-2] == "A"):
                    if(line[p-3] == "S"):
                        print(f"--find gauche {line[p]} {line[p-1]} {line[p-2]} {line[p-3]}")
                        countXmas += 1
    return countXmas

def searchInVertical(input, posFind, i): 
    countXmas = 0
    for p in posFind:
        if(i+3 < len(input)):
            # Regarder en bas
            if(input[i+1][p] == "M"):
                if(input[i+2][p] == "A"):
                    if(input[i+3][p] == "S"):
                        print(f"--find bas {input[i][p]} {input[i+1][p]} {input[i+2][p]} {input[i+3][p]}")
                        countXmas += 1
        if(i-3 >= 0):
            # Regarder en haut
            if(input[i-1][p] == "M"):
                if(input[i-2][p] == "A"):
                    if(input[i-3][p] == "S"):
                        print(f"--find haut {input[i][p]} {input[i-1][p]} {input[i-2][p]} {input[i-3][p]}")
                        countXmas += 1
    return countXmas

def searchInDiagonal(input, line, posFind, i): 
    countXmas = 0
    for p in posFind:
        if(i+3 < len(input) and len(line) - p >= 4):
            # Regarder en bas à droite
            if(input[i+1][p+1] == "M"):
                if(input[i+2][p+2] == "A"):
                    if(input[i+3][p+3] == "S"):
                        print(f"--find bas droite {input[i][p]} {input[i+1][p+1]} {input[i+2][p+2]} {input[i+3][p+3]}")
                        countXmas += 1

        if(i+3 < len(input) and p - 3 >= 0):
            # Regarder en bas à gauche
            if(input[i+1][p-1] == "M"):
                if(input[i+2][p-2] == "A"):
                    if(input[i+3][p-3] == "S"):
                        print(f"--find bas gauche {input[i][p]} {input[i+1][p-1]} {input[i+2][p-2]} {input[i+3][p-3]}")
                        countXmas += 1

        if(i-3 >= 0 and len(line) - p >= 4):
            # Regarder en haut à droite
            if(input[i-1][p+1] == "M"):
                if(input[i-2][p+2] == "A"):
                    if(input[i-3][p+3] == "S"):
                        print(f"--find haut droite {input[i][p]} {input[i-1][p+1]} {input[i-2][p+2]} {input[i-3][p+3]}")
                        countXmas += 1

        if(i-3 >= 0 and p - 3 >= 0):
            # Regarder en haut à gauche
            if(input[i-1][p-1] == "M"):
                if(input[i-2][p-2] == "A"):
                    if(input[i-3][p-3] == "S"):
                        print(f"--find haut gauche {input[i][p]} {input[i-1][p-1]} {input[i-2][p-2]} {input[i-3][p-3]}")
                        countXmas += 1
        
    return countXmas

for i, line in enumerate(input):
    print(f"ligne {i}")
    posFind = findCarac("X", line)

    if(len(posFind) > 0):
        total += searchInHorizontal(line, posFind)
        total += searchInVertical(input, posFind, i)
        total += searchInDiagonal(input, line, posFind, i)

print(f"total: {total}")    
