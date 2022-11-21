'''
Description
An ancient language was recently uncovered which appears to be a close English language
derivative. A group of researchers requires a program to translate English into this ancient text.
The rules to translate any English word to this foreign language are listed below.
Translation rules
1. Separate each word into two parts.
a. The first part is called the “prefix” and extends from the beginning of the word
up to, but not including, the first vowel (The letter “y” will be considered a
vowel).
b. The rest of the word is called the “stem”.
2. The translated text is formed by switching the order of the prefix and the stem, and
adding the letters “ay” to the end.
a. For example, “sandwich” is composed of “s” + “andwich” and translates into
“andwichsay”, which is “andwich” + “s” + “ay”.

Assignment
Your task is to write a simple program in 20min to perform basic English to this foreign
language translation. Your program does not need to expect inputs from the user. Create a
function that makes the translation and call it using your own code.
Sample session
Input: stop
Output: opstay
Input: no
Output: onay
Input: people
Output: eoplepay
Input: bubble
Output: ubblebay
Input: under
Output: underay
Input: admitted
Output: admitteday
Input: away
Output: awayay
'''

def latim(word):
    vowel = ["a", "e", "i", "o", "u", "y"]
    myword = word.split()
    prefix = []
    index = 0
    for letter in word:
        if vowel.count(letter) == 0:
            word[index] = ''
            word[len(word)] = letter
            word.insert(word.remove(letter), len(word))
            
        else:
            break






latim("stop")