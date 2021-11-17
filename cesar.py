def decaler(lettre, n=3):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        if lettre == alphabet[i]:
            if i+n > len(alphabet)-1:
                return alphabet[i+n-len(alphabet)]
            else:
                return alphabet[i+n]
    return lettre

def cesar(L, n=3):
    C = []
    for lettre in L:
        t = decaler(lettre, n)
        C.append(t)
    return ''.join(C)


def dechiffrer(L, n=3):
    return cesar(L, -n)


def place(lettre):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        if lettre == alphabet[i]:
            return i
    return 0


def vigenere(message, cle):
    C = []
    for i in range(len(message)):
        lettre = message[i]
        t = decaler(lettre, place(cle[i % len(cle)]))
        C.append(t)
    return ''.join(C)


def dechiffrevigenere(message, cle):
    C = []
    for i in range(len(message)):
        lettre = message[i]
        t = decaler(lettre, -place(cle[i % len(cle)]))
        C.append(t)
    return ''.join(C)


print(vigenere("BONJOUR TOUT LE MONDE", "BTSSIO"))

assert(cesar("WIKIPEDIA L'ENCYCLOPEDIE LIBRE") == "ZLNLSHGLD O'HQFBFORSHGLH OLEUH")
assert(dechiffrer("ZLNLSHGLD O'HQFBFORSHGLH OLEUH") == "WIKIPEDIA L'ENCYCLOPEDIE LIBRE")

message = "WIKIPEDIA L'ENCYCLOPEDIE LIBRE"
print(cesar(message,5))

