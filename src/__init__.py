from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config.from_object('src.config')

import src.compo, src.jam

@app.route('/')
def index():
	return render_template('jam_play.html',
		title='LD29 - Beneath the Surface',
		links=['<a href="{}">play compo version</a> (made in 48 hours)'.format(url_for('compo_index')),
			'<a href="{}">play jam version</a> (made in 72 hours)'.format(url_for('jam_index')),
			'play post-competition version (coming "soon")'.format(url_for('jam_index')),
			'<a href="http://github.com/DarkArtsAndSciences/ld29-beneath-the-surface">source code<a> (GitHub)'],
		description="""
<div style="min-height: 100px">
<p>I made a game for Ludum Dare 29 about cheating at making a game for Ludum Dare 29. I don't think I survived.</p>

<center><img src="/static/post/you_dont_want_that.gif"></center>

<p><b>How to Play:</b></p>
<p>The correct way to play is to click the links.</p>
<p class="bg">To win the game you'll have to cheat, and to cheat, you'll have to&lt;--ERROR: could not parse 'help_cheat.py'<br/>Try your browser's View Source for more information.--></p>
<!-- 'help_cheat.py': type cheat codes directly into your browser's address bar -->
<p><b>Jam Version Updates:</b></p>

<p>More story and photos, and (in reverse chronological order):</p>

<ul>
<li><b>Changed some of the cheats.</b> In particular, the one near the end is NOT the same as in the compo version. Think harder.</li>
<li>Wallpaper. (later update: fixed typo)</li>
<li>A special background image beneath certain parts of the story text.</li>
<li>Favicons.</li>
<li>Added photographic proof: the story is true, at least up to "I needed a whiteboard and some other stuff that was on sale".</li>
</ul>

<p><b>Post Competition Updates:</b></p>
<ul>
<li>Dual version of logo and better <a href="/static/post/you_dont_want_that_1920x1080.gif">wallpaper</a>.</li>
</ul>
</div>
""")
