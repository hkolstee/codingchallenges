# Each person in Italy has an unique identifying ID code issued by the national tax office after the birth registration: the Fiscal Code (Codice Fiscale). Check the Resources tab for more info on this.

# Given a dictionary containing the personal data of a person (name, surname, gender and date of birth) return the 11 code characters as a string following these steps:

# Generate 3 capital letters from the surname, if it has:

# At least 3 consonants then the first three consonants are used. (Newman -> NWM).
# Less than 3 consonants then vowels will replace missing characters in the same order they appear (Fox -> FXO | Hope -> HPO).
# Less than three letters then "X" will take the third slot after the consonant and the vowel (Yu -> YUX).
# Generate 3 capital letters from the name, if it has:

# Exactly 3 consonants then consonants are used in the order they appear (Matt -> MTT).
# More than 3 consonants then first, third and fourth consonant are used (Samantha -> SNT | Thomas -> TMS).
# Less than 3 consonants then vowels will replace missing characters in the same order they appear (Bob -> BBO | Paula -> PLA).
# Less than three letters then "X" will take the the third slot after the consonant and the vowel (Al -> LAX).
# Generate 2 numbers, 1 letter and 2 numbers from date of birth and gender:

# Take the last two digits of the year of birth (1985 -> 85).
# Generate a letter corresponding to the month of birth (January -> A | December -> T) using the table for conversion included in the code.
# For males take the day of birth adding one zero at the start if is less than 10 (any 9th day -> 09 | any 20th day -> 20).
# For females take the day of birth and sum 40 to it (any 9th day -> 49 | any 20th day -> 60).


months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }


def fiscal_code(person):
    fiscalCode = ""
    # devide the string into two seperate strings of consonants and vowels
    devidedSurname = devide_string(person["surname"])
    devidedName = devide_string(person["name"])

    # create fiscal code in 3 steps, first surname, then name, and then the remaining numbers 
    fiscalCode += surname(devidedSurname)
    fiscalCode += name(devidedName)
    fiscalCode += numbers(person)
    
    return (fiscalCode)

# create the remaining numerical code at the end of the fiscal code according to the instructions
def numbers(person):
    numbers = ""
    dateOfBirth = person["dob"].split("/")
    numbers += dateOfBirth[2][-2:]
    numbers += months[dateOfBirth[1]]
    if (person["gender"] == "M"):
        if (len(dateOfBirth[0]) > 1):
            numbers += dateOfBirth[0]
        else: 
            numbers += "0" + dateOfBirth[0]
    else:
        numbers += str(40 + int(dateOfBirth[0]))

    return (numbers)


def surname(devidedSurname):
    # case more than 3 consonants
    if (len(devidedSurname[0]) > 2):
        return (devidedSurname[0][0:3])
    # case less than 3 consonants but surname is not made up of only 2 letters
    elif (len(devidedSurname[0] + devidedSurname[1]) >= 3):
        return ((devidedSurname[0] + devidedSurname[1])[0:3])
    # case surname is made up of only two letters
    else:
        return ((devidedSurname[0] + devidedSurname[1] + "XXX")[0:3])

def name(devidedName):
    # case exactly 3 consonants
    if (len(devidedName[0]) == 3):
        return (devidedName[0][0:3])
    # case more than 3 consonants
    elif (len(devidedName[0]) > 3):
        return (devidedName[0][0] + devidedName[0][2:4])
    # case less than 3 consonants but name is not made up of only 2 letters
    elif (len(devidedName[0] + devidedName[1]) >= 3):
        return ((devidedName[0] + devidedName[1])[0:3])
    # case name is made up of only two letters
    else:
        return ((devidedName[0] + devidedName[1] + "XXX")[0:3])


def devide_string(string):
    vowelCheck = ['A', 'I', 'E', 'O', 'U']

    devidedString = []
    consonants = ""
    vowels = ""

    # make string uppercase
    for i in (string.upper()):
        if i in vowelCheck:
            vowels += i
        else:
            consonants += i

    devidedString.append(consonants)
    devidedString.append(vowels)
    
    return(devidedString)

# fiscal_code({ "name": "Brendan", "surname": "Eich", "gender": "M", "dob": "1/12/1961"})# "CHEBND61T01"
# fiscal_code({ "name": "Helen", "surname": "Yu", "gender": "F", "dob": "1/12/1950"})# "YUXHLN50T41"
# fiscal_code({ "name": "Al", "surname": "Capone", "gender": "M", "dob": "17/1/1899"})# "CPNLAX99A17"
# fiscal_code({ "name": "Mickey", "surname": "Mouse", "gender": "M", "dob": "16/1/1928"})# "MSOMKY28A16"
# fiscal_code({ "name": "Marie", "surname": "Curie", "gender": "F", "dob": "7/11/1867"})# "CRUMRA67S47"