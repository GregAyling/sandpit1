# Import libraries.
from word_god import longest_words

# Constants
WILD_CHAR = "*"
MIN_LENGTH = 3

if __name__ == "__main__":
	
	# Keep asking for new input, only stopping when quit requested.
	while True:
		rack = input('Enter letters ("' + WILD_CHAR +   '" is wild), or (q)uit: ')
		if rack.lower() == 'q':
			break
		else:
			word_list = longest_words(rack=rack, minimum_length=MIN_LENGTH, wild_character=WILD_CHAR)
			if len(word_list) == 0:
				print("    No words of at least " + str(MIN_LENGTH) + " letters can be made from this rack")
			else:
				for word in word_list:
					print("    " + word)