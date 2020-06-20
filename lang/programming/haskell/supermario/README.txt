Make "Super Nario GC"
http://d.hatena.ne.jp/authorNari/20080422/1208880928

in Haskell

This is Keera Studio's fork of Nario. The reason for this fork is: it's a great game,
t's a great example of Games implemented in haskell, and it should be maintained. The licence
remains the same, and if the author (or anyone else) wants to take the changes, they are
more than free to do so, provided that they comply with the licence terms.

This fork is work in progress. Some references to the original project may remain. This
does not imply that the original author (user mokehehe?) supports our claims or modifications
in any way.

* Operation
	Cursor key, ijkl
		Move up, down, left, right

	Space key, z
		Jump (A button)

	Shift key
		Dash (B button)

	Escape key
		Quit application



* Files
	data
	data/img
		images



* Environment
	Haskell compiler (GHC)

	SDL
	http://www.libsdl.org/

	Graphics.UI.SDL
	http://hackage.haskell.org/cgi-bin/hackage-scripts/package/SDL

	Graphics.UI.SDL.Mixer
	http://hackage.haskell.org/cgi-bin/hackage-scripts/package/SDL-mixer

  * Build
	make

  * Execute
	make run



* Reference
	Super Nario GC
	http://d.hatena.ne.jp/authorNari/20080422/1208880928

	1-1 map
	http://www.geocities.co.jp/SiliconValley-Sunnyvale/6160/newtech/m11.htm

	Font
	http://qtchicks.hp.infoseek.co.jp/fonts-nintendo.html

	unsafeInterleaveIO
	http://d.hatena.ne.jp/tanakh/20040803#p1

	Existential type
	http://d.hatena.ne.jp/keigoi/20080805/p2

	Cyclic import problem in Haskell
	http://d.hatena.ne.jp/ABA/20060627#p1

	Sound materials
	http://utm-game-web.hp.infoseek.co.jp/free-sound.htm
