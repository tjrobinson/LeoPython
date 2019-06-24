Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
StringToEncrypt = input("Please enter a message to encrypt: ")
StringToEncrypt = StringToEncrypt.upper()
ShiftAmount = int(input("Please enter a number from 1 to 25 to be your key. "))
if 25 < ShiftAmount:
    print("Uh Oh, number was too big")
    StringToEncrypt = input("Please enter the message to encrypt: ")
    StringToEncrypt = StringToEncrypt.upper()
    ShiftAmount = int(input("Please enter a number from 1 to 25 to be your key. "))
encryptedString = ""
for currentCharacter in StringToEncrypt:
    position = Alphabet.find(currentCharacter)
    newPosition = position + ShiftAmount
    if currentCharacter in Alphabet:
        encryptedString = encryptedString +  Alphabet[newPosition]
    else:
        encryptedString = encryptedString + currentCharacter
print("Your message is", encryptedString)
