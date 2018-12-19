# Import libraries.
import collections
import string
import itertools

class WordGod:
	"""
	This class accesses a file of words, allowing interrogation.
	
	
	"""
		
	def __init__(self):
		
		# Create list of lowercase words as reference.
		word_list = list(word.strip().lower() for word in open("./words.txt", 'r'))
		
		# Create dictionary of signatures.
		words_bysig = collections.defaultdict(list)
		for word in word_list:
			words_bysig[self._signature(word)].append(word)

		# Create dictionary of anagrams.
		self.anagram_dictionary = {self._signature(word):words_bysig[self._signature(word)] for word in word_list}	

	# Define the signature of a word as its sorted letters.
	def _signature(self, word):
		return ''.join(sorted(word))
			
	# Create new sets when wild characters are found.	
	def _with_wilds_expanded(self, charlist, wild_char):			
		for elem in charlist:
			if wild_char in elem:
				for letter in list(string.ascii_lowercase):
					charlist.append(elem.replace(wild_char,letter,1))
				charlist.remove(elem)
		for elem in charlist:
			if wild_char in elem:
				charlist = self._with_wilds_expanded(charlist, wild_char)
				break
		return charlist

	# Generate all combinations of a given length.
	def _test_rack_generator(self, full_rack, length):
		for test_rack in list(itertools.combinations(full_rack, length)):
			yield ''.join(test_rack)

	# Record any anagrams found in letter list.
	def _record_anagrams(self, source_letters, found_word_list):
		sorted_source = ''.join(sorted(source_letters))
		if sorted_source in self.anagram_dictionary:
			for anag in self.anagram_dictionary[sorted_source]:
				found_word_list.append(anag)

	# Obtain list of longest words.
	def longest_words(self, rack, minimum_length, wild_character):	
		"""Determine the longest words which can be retrieved from a given rack of letters.
		Args:
			rack (str): The list of letters from which words are to be constructed. This may include any number of wild characters.
			minimum_length (int): The minimum length of words to be constructed.
			wild_character (str): A non-alphabetic character to be considered a wild character.

		Returns:
			list: A list of words (sorted alphabetically) which have been found in the given rack. If no words have been found, then the list is empty.
		"""
		
		# Start with an empty list.
		found_words = []
		
		# Loop through each subset of letters (expanding wild characters if necessary), looking for anagrams.
		# Once a word has been found, collect all words found for that length and return a set of unique words as a list.
		for test_length in range(len(rack), minimum_length-1, -1):
			for test_rack in self._test_rack_generator(rack, test_length):
				for expanded_test_rack in self._with_wilds_expanded([test_rack], wild_character):
					self._record_anagrams(expanded_test_rack, found_words)
			if len(found_words) > 0:
				break
		if len(found_words) > 0:
			return sorted(set(found_words))
		else:
			return []
			
# Obtain list of longest words in one step.
def longest_words(rack, minimum_length, wild_character):	
	"""Determine the longest words which can be retrieved from a given rack of letters.
	Args:
		rack (str): The list of letters from which words are to be constructed. This may include any number of wild characters.
		minimum_length (int): The minimum length of words to be constructed.
		wild_character (str): A non-alphabetic character to be considered a wild character.

	Returns:
		list: A list of words (sorted alphabetically) which have been found in the given rack. If no words have been found, then the list is empty.
	"""

	# Create word_god instance.
	myWordGod = WordGod()
	return myWordGod.longest_words(rack=rack, minimum_length=minimum_length, wild_character=wild_character)