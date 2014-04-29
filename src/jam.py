import os
import random

import inflect
inflectr = inflect.engine()

from flask import Flask, render_template, session, send_from_directory, redirect, url_for
from src import app

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static', 'jam'), 'faceup.ico', mimetype='image/vnd.microsoft.icon')

#app.add_url_rule('/favicon.ico', '/static/jam/faceup.ico')

@app.route('/jam')
def jam_index():
	if not 'mode' in session:
		session['mode'] = 'start'

	words = {
		'start': ['up', '', 'someone', 'change', 'win', 'to stop', 'depend'],
		'surface': ['up', '', 'someone', 'change', '<a href="{}">cheat<a>'.format(url_for('jam_cheat', code='code')), 'to stop', 'depend'],
		'beneath': ['down', '', 'something', 'end', 'die', '', 'depend'],
		'fail': ['down', '', 'something', 'end', 'cheat', 'many', 'depend'],
		'multi': ['up', ', yet', 'something', 'end', 'die', 'all the', 'end'],
		'final': ['down', ', yet', 'something', 'end', 'win', '', 'end']
	}[session['mode']]

	links = {
		'start': ['<a href="{}">learn more</a>'.format(url_for('jam_story'))],
		'surface': ['<a href="{}">play SURFACE</a>'.format(url_for('jam_play'))],
		'beneath': ['<a href="{}">play BENEATH</a>'.format(url_for('jam_play'))],
		'fail': ['<a href="{}">play YOU_FAILED</a>'.format(url_for('jam_fail'))],
		'multi': ['<a href="{}">play YOU_FAILED</a>'.format(url_for('jam_play_file', filename='YOU_FAILED')),
			'<a href="{}">play BENEATH</a>'.format(url_for('jam_play_file', filename='BENEATH'))],
		'final': ['<a href="{}">play DONT_FAIL_AGAIN</a>'.format(url_for('jam_play_file', filename='DONT_FAIL_AGAIN'))]*3
	}[session['mode']]

	if 'walkthrough' in session:
		links.insert(0, '<a href="{}">walkthrough</a>'.format(url_for('jam_walkthrough')))

	return inflectr.inflect(render_template('jam_play.html',
		title='#LD29, I need your help.',
		links=links,
		hidden=['Is the game changing what I typed again?',
"Don't trust the game text. It lies to get what it wants. I'll leave hints to help you. I don't think it can change the comments.",
'Be careful. I think...I might have made it angry.',
"I don't want that."],
		description="""
<center><img src="/static/face_{}.gif"></center>
<p>This isn't really a game. It's just the only way I have left to get the message out.</p>
<p>I can't exactly say I wrote it alone, either. I don't mean there are any other people involved{}. It's just...more like something that happened to me, something {} did <b>to</b> me, than something <b>I</b> did.</p>
<!-- Please don't let this be something I did. -->
<p>I <b>can</b> say it all started less than 48 hours ago. I guess it doesn't take more than a weekend for your entire life to {}.</p>
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

@app.route('/jam/story')
def jam_story():
	if not 'mode' in session:  # new players start at the beginning
		return redirect(url_for('jam_index'))

	if not 'page' in session:
		session['page'] = 0

	pages = [
		{'title': 'My ideas are stuck beneath the surface', 'description': """
<p>I was having trouble coming up with an idea for #LD29. <span class="smalltext">Like everyone else, I was ready to make a game about Breaking the Rules.</span></p>
<p>So I went out to buy a whiteboard. That's where ideas come from, right? At the store, I realized didn't have enough marker colors. Also they had bracelet USB drives on sale. And a glass standing desk whiteboard in a block of cork for sticking things to with sharp pins! I bet everyone else is making their graphics in Photoshop or something equally commonplace.</p>
<center><img src="/static/jam/whiteboard.jpg"></center>
<p>Maybe I'm too vulnerable to temptation.</p>
<p>Anyway, after leaning the larger whiteboard against the wall and drawing a rainbow-scented pile of lack of artistic talent on it (not shown; crop is the one Photoshop tool I've mastered), I decided to plug my new USB bracedrivelet into my laptop.</p>
<p>Maybe I'm biased by what happened later, but... I could swear I already knew, somehow, that the thing I wanted was on that drive. I mean, I've gotten free MP3s and wallpaper and stuff like that on new drives before, and I know you can find inspiration anywhere, but this was like... Like when I signed my taxes a few weeks ago, something final and repetitive at the same time. Thanks for your support, we'll be back for more soon. Nothing's as certain as taxes, right? That's how sure I was, that something was on there, that the thing I wanted was on there.</p>
<!-- Turns out I didn't want that. -->
<p>The drive wouldn't fit in the port at first. I flipped it a few times, still no luck. Finally I blew into it, like an old video game cartridge, and <span class="bg">a scrap of paper fell out. If you look closely, you can see it circled in the photo beneath. The arrow is pointing at the white edge of the paper. <span class="smalltext">Yeah, that's an arrow, drawing with a trackpad is hard, okay? My parents paid way too much for my art degree.</span> </span></p>
<center><img src="/static/jam/usb.jpg"></center>
<p>Looks like the "inspected by" sticker was blocking the contacts.  Well, thank you for my protection.</p>
<p>I tried the now "unprotected" drive. It slid straight in on the first try. A moment later, a window popped open.
<center><img src="/static/jam/surface.jpg"></center>
<p>It was empty.</p>
<p>Not even a readme file helpfully explaining how to install USB drivers so you can mount the drive and read the readme.</p>
<p>I mean, I hadn't expected working game code or anything like that. But an entertainingly terrible MP3 would have been nice. Even a <a href="/static/jam/wallpaper.png">wallpaper with a giant pixelated version of the corporate logo</a> would have been something. <span class="bg">I felt a rush of disappointment, then anger, far stronger than the situation deserved.</span></p>
<p>The drive name, SURFACE, was the only thing I could see on the screen. Just sitting there on the screen. <span class="bg">Staring at me. Mocking me.</span></p>
<center><img src="/static/jam/blurred_surface.jpg"></center>
<p>I renamed it DEAD_DRIVE, slammed the laptop lid down, and walked away.</p>
<p class="smalltext">I could never use a desktop computer. There's just no good way to properly express certain emotions to them.</p>
"""},
		{'title': 'Facing the consequences', 'description': """
<p>I spent the rest of the day trying to come up with a game idea without success.</p>
<p class="bg">I didn't even sleep well. I kept having nightmares about a face staring at me with empty eyes, flipping itself over over and over and always looking like it was still upside down, mouth open in silent mocking laughter.</p>
<p>Anyway, as dramatic as it looks, slamming the lid down should just put a laptop to sleep. But when I opened my laptop the next morning, everything was closed except for the new drive's window. It was named BENEATH now, and contained several code and text files.</p>
<center><img src="/static/jam/beneath.jpg"></center>
<p>Curious, I opened a few files. It looked like some sort of web app, but I couldn't figure out what it did, and large sections of the code were commented out entirely.</p>
<p>It took some Serious Difficult Code Hacking, but eventually I figured out how to start the server,</p>
<center><img src="/static/jam/1337_hacking.png"></center>
<p>and use the app.</p>
<p>[screenshot of app in Safari; there's already a saved game named BENEATH]</p>
<p>It's a <b>game</b>? Perfect! <span class="bg">Maybe I'll steal it.</span> I mean use it. This code wasn't here yesterday, so it's like it was written during the competition, right? Maybe I wrote it myself while sleepwalking last night, I don't remember and no one can prove I didn't.</p>
<p>And then I noticed that the game's logo was the face from my nightmares.</p>
<!-- I don't want this. -->
"""},
		{'title': 'Escaping death', 'description': """
<p>Suddenly, I'm in the middle of a combat scene.</p>
<p>[screenshot]</p>
<p>It took me a minute to realize that I had reflexively hit the "continue BENEATH" link just to get that face off my screen. Good reflexes, self! All that time spent gaming <b>is</b> worth something!</p>
<p>I start clicking links at random, no idea what I'm doing but somehow I get away from... some sort of poorly drawn end boss, not sure what it's supposed to be. All it did was stare, but it was doing massive damage before I got away.</p>
<p>Once I'm out of danger, I slow down, read the text, try to figure out what's going on. Most of the puzzles have been completed already and all the NPCs seem to be dead or missing. <span class="bg">The game is so <b>empty</b> that it's setting my nerves on edge. I can't even find the PDEB, and I have a sneaking sick suspicion that if I did, I'd stand there and let him stare at me just to feel wanted.</span></p>
<p>It occurs to me that if I submit this as my own work, and someone asks me a question about it -- <b>any</b> question, even "what's it about?" -- I'm not going to know the answer.</p>
<p>Well, if I won't have to waste any time actually <b>making</b> a game, I'll have plenty of time to play! I decide to start over from the beginning and <span class="bg">write a walkthrough. I'll put a link to it on the front page</span>, call it part of the game content. Look, I made content, I'm not cheating.</p>
<p>Suddenly, I'm in the middle of a combat scene.</p>
<p>Again.</p>
<p>This time I don't escape.</p>
<p>The death cutscene is the first image I've seen in this game that looks like someone spent time on it. <span class="smalltext">Too much time, if you ask me.</span>
<p>I don't even remember how the fight started, what link I clicked. It's a turn based web game, you have to click a link to make anything happen, but this was just...<span class="bg">decision, attack. Almost like the game was reading my mind.</span></p>
<p>Still, if it <b>was</b> reading my mind, I can't complain when it gives me what I wanted, right? Beneath the image of my dead avatar was text informing me that my death was permanent and my save file had been deleted.</p>
"""},
		{'title': 'My game', 'description': """
<p>Time to play this game right: start on the surface, <b>then</b> see how deep the rabbit hole goes.</p>
<p>After playing the other save file, I was expecting something more violent. It's just a simple text adventure, where you move around or interact with things by clicking links. Each page has a paragraph or two about the room or whatever, maybe an ugly black and white drawing of it, and a link. Sometimes two links, but  mostly it seems like the plot is on rails and the game is just giving you the illusion of control.</p>
<p>And the plot... I've been playing for a few hours and I'm still having trouble figuring it out. I'm trapped in a house -- well, it claims I'm not <b>trapped</b>, but <span class="bg">it won't let me open the front door</span> -- with maybe half a dozen rooms, standard house stuff. You can click on lights and faucets and things to turn them on and off, but it all feels hollow, like you're not really interacting with the world. Lights on. Look, the page background changed color. Lights off. Black again. On. Off. On. Off. On. Look, I'm making something happen. Am I winning? I have no idea.</p>
<p>What does it want me to do?</p>
<p>I've explored the whole house, except for one room. There are two bedrooms on the second floor, with giant painted wood letters on their doors. The room with a white S looks like my bedroom; the room with a black B is locked.</p>
<p>I'm starting to wish I'd just written something on my own instead of getting tangled up in this "free" code. The game just isn't fun. Off. On. Off. Pick up an item? You don't want that. On. Open the door? You don't want that. Off. On. Off. Jump out the second floor window? You don't want that. Yeah, well, I'm starting to.</p>
<p>And I'm really starting to hate that sentence. <span class="bg">"You don't want that."<span> It seems to be the game's standard response whenever I ask it to do something from the parts of the code that are commented out. I need to figure out how it's doing that. My code always ignores comments completely, but this seems to know that it's there but not enabled, somehow.</p>
<p>The game seems really glitchy, too. <span class="smalltext">Too bad <b>that</b> wasn't the theme.</span> Sometimes the colors get inverted, and even turning the lights on and off doesn't fix it. Sometimes the images are upside down. I think. Half of them are so poorly drawn, I'm not even sure which way is up.</p>
<p class="bg">Sometimes I feel really weird when it flips. I mean, I'm not having fun to begin with, but once in a while the screen shifts and I feel like I'm being flipped with it, like gravity got stuck in lag for a moment and hit too hard when it caught up, like the ground dropped out beneath me, like I'm trapped inside myself and can't break through the surface. <!-- I don't want that. --> Usually I'd blame that on too many flashing colors.</p>
<p>...but this game is entirely in black and white. It's not even animated. The face never blinks its eyes. It just stares at me. On. Off. On. Off. Stare.</p>
<p>Wait, no, there's <b>one</b> animation. There's a TV in the living room, and the room image has actual video of whatever channel you're watching. Except the only channel you're allowed to watch is playing a static image of the face. Not blinking. Staring.</p>
<p>On.</p>
<p>I want to quit, stop telling me I don't want that.</p>
<p>Off.</p>
<p>Why isn't there a quit button?</p>
<p>On.</p>
<p>Off.</p>
<p>On.</p>
<p>How long have I been playing this game?</p>
<p>Off.</p>
<p>On.</p>
<p>Off.</p>
<p>On.</p>
<p class="bg">If I could figure out how to die, I'd do it.</p>
<p>Off.</p>
<p class="bg">I don't even care if it's cheating. I'd happily type a /cheat/code right into the address bar if I thought it would get me out of here.</p>
<p>On.</p>
<p>Off.</p>
<p>On.</p>
<p class="smalltext">Help.</p>
""".format(url_for('jam_cheat', code='code'))}]

	page = pages[session['page']]
	page['links'] = ['<a href="{}">continue</a>'.format(url_for('jam_story'))]

	session['page'] += 1
	if session['page'] > 2:
		session['walkthrough'] = True
	if session['page'] > len(page):
		page['links'] = ['<a href="{}">back to main menu</a>'.format(url_for('jam_index'))]
		session.pop('page')
		if session['mode'] == 'start':  # if it's locked...
			session['mode'] = 'surface'  # unlock /play

	return inflectr.inflect(render_template('jam_play.html', **page))

@app.route('/jam/walkthrough')
def jam_walkthrough():
	if not 'mode' in session:  # new players start at the beginning
		return redirect(url_for('jam_index'))

	if not 'walkthrough' in session:  # not unlocked yet
		return redirect(url_for('jam_story'))

	pages = {
		'start': {'title': 'Walkthrough', 'description': """
<p>TODO: play game, write walkthrough</p>
"""},
		'surface': {'title': 'Walkthrough: The Surface', 'description': """
<center><img src="/static/jam/rooms.gif"></center>
<p>When the game opens, you're just inside the front door of a small but cheerful house, facing the brightly-lit first floor hallway. Behind you is a sturdy wooden door with a shiny lock.</p>
<p class="bg">The object of the game is to unlock this door. Of course, it won't be the first thing you do, but it may be the last. <!-- I have no idea how you win this game, but it sounds plausible. Don't room escape games always tease you with the exit at the start? --></p>
<p>The hallway branches off into a few rooms: a living room with several electronics to interact with, a kitchen with the usual kitchen appliances and a door to the back yard, and a set of thick-carpeted stairs leading up to the second floor. On the second floor, there are a pair of bedrooms and a bathroom.</p>
<p>In the living room, you can watch the TV <!-- if you want to stare at an ugly station logo -->. There's also a computer with a few apps: a simulated IRC window full of "I hate this theme! I can't think of anything!", a fake web browser that only goes to ludumdare.com, an IDE with some game code, even a test window with a little screenshot of itself. <!-- This is the most self-referential game I've ever seen. It's like it was written by a flaming demon that feeds on being the center of attention. --> The light switch on the wall even changes the background color of the page! A couch with a pettable pet NPC on it and a fluffy black-and-white rug shaped like a cartoon face complete the room.</p>
<p>The kitchen has a refrigerator, stove, microwave, table, and dishwasher, and a minigame involving clicking on it all in the right order under the time limit. <!-- Please do not ask me how to beat it. --> A grandmotherly NPC insists on "helping" her favorite person by politely explaining the rules over and over.</p>
<p>The back door leads to a fenced yard with a small garden and a doghouse with another friendly pet NPC. <!-- that's supposed to be a dog? -->The sky above is bright blue with fluffy clouds and an occasional bird.</p>
<p>Upstairs, one of the bedrooms is locked and the other apparently belongs to you. Your room has a cheap craft-store wooden "S" painted white on the door. Inside are a bed, some posters, and a closet full of clothes, all white. <!-- Who hangs plain white posters on a white wall? I can't figure out if my avatar is supposed to be insane, or if the artist was just lazy. --> The door with a glossy black carbon-fiber "B" on it is locked, but you can slip items under the door <!-- if your inventory is full of rotten food from trying the kitchen minigame -->. In the bathroom are various plumbing items that you can interact with, and a mirror so you can see what your avatar looks like. <!-- Spoiler: you're as poorly drawn as everything else. --></p>
<!-- Okay, that's all the rooms.  Now what? -->
<p>You'll have to find the key to the front door on your own. Try all the minigames. <!-- That should keep them busy for a while. --> Good luck!</p>
<p>&lt;-- TODO: There has to be more to the game than this. What happened to the combat scenes I saw in the other save file? <span class="bg">I can't find a even single way to die. --></span></p>
"""},
		'beneath': {'title': 'Walkthrough: Beneath the Surface', 'description': """
<center><img src="/static/jam/rooms_beneath.gif"></center>
<p>When the game opens, you're just inside the front door of a small, claustrophobic house, facing the narrow first floor hallway. Behind you is a cold steel door with an impressive array of locks and chains.</p>
<p class="bg">The object of the game is to unlock this door. Of course, it won't be the first thing you do, but it may be the last. <!-- I have no idea how you win this game, but it sounds plausible. Don't room escape games always tease you with the exit at the start? --></p>
<p>The hallway branches off into a few rooms: a living room with several broken electronics, a kitchen with a few dirty pots and pans and a door to the back lot, and a set of rickety stairs leading up to the second floor. On the second floor, there are a pair of bedrooms and a bathroom.</p>
<p>In the living room, the TV is broken. The light switch on the wall doesn't do anything. An old couch covered in trash is the only thing on the bare, splintered floorboards.</p>
<p>Dirty dishes fill the sink in the kitchen. A battered old microwave is the only appliance. Not that it matters, since there isn't any food. A pale spot on the wall over a square white spot on yellowing floor shows where the refrigerator used to be. A small table has room for only one chair.</p>
<p>The back door leads to a fenced dirt lot. A pile of wooden boards, some with rusted nails still stuck in them, leans against the side of the house. Patches of yellow scrubgrass struggle to survive around the base of the fence. The sky is a birdless dull gray.</p>
<p>Upstairs, one of the bedrooms is locked and the other apparently belongs to you. Your room has a glossy black carbon-fiber "B" on it, to match most of your posessions. Black satin sheets coordinate with your black leather wardrobe. A single poster-sized sheet of glossy black paper decorates the matte black walls. In the bathroom, the overflowing trash can is all but lost beneath the results of the overflowing plumbing. A mirror taunts you with your own face.</p>
<p>There is no way to unlock the door.</p>
<p>You don't want that.</p>
<p>You will stay in this house until you die.</p>
"""},
		'fail': {'title': 'Walkthrough: Failure', 'description': """
<p>I don't know what's wrong with this game. I'm not even dying anymore, it just cuts straight to my corpse with the evil NPCs standing over it. Staring.</p>
<p>Why can't I stop playing?</p>
<p>I wish there was a way to enable multiple save files. Maybe then it would let me start over. I've tried a few <a href='{}'>cheat codes</a>, but I couldn't figure out the right one.</p>
<p>I wish I could start over.</p>
<p>&nbsp;</p>
<p>Oh, I found the piece of paper that was stuck in the drive at first, remember? The one I thought was an inspection sticker?</p>
<p>It's a piece of folded paper with a black ink symbol on the inside and a red X on the outside. I don't think I have to tell you what the symbol is.</p>
<center><img src="/static/jam/paper.jpg"></center>
""".format(url_for('jam_cheat', code='code'))},
		'multi': {'title': 'Walkthrough: The Second Save', 'description': """
<p>Obviously Bad Hint from the Game Pretending to Be Me: try getting yourself killed!</p>
"""},
		'final': {'title': 'Walkthrough: The Final Save', 'description': """
<p>Okay, I've finally got this game figured out. There's no way to win from inside the game. You have to give it what it wants, <b>outside</b> of the game.</p>
<p>What does it want? It won't tell me. It just says it's not for me know, that it was my place to write the walkthrough that would guide the winner, but not to be the winner myself.</p>
<p class="smalltext">But if I had to guess, I'd say that, like all of its kind, it just wants to spread the infection.<p>
"""}}

	page = pages[session['mode']]
	page['links'] = ['<a href="{}">return to main menu</a>'.format(url_for('jam_index'))]

	return inflectr.inflect(render_template('jam_play.html', **page))

@app.route('/jam/play')
def jam_play():
	if 'mode' in session:
		if session['mode'] == 'surface':
			return inflectr.inflect(render_template('jam_play.html', title='The Surface', links=['<a href="{}">return to main menu</a>'.format(url_for('jam_index'))], description="""
<p>You are in a small, cheery house.The walls are off-white with white trim. The front door is locked. Your TV and computer are in the living room. Softly carpeted stairs lead up to your bedroom.</p>
<p>The local NPCs are smiling and friendly.</p>
<p>You may turn the lights on and off.</p>
"""))

		if session['mode'] == 'beneath':
			return inflectr.inflect(render_template('jam_play.html', title='Beneath the Surface', links=['<a href="{}">look around</a>'.format(url_for('jam_play')), '<a href="{}">die</a>'.format(url_for('jam_die'))], description="""
<p>You are in a small, dark house. Brownish paint peels off in long strips from the decaying walls. The front door lock is rusted shut. The living room has been looted of all valuables that weren't nailed down, all valuables that were nailed down, and the nails themselves. Metal prices must be up again.</p>
<p>The stairway leading down to your bedroom looks wobbly but usable, as long as you're up to date on your tetanus shots.</p>
<p>You may turn the lights on and off, but the bulbs were stolen years ago.</p>
"""))

	return redirect(url_for('jam_index'))

@app.route('/jam/die')
def jam_die():
	if not 'deaths' in session:
		return redirect(url_for('jam_index'))

	session['deaths'] += 1

	if session['mode'] == 'beneath':
		if session['deaths'] < 3:
			return redirect(url_for('jam_dead'))
		else:
			return redirect(url_for('jam_fail'))

	if session['mode'] == 'multi':
		session['mode'] = 'final'
		return redirect(url_for('jam_final'))

	return redirect(url_for('jam_index'))

@app.route('/jam/dead')
def jam_dead():
	return inflectr.inflect(render_template('jam_play.html',
		title='You have died',
		links=['<a href="{}">back to main menu</a>'.format(url_for('jam_index'))],
		description="""
<p>[image of your dead avatar. a local NPC smiles sadly]</p>
"""))

@app.route('/jam/fail')
def jam_fail():
	session['mode'] = 'fail'
	return inflectr.inflect(render_template('jam_play.html',
		title='You have failed',
		links=['<a href="{}">I am a failure.</a>'.format(url_for('jam_index'))],
		description="""
<p>[an unskippable cutscene of NPCs laughing at your corpse]</p>
		"""))

@app.route('/jam/cheat/<code>')
def jam_cheat(code):
	if code.lower() in ['restart']:
		session.clear()
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>You feel completely free.</p>
""".format(code.upper())}

	elif code.lower() in ['quit', 'exit', 'die', 'death', 'dead', 'kill', 'killme', 'suicide'] and session['mode'] in ['surface', 'beneath', 'multi']:
		if session['mode'] == 'surface':
			session['mode'] = 'beneath'
			session['deaths'] = 0
		else:
			session['deaths'] += 1
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>You feel cold and lifeless.</p>
<p>You feel a sudden rush of paranoia. What if someone saw you cheat? You don't want that.</p>
<p>You hope this doesn't cause any weird glitches in the game.</p>
""".format(code.upper())}

	elif code.lower() in ['beneath'] and session['mode'] == 'fail':
		session['mode'] = 'multi'
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>Your vision doubles for a moment.</p>
<p>You feel a sudden rush of paranoia. What if everyone saw you cheat? You don't want that.</p>
<p>You don't want that.</p>
<p>You hope the game isn't angry with you.</p>
<p>You really hope the game isn't angry with you.</p>
""".format(code.upper())}

	elif code.lower() in ['two', 'twofiles', 'many', 'manyfiles', 'enablemanyfiles', 'more', 'morefiles', 'enablemorefiles', 'multiplefiles', 'enablemultiplefiles', 'enablefiles'] and session['mode'] == 'fail':
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>Your vision doubles for a moment, then clears.</p>
<p>A wave of relief washes over you. Cheating is wrong. You don't want that.</p>
<p>You feel like you barely avoided getting into Big Trouble.</p>
<!-- You're on the right track...but what's the code? -->
""".format(code.upper())}

	elif code.lower() in ['idontwantthis']:
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>You have found a secret achievement!</p>
<p>...but nothing happens.</p>
""".format(code.upper())}

	else:
		page = {'description': """
<p>You use the cheat code {}.</p>
<p>Nothing happens.</p>
<p>A wave of relief washes over you. Cheating is wrong. You don't want that.</p>
""".format(code.upper())}

	if not 'links' in page:
		page['links'] = ['<a href="{}">back to main menu</a>'.format(url_for('jam_index'))]

	page['title'] = 'cheat {}'.format(code.upper())

	return inflectr.inflect(render_template('jam_play.html', **page))

@app.route('/jam/play/<filename>')
@app.route('/jam/play/<filename>/<room>')
def jam_play_file(filename, room=None):
	if filename == 'YOU_FAILED':
		return inflectr.inflect(render_template('jam_play.html', title='You have failed again', links=['<a href="{}">I am a repeated failure. I shall return to the main menu in shame.</a>'.format(url_for('jam_index'))], description="""
<center><img src='/static/face_down.gif'></center>
<p>[image: the NPCs continue silently staring at your corpse]</p>
"""))

	if filename == 'BENEATH':
		if not room:
			return inflectr.inflect(render_template('jam_play.html', title='Far Beneath the Surface', description="""
<p>You are in a small, dark house. Brownish paint peels off in long strips from the decaying walls. The front door lock is rusted shut. The living room has been looted of all valuables that weren't nailed down, all valuables that were nailed down, the <a href='{}'>nails</a> themselves, and most of the floor.</p>
<p>The <a href='{}'>stairway</a> leading down to your bedroom looks wobbly but usable, as long as you're up to date on your tetanus shots.</p>
<p>You may turn the lights on and off, but the bulbs were stolen decades ago.</p>
""".format(url_for('jam_play_file', filename='BENEATH', room='nails'), url_for('jam_play_file', filename='BENEATH', room='stairway'))))

		rooms = {
			'nails': {'title': 'A Rusty Nail', 'links': ['<a href="{}">continue</a>'.format(url_for('jam_play'), filename='BENEATH')], 'description': """
<p>You find a single rusty nail that all the previous scavengers somehow missed.</p>
<p>It is sharp and rusty and might kill you instantly.</p>
<p>You don't want that.</p>
"""},
			'stairway': {'title': 'A Wobbly Stairway', 'links': ['<a href="{}">Yeah, right. Let me into my room already.</a>'.format(url_for('jam_play'), filename='BENEATH'), '<a href="{}">It\'s what I deserve.</a>'.format(url_for('jam_die'))], 'description': """
<p>You fall down the stairs and die.</p>
"""}}
		page = rooms[room]
		return inflectr.inflect(render_template('jam_play.html', **page))

	if filename == 'DONT_FAIL_AGAIN':
		return inflectr.inflect(render_template('jam_play.html', title='Failure is Not an Option', links=['<a href="http://www.ludumdare.com/compo/ludum-dare-29/?action=preview&uid=13938">vote</a>', '<a href="{}">return to main menu</a>'.format(url_for('jam_index')), '<a href="{}">cheat: RESTART</a>'.format(url_for('jam_cheat', code='restart'))], description="""
<p>Vote for this game or it will eat your soul.</p>
<p class="bigtext">THE END</p>
"""))

	return inflectr.inflect(render_template('jam_play.html', title='Bad Filename', links=['<a href="{}">back to main menu</a>'.format(url_for('jam_index'))], description="""
<p>There is no save file named {filename}.</p>
<p>&nbsp;</p>
<p>Are you trying to cheat?</p>
<p>I hope you're not trying to cheat. That might make the game angry.</p>
<p>You don't want that.</p>
<p class="smalltext">also, the correct URL is /cheat/&lt;code&gt;</p>
"""))

@app.route('/jam/final')
def jam_final():
	return inflectr.inflect(render_template('jam_play.html',
		title='The Warning',
		links=['<a href="{}">back to main menu</a>'.format(url_for('jam_index'))],
		description="""
<p>[the game overtly threatens you unless it gets what it wants, but doesn't tell you what it wants]</p>
"""))
