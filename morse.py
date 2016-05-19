import string
import winsound
from time import sleep

dot = [1000, 200]
dash = [1000, 600]
letter_pause = 0.6
word_pause = 1.4

MORSE_CODE_LOOKUP = {
    ".-":   "A",
    "-...": "B",
    "-.-.": "C",
    "-..":  "D",
    ".":    "E",
    "..-.": "F",
    "--.":  "G",
    "....": "H",
    "..":   "I",
    ".---": "J",
    "-.-":  "K",
    ".-..": "L",
    "--":   "M",
    "-.":   "N",
    "---":  "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.":  "R",
    "...":  "S",
    "-":    "T",
    "..-":  "U",
    "...-": "V",
    ".--":  "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"
}

# Reverse the dictionary, so we can lookup by character
MORSE_CODE_LOOKUP = {dict_character: dict_morse for dict_morse, dict_character in MORSE_CODE_LOOKUP.items()}

message = input('Enter your message.\n')
message = message.upper()

for character in message:
    if character == ' ':
        print(' ')
        sleep(word_pause)
    elif character not in string.ascii_uppercase and character not in string.digits:
        pass
    else:
        print(character)
        sequence = MORSE_CODE_LOOKUP.get(character)
        print(sequence)
        for beeper in sequence:
            if beeper == '.':
                winsound.Beep(dot[0], dot[1])
            elif beeper == '-':
                winsound.Beep(dash[0], dash[1])
        sleep(letter_pause)
