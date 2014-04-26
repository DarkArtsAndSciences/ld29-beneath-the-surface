import os
import random

import inflect
inflectr = inflect.engine()

from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config.from_object('config')

from words import get_words

@app.route('/')
def index():
	variables = {
		'title': 'Beneath the Surface',
		'description': '<p>We are two souls in one body.</p><p>The one on the surface...</p><p>&nbsp</p><p>&nbsp</p><p>&nbsp</p><p>&nbsp</p><p>...and the one beneath.</p>',
		'ui': {'links': [{'url':'/start', 'text':'play'}]}
	}
	if 'level' in session:
		variables['ui'] = {'links': [{'url':'/play', 'text':'continue'}, {'url':'/quit', 'text':'start over'}]}
	else:
		variables['ui'] = {'links': [{'url':'/start', 'text':'play'}]}
	return inflectr.inflect(render_template('play.html', **variables))

@app.route('/start')
def start():
	session['level'] = 0
	session['choices'] = []
	session['inventory'] = []

	variables = {
		'title': 'Above the Surface',
		'description': """
<p>You awaken in an undescribed room. You remember nothing, not even your own name.</p>
<p>Also, there is a <a href="{crate}">crate</a> here.</p>
<p>This is either <a href="{games}">the beginning of a video game</a>, or <a href="{alcohol}">you're hungover again</a>.</p>
""".format(crate=url_for('get', item='a crate'),
	games=url_for('choose', choice='games'),
	alcohol=url_for('choose', choice='alcohol')),
	}
	return inflectr.inflect(render_template('play.html', **variables))

@app.route('/play')
def play():
	if not 'level' in session:
		return redirect(url_for('start'))

	session['level'] += 1

	words = {'adjective':'fluffy', 'color': 'white', 'animal': 'sheep'}

	rooms = {  #'title': 'description',
		'Was that a({animal})?'.format(**words): """
<p>You thought you saw a({adjective}) {animal} sitting in the corner, but when you turn to look, the room is empty except for a single piece of paper.</p>
<p>Half of the page is filled with a stick-{animal} crudely drawn in {color} crayon. Beneath this childish graffiti is a full page of handwritten text, which on closer inspection turns out to be the word "{adjective}" repeated over and over in a delicately looping cursive script.</p>
""".format(**words),

		'The smell of...paint?': """
<p>The walls are covered in fresh {color} paint.</p>
<p>The room smells...wrong.</p>
<p>Not like fresh paint. Not like anything fresh.</p>
<p>You try not to think about what the paint might be covering.</p>
""".format(**words),

		'The Unlucky Room': """
<p>You are in the unlucky room.</p>
<p>You feel like you should leave as soon as possible.</p>
<p>Maybe you're just paranoid. When was the last time you took your little {color} pills?</p>
""".format(**words),

		'The Unfinished Room': """
<p>This is a terrible excuse for a room description. It's almost as if someone ran out time and didn't finish writing these.</p>
<p>You can't see a thing.{drink}</p>
""".format(drink=('choices' in session and 'alcohol' in session['choices'])*' You need a drink.'),

		'Freedom': """
<p>You feel yourself throwing off your surface emotions and sinking deeper into your true self.</p>
""".format(**words),  # Your true self wants some {choice}.

		'Questions without answers': """
<p>Your vision blurs as you try to examine the room.</p>
<p>Questions swirl through your thoughts. Who are you? Why are you here? Was that a({color}) {animal}? What are you digging for? Why do you feel so {adjective}?</p>
<p>Why can't you see clearly?</p>
""".format(**words),

		'How long have I been here?': """
<p>You see a row of {level} short lines drawn on the wall in {color} crayon. You don't think they were there a minute ago. You don't see any crayons in the room, either.</p>
""".format(level=session['level'], **words)
	}

	#custom_rooms = {0: 'first.html', 13: 'unlucky.html'}
	#random_rooms = ['play.html', 'paint.html', 'paper.html']
	#if session['level'] in custom_rooms:
	#	room = custom_rooms[session['level']]
	#else:
	#	room = random.choice(random_rooms)
	room = random.choice(rooms.keys())

	variables = {
		'title': room,
		'description': rooms[room],
		'ui': {'links': [
			{'url':'/play', 'text':'Dig deeper'},
			{'url':'/quit', 'text':'Give up and return to the surface'}
		]}
	}

	#if something is wrong:
	#	variables['debug'] = "debug"

	return inflectr.inflect(render_template('play.html', **variables))

@app.route('/choose/<choice>')
def choose(choice):
	session['choices'].append(choice)

	variables = {
		'title': 'You have chosen {}'.format(choice),
		'description': 'You know that was the wrong choice, right? You should start over.',
		'ui': {'links': [
			{'url':'/play', 'text':'Dig deeper'},
			{'url':'/quit', 'text':'Give up and return to the surface'}
		]}
	}
	return inflectr.inflect(render_template('play.html', **variables))

@app.route('/get/<item>')
def get(item):
	session['inventory'].append(item)

	variables = {
		'title': 'You get {}'.format(item),
		'description': 'You pick up {}. It does not bite you.'.format(item),
		'ui': {'links': [
			{'url':'/play', 'text':'Dig deeper'.format(item)},
			{'url':'/quit', 'text':'Give up and return to the surface'}
		]}
	}
	return inflectr.inflect(render_template('play.html', **variables))

@app.route('/quit')
def quit():
	title = 'Are you sure you want to quit?'
	description = "You'll lose everything..."
	ui = {
		'links': [
			{'url':'/play', 'text':'No, take me back to the game'},
			{'url':'/confirm_quit', 'text':'Yes, let me out of here!'}
		]
	}
	return inflectr.inflect(render_template('play.html', title=title, description=description, ui=ui))

@app.route('/confirm_quit')
def confirm_quit():
	session.pop('level', None)
	session.pop('choices', None)
	session.pop('inventory', None)
	#TODO: keep achievements, but remove other game data
	return redirect(url_for('index'))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
