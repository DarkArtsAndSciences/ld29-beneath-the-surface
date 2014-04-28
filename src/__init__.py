from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config.from_object('src.config')

import src.compo

@app.route('/')
def index():
	return render_template('play.html',
		title='LD29 - Beneath the Surface',
		links=['<a href="{}">play compo version</a> (finished)'.format(url_for('compo_index')),
			'<a href="{}">play jam version</a> (beta)'.format(url_for('jam_index')),
			'<a href="http://github.com/DarkArtsAndSciences/ld29-beneath-the-surface">source code<a> (GitHub)'],
		description="<center><img src='/static/face_up.gif'></center>")

@app.route('/jam')
def jam_index():
	return render_template('play.html',
		description="<center><img src='/static/face_up.gif'></center><p>It's not uploaded yet. Try again later.</p>")
