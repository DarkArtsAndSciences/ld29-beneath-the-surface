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
	return inflectr.inflect(render_template('index.html', hide_exits=True))

@app.route('/play')
def play():
	if not 'level' in session:
		session['level'] = 0
		session['inventory'] = []
	else:
		session['level'] += 1

	custom_rooms = {0: 'first.html', 13: 'unlucky.html'}
	random_rooms = ['play.html', 'paint.html', 'paper.html']
	if session['level'] in custom_rooms:
		room = custom_rooms[session['level']]
	else:
		room = random.choice(random_rooms)

	return inflectr.inflect(render_template(room, **get_words()))

@app.route('/get/<item>')
def get(item):
	session['inventory'].append('a({})'.format(item))
	return inflectr.inflect(render_template('get.html', item=item, inventory=', '.join(session['inventory'])))

@app.route('/quit')
def quit():
	session.pop('level', None)
	return redirect(url_for('index'))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
