# import required package
from spellchecker import SpellChecker
spell = SpellChecker()

word = 'somethng is hapenning here'     # input string to check
splited_name = word.split(" ")          # split the words in string
print("\nSplitted words ", splited_name)
misspelled = spell.unknown(splited_name)
print("\nMisspelled words: ", misspelled)


# replace misspelled words with correct spelling
for word in misspelled:     # words in misspelled

    # Get a list of `likely` options
    print("\nWords similar to misspelled word: ", spell.candidates(word))

    # Get the one `most likely` answer
    print("Word which is more similar to misspelled word ==>", spell.correction(word))
