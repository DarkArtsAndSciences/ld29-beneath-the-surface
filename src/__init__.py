from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config.from_object('src.config')

import src.compo, src.jam

@app.route('/')
def index():
	urls = {
		'compo': url_for('compo_index'),
		'jam': url_for('jam_index'),
		#'post': url_for('post_index'),
		'source': 'http://github.com/DarkArtsAndSciences/ld29-beneath-the-surface',
		'compo_reset': url_for('compo_cheat', code='restart'),
		'ld29': 'http://www.ludumdare.com/compo/ludum-dare-29/'
	}
	return render_template('post_play.html',
		title="You Don't Want That",
		subtitle="Ludum Dare 29: Beneath the Surface",
		description="""
<p class="center-text">I made a game for <a href="{ld29}">Ludum Dare</a> about <!-- cheating at --> making a game for Ludum Dare.</p>

<h2>How to Play</h2>
<p>The <b>right</b> way to play is to click the links.</p>
<!-- Do not play the wrong way. The game may become angry. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<!-- You don't want that. -->
<p class="bg">...but to <b>win</b> the game you'll have to cheat, and to cheat, you'll have to<span class="error">&lt;--ERROR: View page source for more information.--></span></p>
<!-- 'help_cheat.py': type cheat codes directly into your browser's address bar -->

<a href="{compo}"><img class="center-image" src="/static/post/you_dont_want_that.gif" width="400" height="312"></a>

<h2>Hints</h2>
<ul>
<li>The end of the game is clearly labeled THE END.</li>
<li>The end of the story is just the beginning, and the real game is hidden <span class="bg">beneath the surface...</span></li>
<li>For the speed gamers in the audience, you can skim the story as long as you catch the hints about what to do next.</li>
<li>However, you may want to pay close attention to the text <b>on the main menu</b>.</li>
<li>Cheats are all lowercase, despite being displayed in upper.</li>
<li>Don't trust link colors to tell you if a page is new or old.</li>
<li>If you're getting server errors or are completely lost and want to read the introduction again, you can restart the game at the (real) beginning by clearing your browser cookies (it's the one from beneath-the-surface.herokuapp.com). There's also a "restart" cheat, but if you know what to do with that, you probably aren't lost.</li>
</ul>

<p class="center-text"><a class="link" href="{compo}">play COMPO</a><br/>made in 48 hours</p>
<p class="center-text"><a class="link" href="{jam}">play JAM</a><br/>made in 72 hours [<a href="#jam">changelog</a>]</p>
<p class="center-text"><span class="link">play POST</span><br/>coming "soon" [<a href="#post">changelog</a>]</p>
<p class="center-text"><a class="link" href="{source}">play GITHUB</a><br/>source and development history</p>

<a name="jam"><h2>Jam Version Changelog</h2></a>
<ul>
<li>Around hour 50, changed URLs from / to /compo so I could add /jam. (No gameplay changes, just making it possible to host everything on one server.)</li>
<li>Edited and expanded the story. Added walkthroughs for the SURFACE and BENEATH savefiles.</li>
<li>Added photographic proof: <b>the story is true</b>, <span class="smalltext">at least up to "I needed a whiteboard and some other stuff that was on sale"</span>.</li>
<li>Favicons (yes, plural).</li>
<li>A special background image beneath certain parts of the story text.</li>
<li><b>Changed cheats.</b> The last one is NOT the same as in the compo version. The earlier ones should be easier, and are no longer case-sensitive.</li>
<li>Ugly promotional wallpaper, because I complained about not getting any in the story.</li>
</ul>

<a name="post"><h2>Post Competition Changelog</h2></a>
<ul>
<li>Fixed hashtag typo (it's #LD48, not #LD29) in several places, including the <a href="http://www.ludumdare.com/compo/ludum-dare-29/?action=preview&uid=13938">entry page</a> title, which left the game without a name, so of course I reused a sentence I wrote <!-- over and over and over --> during the compo.</li>
<li>New logo (see above), which is just both compo logos and the "new" game name all in one image, so it's arguably a one-line fix...<b>in Photoshop</b>.</li>
<li>While on the entry page, I noticed I still had 4 open screenshot slots, so I added the new logo, the first and last photos from the story, and a screenshot of THE END (the original screenshot is still there, but not the primary).</li>
<li>Another <a href="/static/post/you_dont_want_that_1920x1080.gif">wallpaper</a> with the new logo, because the Jam wallpaper wasn't pixelated enough.</li>
<li>More to come. I intend to finish the story, and try to make the minigame live up to its description.</li>
</ul>
""".format(**urls))
