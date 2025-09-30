import sys

def ceasar():

    alphabet = " abcdefghijklmnopqrstuvwxyz"
    get_letter = 0
    decipher = []

    file = open(sys.argv[1], "r")
    shift = file.readline()
    cipher = str(file.readline()).strip().lower()
    
    shift = (int(shift) % 26)

    for letter in cipher:
        get_letter = alphabet.index(letter) + 26 - shift
        decipher.append(alphabet[get_letter % 26])

    print(shift)
    print(cipher)
    print("".join(decipher))

    file.close()

if __name__ == '__main__':
    ceasar()