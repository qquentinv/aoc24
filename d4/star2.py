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

total = 0

# Trouver le mot MAS en forme de X, en diagonale haut gauche, haut droit, bas gauche, bas droite
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

def searchInDiagonal(input, line, posFind, i): 
    countXmas = 0

    for p in posFind:
        countDiago = 0
        # Diagonale 1
        if(i+1 < len(input) and len(line) - p >= 2 and i-1 >= 0 and len(line) - p >= 2):
            # Regarder en haut à droite vers bas gauche
            if(input[i+1][p+1] == "M"):
                if(input[i-1][p-1] == "S"):
                        print(f"--find MAS")
                        countDiago += 1
            elif(input[i+1][p+1] == "S"):
                if(input[i-1][p-1] == "M"):
                        print(f"--find SAM")
                        countDiago += 1


        # Diagonale 2
        if(i+1 < len(input) and len(line) - p >= 2 and i-1 >= 0 and len(line) - p >= 2):
            # Regarder en haut à gauche vers bas droite
            if(input[i-1][p+1] == "M"):
                if(input[i+1][p-1] == "S"):
                        print(f"--find MAS")
                        countDiago += 1
            elif(input[i-1][p+1] == "S"):
                if(input[i+1][p-1] == "M"):
                        print(f"--find SAM")
                        countDiago += 1

        if(countDiago == 2): 
            countXmas += 1

    return countXmas

for i, line in enumerate(input):
    print(f"ligne {i}")
    posFind = findCarac("A", line)

    if(len(posFind) > 0):
        total += searchInDiagonal(input, line, posFind, i)

print(f"total: {total}")    
