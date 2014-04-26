import random

dictionary = {
	'animals': ['cat', 'dog', 'sheep', 'weasel', 'toad', 'pangolin'],
	'colors': ['off-brown', 'shiny silver', 'yellowish', 'mauve', 'blood red', 'sickly green'],
	'adjectives': ['happy', 'silly', 'fluffy', 'pointy', 'scarred', 'twitching'],
}

def get_words():
	return {word[:-1]: random.choice(dictionary[word]) for word in dictionary}
