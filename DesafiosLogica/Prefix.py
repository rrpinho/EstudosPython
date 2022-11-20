'''
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. 
If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.


Constraints:
    1 <= sentence.length <= 100
    1 <= searchWord.length <= 10
    sentence consists of lowercase English letters and spaces.
    searchWord consists of lowercase English letters.
'''

def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    sentenceList = sentence.split()
    for word in sentenceList:
        prefix = True
        i = 0
        while prefix:
            for letter in word:
                if i < len(searchWord):
                    if letter != searchWord[i]:
                        prefix = False
                        break
                    i += 1
                else:
                    print(sentenceList.index(word)+1)
                    prefix = False
                    return
    print(-1)


isPrefixOfWord("i love eating burger", "burg")
isPrefixOfWord("this problem is an easy problem", "pro")
isPrefixOfWord("i am tired", "you")