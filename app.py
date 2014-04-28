import os
import random

import inflect
inflectr = inflect.engine()

from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
	if not 'mode' in session:
		session['mode'] = 'start'

	words = {
		'start': ['up', '', 'someone', 'change', 'win', 'to stop', 'depend'],
		'surface': ['up', '', 'someone', 'change', 'cheat', 'to stop', 'depend'],
		'beneath': ['down', '', 'something', 'end', 'die', '', 'depend'],
		'fail': ['down', '', 'something', 'end', 'cheat', 'many', 'depend'],
		'multi': ['up', ', yet', 'something', 'end', 'die', 'all the', 'end'],
		'final': ['down', ', yet', 'something', 'end', 'win', '', 'end']
	}[session['mode']]

	links = {
		'start': ['<a href="/story">learn more</a>'],
		'surface': ['<a href="/play">play SURFACE</a>'],
		'beneath': ['<a href="/play">play BENEATH</a>'],
		'fail': ['<a href="/fail">play YOU_FAILED</a>'],
		'multi': ['<a href="/play/YOU_FAILED">play YOU_FAILED</a>',
			'<a href="/play/BENEATH">play BENEATH</a>'],
		'final': ['<a href="/play/DONT_FAIL_AGAIN">play DONT_FAIL_AGAIN</a>']*3
	}[session['mode']]

	if 'walkthrough' in session:
		links.insert(0, '<a href="/walkthrough">walkthrough</a>')

	return inflectr.inflect(render_template('play.html',
		title='#LD29, I need your help.',
		links=links,
		hidden=['Is the game changing what I typed again?',
"Don't trust the game text. It lies to get what it wants. I'll leave hints to help you. I don't think it can change the comments.",
'Be careful. I think...I might have made it angry.',
"I don't want that."],
		description="""
<center><img src='/static/face_{}.gif'></center>
<p>This isn't really a game. It's just the only way I have left to communicate.</p>
<p>I can't exactly say I wrote it alone, either. I don't mean there are any other people involved{}. It's just...more like something that happened to me, something {} did <b>to</b> me, than something <b>I</b> did.</p>
<!-- Please don't let this be something I did. -->
<p>I <b>can</b> say it all started less than 48 hours ago. It doesn't take more than a weekend for your entire life to {}.</p>
<p>Anyway, I'm not posting this because I want to {}, or for fame, or even just for fun.</p>
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<!-- I don't want that. -->
<p>I don't want that.</p>
<p>I just want {} other people going through what I've been through.</p>
<p>Please, keep an open mind and keep reading. Your life may {} on this "game".</p>
""".format(*words)))

@app.route('/story')
def story():
	if not 'mode' in session:  # new players start at the beginning
		return redirect(url_for('index'))

	if not 'page' in session:
		session['page'] = 0

	pages = [
		{'title': 'My ideas are stuck beneath the surface', 'description': """
<p>I was having trouble coming up with an idea for #LD29. (Like everyone else, I was ready to make a game about Breaking the Rules.)</p>
<p>So I decided to head out to my local office suppy store to pick up a whiteboard (that's where ideas come from, right?) and then realized I didn't have enough markers. Also they had bracelet USB drives on sale. And a glass standing desk whiteboard in a block of cork for sticking things to with sharp pins! I bet everyone else is making their graphics in Photoshop or something equally commonplace.</p>
<p>[placeholder: photo]</p>
<p>Maybe I'm too vulnerable to temptation.
<p>Anyway, after leaning the larger whiteboard against the wall and drawing a rainbow-scented pile of lack of artistic talent on it, I decided to try out my new USB drive.
<p>Maybe I'm just biased by what happened later, but I could swear I had a feeling that the idea I needed for my game was on that drive somehow. I mean, I know drives sometimes come with free terrible MP3s and stuff like that, and you can find inspiration in anything, but this was something more. Like a cold, solid certainty, like the way I felt when I signed my taxes two weeks ago, something final yet endless. Thanks for the support, we'll be back for more next year. I was that sure, that the idea was in there, that it was something I could use and reuse.</p>
<p>I wish I'd spent more time trying to come up with an idea of my own.</p>
<p>The drive wouldn't go into the USB port at first. I flipped it a few times, still no luck. Finally I blew into it, as if it were an old NES cartridge, and a scrap of paper fell out, probably the "inspected by" sticker. Well, thank you for my protection. Without the paper in the way, the drive clicked neatly into the port and showed up on my computer a few seconds later.</p>
<center><img src='/static/surface.png'></center>
<p>It was empty.</p>
<p>Not even a readme file helpfully explaining how to install USB drivers so you can mount the drive and read the readme.</p>
<p>I hadn't expected working game code or anything like that. But an entertainingly terrible MP3 would have been nice. Even a wallpaper with a giant pixelated version of the corporate logo would have been something. I felt a rush of disappointment, then anger, far stronger than the situation deserved.</p>
<p>The drive name, SURFACE, was the only thing I could see on the screen. Just sitting there on the screen. Staring at me. Mocking me.</p>
<p>[screenshot, blurred except for drive name]</p>
<p>I renamed it DEAD_DRIVE, slammed the laptop lid down, and walked away.</p>
<p class='smalltext'>I could never use a desktop computer. There's no good way to properly express certain emotions to them.</p>
"""},
		{'title': 'Facing the consequences', 'description': """
<p>I spent the rest of the day trying to come up with a game idea without success.</p>
<p>I didn't even sleep well. I kept having nightmares about a face staring at me with empty eyes, flipping itself over and over and always looking like it was still upside down, mouth open in silent mocking laughter.</p>
<p>When I opened my laptop the next morning, all my windows had been closed -- as dramatic as it looks, slamming the lid down shouldn't do anything except put it to sleep -- except for the one showing my new USB drive. It was named BENEATH now, and contained several code and text files.</p>
<center><img src='/static/beneath.png'></center>
<p>Curious, I opened a few files. It looked like some sort of web app, but I couldn't figure out what it did, and large sections of the code were commented out entirely.</p>
<p>It took some Serious Difficult Code Hacking, but eventually I figured out how to start the server,</p>
<p>[screenshot of ">python app.py"]</p>
<p>and use the app.</p>
<p>[screenshot of app in Safari; there's already a saved game named BENEATH]</p>
<p>It's a game? Perfect! Maybe I'll steal it. I mean use it. This code wasn't here yesterday, so it's like it was written during the competition, right? Maybe I wrote it myself while sleepwalking last night, I don't remember and you can't prove me wrong.</p>
<p>And then I noticed that the game's logo was the face from my nightmares.</p>
"""},
		{'title': 'Escaping death', 'description': """
<p>Suddenly, I'm in the middle of a combat scene.</p>
<p>[screenshot]</p>
<p>It took me a minute to realize that I had reflexively hit the CONTINUE GAME button just to get that face off my screen. Good reflexes, self! All that time spent gaming IS worth something!</p>
<p>I start clicking links at random, no idea what I'm doing but somehow I manage to get out of combat and run away. Once I'm out of danger, I start exploring. It looks like an interesting game, but most of the puzzles have been completed already and I have no idea what I'm supposed to be doing now.</p>
<p>It occurs to me that if I submit this as my own work, and people ask me any questions about it, I'm not going to be able to come up with convincing answers.</p>
<p>Well, I won't have to waste any time actually <b>making</b> a game, plenty of time to play. I decide to start over from the beginning, maybe write a walkthrough and take a bunch of screenshots.</p>
<p>Suddenly, I'm in the middle of a combat scene.</p>
<p>Again.</p>
<p>This time I don't escape.</p>
<p>I don't even remember how it started, what link I clicked to start the fight. It's a turn based web game, you have to click a link to make anything happen, but it was just...decision, attack. Almost like the game was reading my mind.</p>
<p>Anyway, it worked. After the thing killed me, it sent me back to the main menu. The saved game was gone and I was free to create a new one. Death must be permanent in this game. I'll have to be careful.</p>
"""},
		{'title': 'My game', 'description': """
<p>Time to play this game from the beginning and find out what it's about.</p>
<p>After playing the other save file, I was expecting something more violent. It's just a simple text adventure, where you move around or interact with things by clicking links. Each page has a paragraph or two about the room or whatever, maybe an ugly black and white drawing of it, and a link. Sometimes two links, but  mostly it seems like the plot is on rails and the game is just giving you the illusion of control.</p>
<p>And the plot... I've been playing for a few hours and I'm still having trouble figuring it out. I'm trapped in a house -- well, it claims I'm not <b>trapped</b>, but it won't let me open the front door -- with maybe half a dozen rooms, standard house stuff. You can click on lights and faucets and things to turn them on and off, but it all feels hollow, like you're not really interacting with the world. Lights on. Look, the page background changed color. Lights off. Black again. On. Off. On. Off. On. Look, I'm making something happen. Am I winning? I have no idea.</p>
<p>What does it want me to do?</p>
<p>I've explored the whole house, except for one room. There are two bedrooms on the second floor, with giant painted wood letters on their doors. The room with a white S looks like my bedroom; the room with a black B is locked.</p>
<p>I'm starting to wish I'd just written something on my own instead of getting tangled up in this "free" code. The game just isn't fun. Off. On. Off. Pick up an item? You don't want that. On. Open the door? You don't want that. Off. On. Off. Jump out the second floor window? You don't want that. Yeah, well, I'm starting to.</p>
<p>And I'm really starting to hate that sentence. "You don't want that." It seems to be the game's standard response whenever I ask it to do something from the parts of the code that are commented out. <span class='smalltext'>I need to figure out how it's doing that. My code always ignores comments completely, but this seems to know that it's there but not enabled, somehow.</span></p>
<p>The game seems really glitchy, too. <span class='smalltext'>Too bad <b>that</b> wasn't the theme.</span> Sometimes the colors get inverted, and even turning the lights on and off doesn't fix it. Sometimes the images are upside down. I think. Half of them are so poorly drawn, I'm not even sure which way is up.</p>
<p>Sometimes I feel really weird when it flips. I mean, I'm not having fun to begin with, but once in a while the screen shifts and I feel like I'm being flipped with it, like gravity got stuck in lag for a moment and hit too hard when it caught up, like the ground dropped out beneath me, like I'm trapped inside myself and can't break through the surface. <!-- I don't want that. --> Usually I'd blame that on too many flashing colors.</p>
<p>...but this game is entirely in black and white. It's not even animated. The face never blinks its eyes. It just stares at me. On. Off. On. Off. Stare.</p>
<p>Wait, no, there's <b>one</b> animation. There's a TV in the living room, and the room image has actual video of whatever channel you're watching. Except the only channel you're allowed to watch is playing a static image of the face. Not blinking. Staring.</p>
<p>I want to quit, stop telling me I don't want that.</p>
<p>How long have I been playing this game?</p>
<p>On.</p>
<p>Off.</p>
<p>On.</p>
<p>Off.</p>
<p>On.</p>
<p>Off.</p>
<p>On.</p>
<p>Off.</p>
<p>On.</p>
<p>Off.</p>
<p>If I could figure out how to die, I'd do it.</p>
<p>&nbsp;</p>
<p class='smalltext'>I don't even care if it's cheating. I'd happily type a /cheat/code right into the address bar if I thought it would get me out of here.</p>
<p>&nbsp;</p>
<p>On.</p>
<p>Off.</p>
<p>On.</p>
<p class='smalltext'>Help.</p>
"""}]

	page = pages[session['page']]
	page['links'] = ['<a href="/story">continue</a>']

	session['page'] += 1
	if session['page'] > 2:
		session['walkthrough'] = True
	if session['page'] > len(page):
		page['links'] = ['<a href="/">back to main menu</a>']
		session.pop('page')
		if session['mode'] == 'start':  # if it's locked...
			session['mode'] = 'surface'  # unlock /play

	return inflectr.inflect(render_template('play.html', **page))

@app.route('/walkthrough')
def walkthrough():
	if not 'mode' in session:  # new players start at the beginning
		return redirect(url_for('index'))

	if not 'walkthrough' in session:  # not unlocked yet
		return redirect(url_for('story'))

	pages = {
		'start': {'title': 'Walkthrough', 'description': """
<p>TODO: play game, write walkthrough</p>
"""},
		'surface': {'title': 'Walkthrough: The Surface', 'description': """
<p>When the game starts, you'll find yourself in a small house.</p>
<p>You can turn the lights on and off.</p>
<p>Disturbingly cheerful NPCs will pretend to be your friends and family.</p>
<p style='smalltext'>TODO: There has to be more to the game than this. What happened to the combat scenes? I can't even find a single way to die.</p>
"""},
		'beneath': {'title': 'Walkthrough: Beneath the Surface', 'description': """
<p>When the game starts, you'll find yourself alone in a small house.</p>
<p>You will not be alone for long. You will be tempted to use this time to find a weapon.</p>
<p>You don't want that.</p>
<p>You should just focus on escape. Get out of the house. Take any option you can.</p>
<p>You are running out of time.</p>
<p>You don't want that.</p>
<p>Hint: this game would also have worked for Death Is Useful.</p>
"""},
		'fail': {'title': 'Walkthrough: Failure', 'description': """
<p>I don't know what's wrong with this game. I'm not even dying anymore, it just cuts straight to my corpse with the evil NPCs standing over it. Staring.</p>
<p>Why can't I stop playing?</p>
<p>I wish there was a way to enable multiple save files. Maybe then it would let me start over. I've tried a few <a href='/cheat/code'>cheat codes</a>, but I couldn't figure out the right one.</p>
<p>I wish I could start over.</p>
<p>&nbsp;</p>
<p>Oh, I found the piece of paper that was stuck in the drive at first, remember? The one I thought was an inspection sticker?</p>
<p>It's a piece of old, thin paper, folded up with a black ink symbol on the inside and a red X on the outside. I don't think I have to tell you what the symbol is. [photo]</p>
"""},
		'multi': {'title': 'Walkthrough: The Second Save', 'description': """
<p>Obviously Bad Hint from the Game Pretending to Be Me: try getting yourself killed!</p>
"""},
		'final': {'title': 'Walkthrough: The Final Save', 'description': """
<p>Okay, I've finally got this game figured out. There's no way to win from inside the game. You have to give it what it wants, <b>outside</b> of the game.</p>
<p>What does it want? It won't tell me. It just says it's not for me know, that it was my place to write the walkthrough that would guide the winner, but not to be the winner myself.</p>
<p class='smalltext'>But if I had to guess, I'd say that, like all of its kind, it just wants to spread the infection.<p>
"""}}

	page = pages[session['mode']]
	page['links'] = ['<a href="/">return to main menu</a>']

	return inflectr.inflect(render_template('play.html', **page))

@app.route('/play')
def play():
	if 'mode' in session:
		if session['mode'] == 'surface':
			return inflectr.inflect(render_template('play.html', title='The Surface', links=['<a href="/">return to main menu</a>'], description="""
<p>You are in a small, cheery house.The walls are off-white with white trim. The front door is locked. Your TV and computer are in the living room. Softly carpeted stairs lead up to your bedroom.</p>
<p>The local NPCs are smiling and friendly.</p>
<p>You may turn the lights on and off.</p>
"""))

		if session['mode'] == 'beneath':
			return inflectr.inflect(render_template('play.html', title='Beneath the Surface', links=['<a href="/play">look around</a>', '<a href="/die">die</a>'], description="""
<p>You are in a small, dark house. Brownish paint peels off in long strips from the decaying walls. The front door lock is rusted shut. The living room has been looted of all valuables that weren't nailed down, all valuables that were nailed down, and the nails themselves. Metal prices must be up again.</p>
<p>The stairway leading down to your bedroom looks wobbly but usable, as long as you're up to date on your tetanus shots.</p>
<p>You may turn the lights on and off, but the bulbs were stolen years ago.</p>
"""))

	return redirect(url_for('index'))

@app.route('/die')
def death():
	if not 'deaths' in session:
		return redirect(url_for('index'))

	session['deaths'] += 1

	if session['mode'] == 'beneath':
		if session['deaths'] < 3:
			return redirect(url_for('dead'))
		else:
			return redirect(url_for('fail'))

	if session['mode'] == 'multi':
		session['mode'] = 'final'
		return redirect(url_for('final'))

	return redirect(url_for('index'))

@app.route('/dead')
def dead():
	return inflectr.inflect(render_template('play.html',
		title='You have died',
		links=['<a href="/">back to main menu</a>'],
		description="""
<p>[image of your dead avatar. a local NPC smiles sadly]</p>
"""))

@app.route('/fail')
def fail():
	session['mode'] = 'fail'
	return inflectr.inflect(render_template('play.html',
		title='You have failed',
		links=['<a href="/">I am a failure.</a>'],
		description="""
<p>[an unskippable cutscene of NPCs laughing at your corpse]</p>
		"""))

@app.route('/cheat/<code>')
def cheat(code):
	if code in ['clear', 'restart', 'start-over']:
		session.clear()
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>You feel completely free.</p>
""".format(code.upper())}

	elif code in ['multi', 'multiple', 'many', 'files', 'enable-multiple-files']:
		session['mode'] = 'multi'
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>Your vision doubles for a moment.</p>
<p>You feel a sudden rush of paranoia. What if someone saw you cheat? You don't want that.</p>
<p>You hope the game isn't angry with you.</p>
""".format(code.upper())}

	elif code in ['quit', 'die'] and session['mode'] == 'surface':
		session['mode'] = 'beneath'
		session['deaths'] = 0
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>You feel strangely empty.</p>
<p>You feel a sudden rush of paranoia. What if someone saw you cheat? You don't want that.</p>
<p>You hope this doesn't cause any weird glitches in the game.</p>
""".format(code.upper())}

	else:
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>Nothing happens.</p>
<p>A wave of relief washes over you. Cheating is wrong. You don't want that.</p>
""".format(code.upper())}

	if not 'links' in page:
		page['links'] = ['<a href="/">back to main menu</a>']

	page['title'] = 'cheat {}'.format(code.upper())

	return inflectr.inflect(render_template('play.html', **page))

@app.route('/play/<filename>')
@app.route('/play/<filename>/<room>')
def play_filename(filename, room=None):
	if filename == 'YOU_FAILED':
		return inflectr.inflect(render_template('play.html', title='You have failed again', links=['<a href="/">I am a repeated failure. I shall return to the main menu in shame.</a>'], description="""
<center><img src='/static/face_down.gif'></center>
<p>[image: the NPCs continue silently staring at your corpse]</p>
"""))

	if filename == 'BENEATH':
		if not room:
			return inflectr.inflect(render_template('play.html', title='Far Beneath the Surface', description="""
<p>You are in a small, dark house. Brownish paint peels off in long strips from the decaying walls. The front door lock is rusted shut. The living room has been looted of all valuables that weren't nailed down, all valuables that were nailed down, the <a href='/play/BENEATH/nails'>nails</a> themselves, and most of the floor.</p>
<p>The <a href='/play/BENEATH/stairway'>stairway</a> leading down to your bedroom looks wobbly but usable, as long as you're up to date on your tetanus shots.</p>
<p>You may turn the lights on and off, but the bulbs were stolen decades ago.</p>
"""))

		rooms = {
			'nails': {'title': 'A Rusty Nail', 'links': ['<a href="/play/BENEATH">continue</a>'], 'description': """
<p>You find a single rusty nail that all the previous scavengers somehow missed.</p>
<p>It is sharp and rusty and might kill you instantly.</p>
<p>You don't want that.</p>
"""},
			'stairway': {'title': 'A Wobbly Stairway', 'links': ['<a href="/play/BENEATH">Yeah, right. Let me into my room already.</a>', '<a href="/die">It\'s what I deserve.</a>'], 'description': """
<p>You fall down the stairs and die.</p>
"""}}
		page = rooms[room]
		return inflectr.inflect(render_template('play.html', **page))

	if filename == 'DONT_FAIL_AGAIN':
		return inflectr.inflect(render_template('play.html', title='Failure is Not an Option', links=['<a href="/">vote</a>', '<a href="/">return to main menu</a>', '<a href="/cheat/clear">start over</a>'], description="""
<p>Vote for this game or it will eat your soul.</p>
<p class='bigtext'>THE END</p>
"""))

	return inflectr.inflect(render_template('play.html', title='Bad Filename', links=['<a href="/">back to main menu</a>'], description="""
<p>There is no save file named {filename}.</p>
<p>&nbsp;</p>
<p>Are you trying to cheat?</p>
<p>I hope you're not trying to cheat. That might make the game angry.</p>
<p>You don't want that.</p>
<p style='smalltext'>also, the correct URL is /cheat/&lt;code&gt;</p>
"""))

@app.route('/final')
def final():
	return inflectr.inflect(render_template('play.html',
		title='The Warning',
		links=['<a href="/">back to main menu</a>'],
		description="""
<p>[the game overtly threatens you unless it gets what it wants, but doesn't tell you what it wants]</p>
"""))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
