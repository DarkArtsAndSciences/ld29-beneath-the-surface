from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config.from_object('src.config')

import src.compo, src.jam

@app.route('/')
def index():
	return render_template('jam_play.html',
		title='LD29 - Beneath the Surface',
		links=['<a href="{}">play compo version</a> (finished)'.format(url_for('compo_index')),
			'<a href="{}">play jam version</a> (in progress, better graphics)'.format(url_for('jam_index')),
			'<a href="http://github.com/DarkArtsAndSciences/ld29-beneath-the-surface">source code<a> (GitHub)'],
		description="""
<div class="bg" style="min-height: 100px">
<p>I made a game for Ludum Dare 29 about cheating at making a game for Ludum Dare 29. I don't think I survived.</p>

<p>Controls: Mostly just clicking links; if you can read this, you can play the game. However, to win the game you'll have to cheat, and to cheat, you'll have to&lt;--ERROR: could not parse 'help_cheat.py'<br/>Try your browser's View Source for more information.--></p>
<!-- 'help_cheat.py': type cheat codes directly into your browser's address bar -->
</div>
""")
