import re
import string

eng_to_pig_latin_cipher = {"football415": "ootball415gāŷ", "Pittsburgh": "Ittsburghrāŷ",
                           "Y2ellow": "Y2ellowŵāŷ", "yellow": "ellowaāŷ", "yttrium":"iumavvtāŷ"}

eng_word = 'yttrium'
vowels = 'aeiou'
digits = '0123456789'
cipher = []
alphabets = string.ascii_lowercase

# Requirement 2
'''A cipher shifted letter is substitution cipher in which the letter in the plaintext is replaced by a letter some 
fixed number of step positions down the alphabet. For example, with a step of 2, D would be replaced by F, E would become G. 
Numeric digits are not cipher shifted.'''
def ceasar_cipher(word, shift):
    # Based on the shift passed translate the alphabets starting from A to Z to A+shift to Z+shift so we don't get an exception index out of range
    trans = lambda alphabets, shift: word.maketrans(alphabets, alphabets[shift:] + alphabets[:shift])
    return(word.translate(trans(alphabets, shift)))

# Function to Run the rules for Pig Latin derivation.
def pig_latin_cipher(eng_word, step):
    sub,str1 = [],''
    first = eng_word[0]
    second =  eng_word[1]
    text, sub_str, ciphered_text, piglatin = None, None, None, None
    is_capital = False

    if first.lower() == 'y' and second.isdigit():
        # Requirement 5 - 2nd half:
        '''If the first letter of a word is a 'y' followed by a digit, it is to treated as a vowel as are any other occurrences of 'y'.'''
        piglatin = eng_word +'ŵāŷ'

        # Requirement 3:
        '''
        If word ends with a digit, or a series of consecutive digits, the minimum digit in the series becomes the cipher step value. 
        Thus, overriding (replacing) the step input parameter. Note: a series composed of a single digit has a minimum value equal to that digit.
        '''
    elif any(char.isdigit() for char in eng_word) and first.lower() not in vowels:
        num = re.search(r'\d+', eng_word)
        low = min([int(n) for n in num.group()])
        numeric = num.group()
        d_pos = eng_word.find(numeric)
        if first == first.upper():
            is_capital = True
        for l in eng_word[:d_pos]:
            if l in vowels:
                l_pos = eng_word.find(l)
                sub_str = eng_word[l_pos:d_pos]
                text = eng_word[:l_pos]
                break

        if low < step:
            ciphered_text = ceasar_cipher(text, low)
        else:
            ciphered_text = ceasar_cipher(text, step)
        if is_capital:
            piglatin = sub_str.capitalize()+numeric+ciphered_text+ "āŷ"
        else:
            piglatin = sub_str + numeric + ciphered_text + "āŷ"
    elif first.lower() not in vowels and any(char.isdigit() for char in eng_word) == False:
        text = None
        for l in eng_word:
            if l.lower() in vowels:
                l_pos = eng_word.find(l)
                sub_str = eng_word[l_pos:]
                if first == first.upper():
                    is_capital = True
                text = eng_word[:l_pos].lower()
                break
        ciphered_text = ceasar_cipher(text, step)
        # Requirement - 7:
        '''
        If the original word was capitalized, the new LPC version of the word should also be capitalized in the first letter. 
        If the original capital letter was a consonant, and thus moved, it should no longer be capitalized in its new location.
        '''
        if is_capital:
            piglatin = sub_str.capitalize()+ciphered_text+"āŷ"
        else:
            piglatin = sub_str + ciphered_text + "āŷ"

    print(f'Test word is {eng_word} and its equivalent piglatin word is {piglatin}. '
          f'Comparison with mapping dictionary is {eng_to_pig_latin_cipher[eng_word] == piglatin}')

pig_latin_cipher(eng_word, 2)