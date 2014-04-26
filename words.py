import random

dictionary = {
	'animals': ['cat', 'dog', 'sheep', 'weasel', 'toad', 'pangolin'],
	'colors': ['off-brown', 'shiny silver', 'yellowish', 'mauve', 'blood red', 'sickly green'],
	'adjectives': ['happy', 'silly', 'fluffy'],
}

titles = ['a room', 'a {color} room', 'a large room', 'the last room']
descriptions = [
	"This is a terrible excuse for a room description. You can't see a thing.",
	"The walls are covered in fresh {color} paint.",
	"You feel yourself throwing off your surface emotions and sinking deeper into your true self.",
	"Out of the corner of your eye, you glimpse a pile of {adjective} {animal}s. You turn around to find the room empty except for a single piece of paper with a crude {animal} drawn on it in {color} crayon.",
	"Your vision blurs as you try to examine the room. Questions swirl through your thoughts. Who are you? Why are you here? Was that a {color} {animal}? What are you digging for? Why do you feel so {adjective}? Why can't you see clearly?",
	"You see a row of {level} short lines drawn on the wall in {color} crayon. You don't think they were there a minute ago. You don't see any crayons in the room, either."
	]

def get_words(level=0):
	words = {word[:-1]: random.choice(dictionary[word]) for word in dictionary}
	words['level'] = level
	words['title'] = random.choice(titles).format(**words).title()
	words['description'] = random.choice(descriptions).format(**words)
	return words

def get_room(level=0):
	if level == 13:
		return 'unlucky.html'
	return 'play.html'
