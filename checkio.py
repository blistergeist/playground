# checkio.py

def non_unique(data):
    freqDist = {}

    for val in set(data):
        freqDist[val] = 0

    for val in data:
        freqDist[val] += 1

    for val, freq in freqDist.items():
        if freq == 1:
            del(data[data.index(val)])


def roman_numeral(data):
    values = [1000, 900, 500, 400, 100, 
        90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 
        'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    for i in range(len(values)):
        result = data/values[i]
        if result >= 1:
            roman += symbols[i]*int(result)
            data = data%values[i]
        
    return roman


def grille_cipher(grille, cipher):
    password = ''
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if grille[j][k] == 'X':
                    password += cipher[j][k]
        grille = list(zip(*grille[::-1]))
    return password


def safe_pawns(pawns):
    # a pawn is safe if there is another one row up and one column left/right
    safePawns = 0
    for pawn in pawns:
        # calculate required positions for the safety of that space
        col = pawn[0]
        row = int(pawn[1])
        safeSpaces = [chr(ord(col)+1)+str(row-1), chr(ord(col)-1)+str(row-1)]
        # determine if the safe spaces are included in list of pawns
        if safeSpaces[0] in pawns or safeSpaces[1] in pawns:
            # if so, the pawn we are testing is safe
            safePawns += 1
    return safePawns



def main():
    # data = [1,2,3,2,1]
    # print(non_unique(data))
    # data = 3999
    # print(roman_numeral(data))
    # grille = ('X...', '..X.', 'X..X', '....')
    # cipher = ('itdf', 'gdce', 'aton', 'qrdi')
    # print(grille_cipher(grille, cipher))
    pawns = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
    print(safe_pawns(pawns))


if __name__ == '__main__':
    main()
