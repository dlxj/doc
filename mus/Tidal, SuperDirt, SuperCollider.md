

Tidal is made for generating patterns, but doesn’t itself make any sound.  
Tidal will by default send messages to SuperDirt in order to trigger sounds.  

SuperDirt written in SuperCollider.    
SuperDirt comes with a fairly large library of sound samples, as well as a range of synthesisers.  
SuperDirt is also possible to register MIDI devices with SuperDirt, so that you can trigger external sounds on soft/hardware synthesisers.  

SuperCollider is a very well developed programming language that is designed for sound synthesis (and digital signal processing in general) that can itself be live coded. By default though, you’ll just use it in order to host SuperDirt.

《The SuperCollider book》 mit press  


d1 $ s "cp supermandolin"    
SuperDirt will play a short sound sample, which it will find inside a folder called cp on your computer.    
You can find it from SuperCollider – from the menus select ‘open user support directory’, and then open ‘downloaded-quarks’ and then ‘Dirt-Samples’. You’ll see a bunch of ‘.wav’ files inside the cp folder, because cp isn’t a single sound but a set of them known as a ‘soundbank’. By default SuperDirt will play the first one – to play the second, you can specify cp:1 in your pattern instead (it starts counting at 0).    

You won’t find a folder in Dirt-Samples called supermandolin, because that is a synthesiser rather than sample-based soundbank.   
You can play notes as numbers like this:   
d1 $ note "0 7 12" # s "supermandolin"   
or as note names like this:  
d1 $ note "c gs7 c6 gf4" # s "supermandolin"  

(If supermandolin isn’t working for you, it’s almost definitely because sc3-plugins isn’t installed properly, which is required by most synths.)

在MIDI中，音符由从0到127的数字表示，其中音符21到108正好对应大钢琴的88个按键

《Computer Music using SuperCollider and Logic Pro》

Each key on the piano is a MIDI number. The lowest note musicians use is C-1, which has the MIDI number 0. The number 12 = C0, 24 = C1, 36 = C2, 48 = C3, 60 = C4 (which is middle C on the piano, remember this one and you can quickly calculate the others), and so on. Music theorists use C4 for middle C. Unfortunately, this is not standard among synthesizers: some MIDI equipment uses C5 for MIDI pitch 60, which makes MIDI 0 a C0, and Logic uses C3 for middle C. Sorry. Each piano key is 1 number. C#4 would be 61. The pitch A-440 is above middle C so it is 69. Here is our theme in MIDI: 60, 62, 63, 60, 66. You can use decimal precision with MIDI, so 60.00, 62.00, etc. would work. It should look familiar. MIDI and cents are the same. 

Orchestral Sound texture v1  by nicolaariutti

I've used samples from the SSO (https://github.com/peastman/sso).


// Orchestral Sound texture v1

(
s.options.numBuffers = 1024 * 32;
//increase the memory available to the server
s.options.memSize = 8192 * 128;
)
//boot the server
s.boot;



//LOAD SAMPLES //////////////////////////////////////////////////////////////////

// VIOLINS 1 
(
var tmp_buffers;
var tmp_array;
var path;

// 1. load samples from a folder extracting only one channel from the stereo files
path = PathName("/home/nicola/Musica/samples/Sonatina Symphonic Orchestra/Samples/1st Violins/");
path.entries.do{
	|item|
	if( item.fileName.contains("1st-violins-sus-"),
		{
			//item.fileName.postln;
			//item.fullPath.postln;
			tmp_buffers = tmp_buffers.add( Buffer.readChannel(s, item.fullPath, channels:1));

		},{	//do nothing
		}
	);
};

// 2. create an array of dictionaries
tmp_array = Array.newClear();

https://www.youtube.com/watch?v=Ff7X5JFyxK4  
vst plugins in supercollider  
found this accidentally https://git.iem.at/pd/vstplugin  

Here’s the source: https://git.iem.at/pd/vstplugin/tree/develop 4
Windows binaries (64 bit): https://drive.google.com/open?id=15rxPZLPLdIfQU6nokcQu2GrDBxW_ld9n 3
macOS binaries: https://drive.google.com/open?id=1U7r5NmHu30sk-hnFYKTt23V1TeRqt_so 

https://github.com/supercollider/sc3-plugins

VstPluginController.schelp
VstPlugin.scx
VstPlugin.schelp
VstPlugin.sc


Here is an example with MDA ePiano VST on Mac OS X.

VstPlugin.makeSynthDef.add;

~vst = VstPlugin.new([\nin, 0, \nout, 2, \out, 0, \replace, 0], s, addAction: \addToHead);

~vst.open("/Library/Audio/Plug-Ins/VST/mda ePiano.vst", info: true);



(

Event.addEventType(\vstPlugin, { |server|

	var notes = [

		~midinote.value,  // 0

		~ctranspose.value,  // 1

		~velocity.value, // 2

		~sustain.value, // 3

		~lag.value, // 4

		~timingOffset.value, //5

		~instrument, // 6

		~midiChannel.value, // 7

	].flop;

	var timeNoteOn, timeNoteOff;



	notes.do { |note|

		// sustain and timingOffset are in beats, lag is in seconds

		timeNoteOn = (thisThread.clock.tempo.reciprocal*note[5])+note[4]+server.latency;

		timeNoteOff = (thisThread.clock.tempo.reciprocal*(note[3]+note[5]))+note[4]+server.latency;



		SystemClock.sched(timeNoteOn, {

			note[6].midiNoteOn(chan: note[7] ? 0, note: (note[0]+note[1]).asInteger, veloc: note[2].asInteger.clip(0,127));

		});

		SystemClock.sched(timeNoteOff, {

			note[6].midiNoteOff(chan: note[7] ? 0, note: (note[0]+note[1]).asInteger, veloc: note[2].asInteger.clip(0,127));

		});

	}

});

)



(

Pbind(*[

	type: \vstPlugin,

	instrument: ~vst,

	dur: 4,

	degree: [0, 4],

	velocity: 64

]).play;

)



// straight timing

(

Pbind(*[

	type: \vstPlugin,

	instrument: ~vst,

	legato: Pgauss(0.2,0.05,inf),

	dur: 0.2,

	degree: [2,5,12],

	ctranspose: Pseq([0,0,0,0,4,4,4,4,5,5,5,5],inf),

	velocity: Pgauss(64,10,inf),

]).play;

)



// loose timing

(

Pbind(*[

	type: \vstPlugin,

	instrument: ~vst,

	legato: 0.1,

	dur: 0.2,

	midinote: [66, 69, 74],

	lag: Pwhite(-0.05!3, 0.05)

]).play;

)

VstPluginController.schelp
VstPlugin.scx
VstPlugin.schelp
VstPlugin.sc

