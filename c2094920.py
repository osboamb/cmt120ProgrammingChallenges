# Exercise 1
import math


def reduceFraction(num, den):
    """
    This function takes a numerator and a denominator, reducing the fraction to its lowest terms and outputing them
    as integers.
    
    Args: 
        num (int): the numerator 
        den (int): the denominator
    
    Returns:
        Tuple: the fraction reduced to its lowest term
    
    Examples:
        >reduceFraction(12, 15)
        (4,5)
    """
    common_factor = math.gcd(num, den)
    num_simplified = num / common_factor
    den_simplified = den / common_factor
    return (int(num_simplified), int(den_simplified))


# Exercise 2
def isMagicDate(day, month, year):
    """
    This function outputs whether the date is magic, for example a date is magic if the day * month equals the last
    two digits of the year.
    
    Args: 
        day (int): day
        month (int): month 
        year (int): year 
        
    Returns:
        Bool: if the input is a magic date
        
    Examples: 
        >isMagicDate(10, 6, 1960)
        True  
    """
    if int(str(year)[-2:]) == day * month:
        return True
    else:
        return False


# Exercise 3
def sublist(l):
    """
    This function outputs every possible sublist of a given list
    
    Args: 
        l (list): The list you would like to work out sublists for 
        
    Returns:
        List: it will return all possible sublists as your new_list
    
    Examples: 
        >>> sublist(['a', 'b', 'c',])
        [[], ['a'], ['a', 'b'], ['a', 'b', 'c'], ['b'], ['b', 'c'], ['c']]    
    """
    new_list = [[]]
    for i in range(len(l)):
        for j in range(i + 1, len(l) + 1):
            new_list.append(l[i:j])
    return new_list


# Exercise 4



def pigLatin(word):
    """
    This function allows user to input a string and returns the string translated into PigLatin.
    
    Args: 
        word (str): The string you would like to translate 
    
    Returns:
        Str: word, translated into PigLatin 
    
    Examples:
        >pigLatin('Stefan!')
        'Efanstay!'
    """
    vowel = ['a', 'e', 'i', 'o', 'u']
    newword = word
    punc = ''
    punctuation = '''!()-[]{};:'"\\, <>./?@#$%^&*_~'''
    if word[-1] in punctuation:
        punc = word[-1]
        newword = word[:-1]
    i = 0
    while word[i].lower() not in vowel:
        newword = newword[1:] + newword[0].lower()
        i += 1

        if i == len(word):
            break

    if word[0].isupper():
        newword = newword[0].upper() + newword[1:]

    if word[0].lower() in vowel:
        newword += 'way' + punc
    else:
        newword += 'ay' + punc

    return newword


# Exercise 5
def morseCode(message):
    """
    :param message:
    :return:

    This function uses a dictionary to take a string of letter and numbers, returning them as Morse Code. 
    
    Args: 
        message (str): The message that you would like translated to Morse Code 
        
    Returns:
        None: message, translated into Morse Code 
    
    Examples: 
         >morseCode('Hello, World!')
        .... . .-.. .-.. --- .-- --- .-. .-.. -..
    """

    morse_coder = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
        'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    punctuation = '''!()-[]{};:'"\\, <>./?@#$%^&*_~'''
    message = message.translate(str.maketrans('', '', punctuation))
    message = ''.join(message.split())
    morse = []

    for letter in message:
        letter = letter.lower()
        morse_letter = morse_coder[letter]
        morse.append(morse_letter)
    morse_message = " ".join(morse)

    return morse_message


# Exercise 6

num_to_letters = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                  '8': 'eight', '9': 'nine',
                  '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
                  '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty',
                  '30': 'thirty',
                  '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety',
                  '100': 'hundred'
                  }


def int2Text(num):
    """
    This function takes an integer between 0 and 999, returning it in its word form.
    
    Args: 
        num (int): The integer you would like to translate into its word form 
    
    Returns:
        Str: The word form of the integer as a string
    
    Examples:
        >int2Text(10)
        'ten'
    """
    transcribe = []

    assert num >= 0, "num must be positive"
    assert num <= 999, "num must be between 0 and 999"

    if num in range(20):
        transcribe.append(num_to_letters[str(num)])

    elif len(str(num)) == 2:
        transcribe.append(num_to_letters[str(int(str(num)[0]) * 10)])
        if int(str(num)[1]) != 0:
            transcribe.append(num_to_letters[str(int(str(num)[1]))])

    elif len(str(num)) == 3:
        transcribe.append(num_to_letters[str(num)[0]])
        transcribe.append(num_to_letters['100'])

        if int(str(num)[1]) == 0 and int(str(num)[2]) != 0:
            transcribe.append(num_to_letters[str(num)[2]])
        elif int(str(num)[1]) == 1:
            transcribe.append(num_to_letters[str(num)[1:]])
        else:
            if int(str(num)[1]) != 0:
                transcribe.append(num_to_letters[str(int(str(num)[1]) * 10)])
            if int(str(num)[2]) != 0:
                transcribe.append(num_to_letters[(str(num)[2])])

    num_as_word = (' '.join(transcribe))

    return num_as_word


# Exercise 7
def missingComment(filename):
    """
    This function reads a given file and returns any functions that do not have comments immediately before them.
    
    Args: 
        filename (str): The file that contains the functions 
        
    Returns:
        list: The name of any function within the file that does not have a comment immediately before it 
    
    Examples:
        >missingComment('test_3')
        ['adding']
        
    """
    file = open(filename)
    lines = [line for line in file]
    function_index = []

    for i, line in enumerate(lines):
        if line[:3] == 'def':
            function_index.append(i)

    functions = []
    for i in function_index:
        if i == 0:
            functions.append(lines[i].split('(')[0][4:])
        elif lines[i - 1][0] != '#':
            functions.append(lines[i].split('(')[0][4:])

    return functions


# Exercise 8
def consistentLineLength(filename, length):
    """
    This function takes two parameters, filename and length. It reads the file and justifys the text to the given
    length.
    
    Args:
        filename (str): The file that contains the text to be justified 
        length (int): The maximum length, must be a positive integer.
    
    Returns:
        list: The text within the file justified to the length 
    
    Examples:
        >consistentLineLength('test_4', 70)
        ['Alice was beginning to get very tired of sitting by her sister on the',
         'bank, and of having nothing to do: once or twice she had peeped into',
         'the book her sister was reading, but it had no pictures or',
         'conversations in it,"and what is the use of a book," thought Alice,',
         '"without pictures or conversations?"']    
    """
    file = open(filename)
    output = []

    characters = []
    for line in file:
        characters += line.strip('\n') + ' '
    characters = characters[:-1]

    while len(characters) >= length:
        i = length
        while characters[i] != ' ':
            i -= 1

        justify = characters[:i]
        output.append("".join(str(letter) for letter in justify))
        characters = characters[i + 1:]

    justify = characters
    output.append("".join(str(letter) for letter in justify))

    return output


# Exercise 9
def knight(start, end, moves):
    """
    This function returns true if it is possible to go from the start to the end in the given moves and returns false
    if it is not.
    
    Args: 
        start (str): The starting position of the knight
        end (str): The ending position of the knight
        moves (int): The number of moves the knight can take to travel between the start and the end 
    
    Returns:
        bool: True or False, depending on whether it is possible to travel in the given moves or not 
    
    Examples: 
        >knight('b4', 'b6', 1)
        False
    """

    num_to_letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    start_num = (int(start[1]), num_to_letters[start[0]])
    end_num = (int(end[1]), num_to_letters[end[0]])

    def all_knight_poss(position):
        x, y = position
        poss1 = x + 1, y + 2
        poss2 = x + 1, y - 2
        poss3 = x - 1, y + 2
        poss4 = x - 1, y - 2
        poss5 = x + 2, y + 1
        poss6 = x + 2, y - 1
        poss7 = x - 2, y + 1
        poss8 = x - 2, y - 1

        return [poss1, poss2, poss3, poss4, poss5, poss6, poss7, poss8]

    master_list = []
    truth_poss = [[] for i in range(moves + 1)]
    truth_poss[0].append(start_num)

    for move in range(moves):
        for poss in truth_poss[move]:
            all_poss = all_knight_poss(poss)
            truth_index = [item[0] in range(1, 8) and item[1] in range(1, 8) for item in all_poss]
            for i, item in enumerate(all_poss):
                if truth_index[i] is True:
                    truth_poss[move + 1].append(item)
                    master_list.append(item)

    return end_num in master_list


# Exercise 10
def warOfSpecies(environment):
    return None
