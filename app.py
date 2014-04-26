import os

from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config.from_object('config')

from words import get_room, get_words

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
	if not 'level' in session:
		session['level'] = 0
		return render_template('first.html')

	session['level'] += 1
	return render_template(get_room(session['level']), **get_words(session['level']))

@app.route('/quit')
def quit():
	session.pop('level', None)
	return redirect(url_for('index'))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
