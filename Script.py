import csv
import re

print("Welcome to SMS abbreviation Translator")
print("Remember not to use any void character in continuation")

print('===================================================')

def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        # File path which consists of Abbreviations.
        fileName = "C:\\Users\\risha\\Desktop\\slang.txt"
        # File Access mode [Read Mode]
        accessMode = "r"
        with open(fileName, accessMode) as myCSVfile:
            # Reading file as CSV with delimiter as "=", so that abbreviation are stored in row[0] and phrases in row[1]
            dataFromFile = csv.reader(myCSVfile, delimiter="=")
            # Removing Special Characters.
            _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
            for row in dataFromFile:
                # Check if selected word matches short forms[LHS] in text file.
                if _str.upper() == row[0]:
                    # If match found replace it with its appropriate phrase in text file.
                    user_string[j] = row[1]
            myCSVfile.close()
        j = j + 1
    # Replacing commas with spaces for final output.
    print(' '.join(user_string))
    print('===================================================')
    print('')

while True:
    print("Provide Input below or print exit or EXIT to end script")
    # Getting User String.
    # Sample : user input = "Hi Rishabh meet me asap!"
    user = input()
    # Keep Calling procedure until EXIT or exit keyword is encountered.
    if user.upper() == 'EXIT':
        print("Exiting Script")
        break
    translator(user)
