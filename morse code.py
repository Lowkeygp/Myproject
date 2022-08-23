#welcome message
print("Welcome to Wolmorse")
print("This program encodes and decodes Morse code.")

# This variable holds each letter and it's corresponding value
MORSE_CODE = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--',
        'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '/', '.': '.-.-.-', ',': '.-.-', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'}
MORSE_DECODE = {value: key for key, value in MORSE_CODE.items()}
outputMessage = ""               # Holds the output message

# Function to encode morse code
def encode(message):

    code = ''

    for index, char in enumerate(message):
        try:
            code += MORSE_CODE[char.lower()]
        except KeyError:
            raise ValueError(f'Char "{char}" at {index} cannot be encoded.')

        code += ' '

    return code[:-1]  # Remove trailing space.

# Function to decode morse code
def decode(morse_code):

    message = ''

    for index, sequence in enumerate(morse_code.split()):
        try:
            message += MORSE_DECODE[sequence]
        except KeyError:
            raise ValueError(f'Cannot decode code "{sequence}" at {index}.')

    return message
  
# Depending on the users input this loop will choose whether to run the encode function or decode function
morse = True
while morse:
    #Takes users input and formats it into variable message which is in lowercase
    inputString = input('Enter a message you would like to encode or decode\n')
    message = inputString.lower().strip()
    #Takes users input on the their choice of whether to decode or encode and formats it into variable choice which is in lowercase
    choice = input('(E)ncode or (D)ecode?\n')
    choice = choice.lower().strip()

    if choice == 'e' or choice == 'encode':
        outputMessage = encode(message)
        print(outputMessage)
    elif choice == 'd' or choice == 'decode':
        outputMessage = decode(message)
        print(outputMessage)
    else:
        print('Error!')

    again=str(input("Would you like to encode/decode another message? (y/n) "))
    if again == "n":
      morse = False
    elif again == "y":
      morse = True
print('Thanks for using the program, goodbye!')
