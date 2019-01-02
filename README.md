# word_godss

This library supplies functionality based on a file containing a list of words.

## Class WordGod

Instances of this class contain a dictionary of anagrams constructed from the given word file.

Parameters:
1. word_filename = Name of file containing a list of words. There is one word per line. Case is not important.

## Class Function WordGod.longest_words

This function finds the longest words which can be constructed from a given set of letters using the instance's anagram dictionary.

Parameters:
1. rack = String of letters (including wilds) from which words are to be constructed.
2. minimum_length = Smallest number of characters to make words from.
3. wild_character = The character to be considered a wild. 

Returns:
1. List of longest words.

## Function longest_words

This function finds the longest words which can be constructed from a given set of letters using the given word file.

Parameters:
1. rack = String of letters (including wilds) from which words are to be constructed.
2. minimum_length = Smallest number of characters to make words from.
3. wild_character = The character to be considered a wild. 
4. word_filename = Name of file containing a list of words. There is one word per line. Case is not important.

Returns:
1. List of longest words.