# Python String Ops - Lab Work

'''
1. Function Annotation: FxNm( input: str ) -> dict
Write a Python program to count the number of characters (character frequency) in a string.
Sample String: ‘google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

s = 'google.com'

def char_freq(s):
    d = {}
    [d.update({i: s.count(i)}) for i in s]
    print(d)

'''
2. Function Annotation: FxNm( input: str ) -> str
Write a Python program to return a string from a given string where all occurrences of its first char have
been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''
sample = 'restart'
def first_char_dollar(sample):
    first = sample[0]
    sample = sample[1:].replace(first, '$')
    print(first+sample)

'''3. Write a Python function that takes a list of words and returns the length of the longest word. '''
word_list = ['first', 'second', 'third', 'fourth']
def longest_word(word_list):
    tie_breaker = []
    longest =  max([len(w) for w in word_list])
    [tie_breaker.append(w) for w in word_list if len(w) == longest]
    print(f'longest word(s) are {tie_breaker}')

'''4. Write a Python program to remove the characters appearing at odd index values of a given string and return the resulting string.'''
odd_word = 'restart'
def remove_odd(odd_word):
    print(odd_word[::2])

'''5. Write a Python function to reverses a string if it's length is a multiple of 4 and returns resulting string.'''
var5 = 'rest'
def rev_string(var5):
    if len(var5) % 4 == 0:
        print(var5[::-1])
    else:
        print(var5)
'''6. Write a Python function to convert a given string to all uppercase 
if it contains at least 2 uppercase characters in the first 4 characters. Return the result.'''
var6 = 'reSTart'
def upper_test(var6):
    upper_count = 0
    for i in var6[:4]:
        if i == i.upper():
            upper_count += 1
    if upper_count >= 2:
        print(var6.upper())
    else:
        print(var6)

'''
7. Write a Python program to create a Caesar encryption.
Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, 
Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter 
some fixed number of positions down the alphabet. For example, with a shift of 2, D would be 
replaced by F, E would become G, and so on. The method is named after Julius Caesar, 
who used it in his private correspondence.
'''
var7, shift = 'xyz', 2
cipher = []
alphabets = 'abcdefghijklmnopqrstuvwxyz'
def ceasar_cipher(var7, shift):
    trans = lambda x, n: var7.maketrans(x, x[n:] + x[:n])
    print(var7.translate(trans(alphabets, shift)))

'''
8. Write a Python program to remove existing indentation from a given string. 
You may assume that only a space (' ') and tab (\t) characters are used for indentation. 
Return the resulting string. Hint: review the capabilities of the textwrap builtin module.
'''
var8 = '    abc'
def remove_indent(var8):
    print(var8.strip())

'''9. Write a Python program to strip the set of provided characters from a string. Return the resulting string.'''
var9,chg = 'abc', 'ac'
def replace_char(var9, chg):
    print(var9.translate({ord(i): None for i in chg}))

'''
10. Write a Python program to count repeated characters in a string. 
Return a dictionary where the keys are the repeated characters and the values are the count.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output: {o: 4, e: 3, u: 2, h: 2, r: 2, t: 2}
'''
var10 = 'thequickbrownfoxjumpsoverthelazydog'
def repeated_chars(var10):
    d = {}
    [d.update({i: var10.count(i)}) for i in var10 if var10.count(i) > 1]
    print(sorted(d.items(), key=lambda x:x[1], reverse=True))

'''
11. Write a Python program to check if a string contains all letters of the alphabet.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
'''
import string
var11 = 'thequickbrownfoxjumpsoverthelazydog'
alphabet_list = set(string.ascii_lowercase)
def alphabet_check(var11):
    check = set(var11.lower()) >= alphabet_list
    print(check)

'''
12. Write a Python program to swap comma and dot in a string. 
Return the resulting string. Challenge: try using the translate() and maketrans() methods of string.
'''
var12 = '32.054,23'
def swap(var12):
    swap_char = var12.maketrans('.,', ',.')
    res = var12.translate(swap_char)
    print(res)

'''
13. Write a Python program to remove duplicate characters of a given string. 
Your solution should leave the 1st occurrence and remove all subsequent occurrences. 
Other than the removals, the order of the characters in the string should not be affected. Return the resulting string.
Sample string: "32.054,23"
Expected Output: "32.054,"
'''
var13 = '32.054,23'
unique_set = {}
def remove_subseq_occur(var13):
    [unique_set.update({var13.find(i): i}) for i in var13 if i not in unique_set]
    print(''.join(unique_set.values()))

'''
14. Write a Python program to create a string from two given strings by concatenating the 
characters that are not contained by both strings. The characters from the 1st string should appear 
before the characters from the 2nd string. Return the resulting string.
Sample input: ‘0abcxyz’, ‘abcxyz1’
Expected Output: ‘01’
'''
var14_1, var14_2 = '0abcxyz', 'abcxyz1'
def concat(var14_1,var14_2):
    common = set(var14_1) & set(var14_2)
    res = [l for l in var14_1 + var14_2 if l not in common]
    print(''.join(res))

'''
15. A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Your function must meet the following criteria
Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
Periods or commas should not affect what is matched. “It is closed.” would be included when the keyword is “closed”. You may assume that source document punctuation is limited to periods and commas only.
Return a list of the index values into the original list for all documents containing the keyword.
Sample input: [ "The Learn Python Challenge Casino.", "They bought a car while at the casino", "Casinoville" ], ‘casino’
'''
words_list = [ "The Learn Python Challenge Casino.", "They bought a car while at the casino", "Casinoville" ]
search_string = 'CASINO'
def text_manipulation(words_list, search_string):
    search_result = []
    for sentence in words_list:
        words = sentence.replace('.', '').replace(',', '').split(' ')
        [search_result.append(words_list.index(sentence)) for w in words if w.upper() == search_string]
    print(search_result)

'''
16. This function receives a (word/string) as a parameter. 
The objective of the function is to convert the incoming string to its 
"Pig Latin" equivalent and return the Pig Latin string.
'''
eng_to_pig_latin = {"football": "ootballfay", "Pittsburgh":"Ittsburghpay",
                    "Apple":"Appleway","oink":"oinkway", "ontology":"ontologyway","yellow":"ellowyay","yttrium":"iumyttray"}
eng_word = 'yttrium'
vowels = 'aeiou'
def pig_latin(eng_word):
    sub,str1 = [],''
    first = eng_word[0]
    second =  eng_word[1]
    if first.lower() in vowels:
        piglatin = eng_word +'way'
    elif first.lower() == first and second.lower() in vowels:
        piglatin = eng_word[1:]+first+'ay'
    elif first.lower()+second.lower() not in vowels:
        for l in eng_word:
            if l not in vowels:
                sub.append(l)
            else:
                str1 = eng_word[eng_word.index(l):]
                break
        str2 = ''.join(sub)
        piglatin = str1+str2+'ay'
    else:
        piglatin = eng_word[1:].capitalize()+first.lower()+'ay'
    print(f'Test word is {eng_word} and its equivalent piglatin word is {piglatin}. '
          f'Comparison with mapping dictionary is {eng_to_pig_latin[eng_word] == piglatin}')


def main():
    char_freq(s)
    first_char_dollar(sample)
    longest_word(word_list)
    remove_odd(odd_word)
    rev_string(var5)
    upper_test(var6)
    ceasar_cipher(var7, shift)
    remove_indent(var8)
    replace_char(var9, chg)
    repeated_chars(var10)
    alphabet_check(var11)
    swap(var12)
    remove_subseq_occur(var13)
    concat(var14_1, var14_2)
    text_manipulation(words_list, search_string)
    pig_latin(eng_word)

if __name__ == "__main__":
    main()