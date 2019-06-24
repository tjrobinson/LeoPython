Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
StringToEncrypt = input("Please enter the message to decrypt: ")
StringToEncrypt = StringToEncrypt.upper()
ShiftAmount = int(input("Please enter the key to decrypt. "))
if 25 < ShiftAmount:
    print("Uh Oh, number was too big")
    StringToEncrypt = input("Please enter the message to decrypt: ")
    StringToEncrypt = StringToEncrypt.upper()
    ShiftAmount = int(input("Please enter the key to decrypt. "))
ShiftAmountB = ShiftAmount + ShiftAmount
ShiftAmount = ShiftAmount - ShiftAmountB
encryptedString = ""
for currentCharacter in StringToEncrypt:
    position = Alphabet.find(currentCharacter)
    newPosition = position + ShiftAmount
    if currentCharacter in Alphabet:
        encryptedString = encryptedString +  Alphabet[newPosition]
    else:
        encryptedString = encryptedString + currentCharacter
    encryptedString = encryptedString.lower()
print("The message is", encryptedString)
