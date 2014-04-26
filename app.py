import os
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

animals = ['cat', 'dog', 'sheep', 'weasel', 'toad', 'pangolin']
colors = ['off-brown', 'shiny silver', 'yellowish', 'mauve', 'blood red', 'sickly green']
titles = ['a room', 'a {color} room', 'a large room', 'the last room']
descriptions = [
	"This is a terrible excuse for a room description. You can't see a thing.",
	"The walls are covered in fresh {color} paint. You really hope that's paint.",
	"You feel yourself throwing off your surface emotions and sinking deeper into your true self.",
	"Out of the corner of your eye, you glimpse a pile of {animal}s. You turn around to find the room empty except for a single piece of paper with a crude {animal} drawn on it in {color} crayon.",
	"Your vision blurs as you try to examine the room. Questions swirl through your thoughts. Who are you? Why are you here? Was that a {color} {animal}? What are you digging for? Why can't you see clearly?"
]

@app.route('/play')
def play():
	data = {}
	data['color'] = random.choice(colors)
	data['animal'] = random.choice(animals)
	data['title'] = random.choice(titles).format(**data)
	data['description'] = random.choice(descriptions).format(**data)
	return render_template('play.html', **data)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
