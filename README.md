# How to record lectures with minimal after-edits
(author: Stefan Harmeling, created: 2020-09-02, license: CC BY-SA 4.0)

There does exist quite a bit of information about this topic at the HHU
wiki, e.g.

* https://wiki.hhu.de/display/HHU/Bereitstellung+von+Lehrvideos+und+Veranstaltungsaufzeichnungen
* https://wiki.hhu.de/pages/viewpage.action?pageId=160268766
* https://wiki.hhu.de/pages/viewpage.action?pageId=160268775

In particular, the colleagues from the Multimediazentrum (MMZ@HHU) are really
helpful with many questions I had.

Here are simple setups that I use to record my lectures with
a Mac.


## TLDR / useful software
* Camtasia (to record screen and mic)
* Display Menu (to reduce the screen resolution to non-retina)
* Quicktime Player (to show handwriting on an ipad)
* Paper (on ipad for handwriting)
* Visualizer (for showing the webcam in a window)
* Apptivate (to switch between programs with function keys)
* Horo (to show a stopwatch in the menubar)

## Simplest setup / more details

**Hardware**: a laptop with builtin microphone (I use a 2014 Macbook
Pro)

**Software**: Camtasia

**Steps**: 
1. start Camtasia to record the screen and the microphone, it let's
   you select what to record, just choose screen and mic.
2. give the lecture using Powerpoint, Keynote, Preview (PDF), ...
3. stop Camtasia recording by clicking on some menubar item that looks
   like two frames of a film
4. in Camtasia export the video with "Share" --> "Local File", set parameters: "Export to MP4", click on "Options", under Video (as suggested by MMZ@HHU):
    * Framerate 25
    * Data Rate: 1000 kbits/sec
    * Keyframe Rate 30
5. get a tea while exporting takes place (can take 30 minutes)
6. upload video to the mediathek


## Reduce screen resolution (don't record retina resolution!)

**Problem**: assuming a Retina display on the Mac, the display might
tell you that the resolution is 1280x800, but actually it is recording
2560x1600 since it is "retina".  So the file of the video is very
large, possibly the quality is also not great or the sync between
audio and video is broken, because your computer is quite busy writing
out the high resolution to disk.

**Solution**: use the App "Display Menu.app" to reduce the resolution.
E.g. on my laptop there are in that application two options with
1280x800 one with a white-background "16:9" icon, one with a dark one.
Choose the dark one (as explained in its documentation)!  In
Camtasia's recording dialog you should see the "real" numbers of the
resolution you are about the record.  So try this with Retina, you see
2560x1600 in Camtasia's dialog, using "Display Menu" you can reduce it
to 1280x800.  There might be other apps that can correctly set the
resolution to non-retina.  The builtin preference panel "Displays"
sometimes can do it (try clicking on it with 'option' key), mine can
not.

## Chop out only 1280x720 (i.e. omit top 80 pixels)

**Problem**: you are also recording (if not in fullscreen mode) the
menubar on the top of the screen or for other reasons you want to use
some "standard" image format.

**Solution**: choose "720p HD (1280x720)" from "Preset region" in
Camtasia's recording dialog.  Then move the appearing rectangle to the
bottom part of your screen and leave a margin on top.  "720p HD" is
also a good format for uploading to the mediathek website (so less
editing required afterwards).

**Note**: also presenting in fullscreen removes the menubar, but the
chop-out-setup has the added value, that you can show during the
lecture other information (e.g. a website or your text editor for live
programming or a youtube video) and everything will be recorded by
Camtasia.

## Tip: timer in the menu bar

**Problem**: after the recording you would like to get rid of some
passages of your video, but how can you quickly find the exact
locations afterwards in the editor of Camtasia?

**Solution**: let a timer/stopwatch (with seconds) run in the menubar
(e.g. Horo.app works well, or put a stopwatch on your table).  If you
want to redo something during the recording (for home made lectures),
write down the time of the timer on a sheet of paper and redo the
passage until you are happy with it.  After finishing the whole
lecture (in one big recording) cut out the failed parts using the
Camtasia editor.  For this go backwards through your paper list of
times and backwards in time through the video.  You find the position
immediately using the time stamps.


## Include handwriting into your recording

**Problem**: how can I show and record handwriting?

**Solution**: connect an iPad to your Mac with a cable.  Then start
the application "QuickTime Player" and choose "File"-->"New Movie
Recording" from the menu.  A window opens with a red recording button
in the middle of the lower part.  Right next to that button is a down
arrow, looking like a "v".  Click on it and choose "ipad".  Now the
window should show everything you are doing on the ipad.  Now if
during your Powerpoint presentation you want to show some handwriting
(e.g. deriving `P=NP` for `N=1`), just switch to the "Quicktime Player"
application and start writing.  After that just switch back to your
presentation.  Camtasia will record everything it sees on the screen,
so also your handwriting will be recorded.

**Note**: what app for writing?  I like "Paper", since it is just a
white sheet of paper without any menu (if you set it up properly).

**Note**: to quickly switch between apps during your lecture, assign
your function keys to directly switch to a particular application
(e.g. using the tool "Apptivate", there might be other ways to do
that).

**Note**: why not use "QuickTime Player" instead of "Camtasia" for
screen recording?  The problem with "Quicktime Player" is that its
recording files are much bigger than those of "Camtasia".


## Include a video of yourself (for home made lecture videos)

**Problem**: how can I also show a video of myself without much
editing?

**Solution**: of course Camtasia can also record your webcam in
addition to the screen in separate tracks.  However, you would have
to do some editing afterwards to show it in the corner of the final
video.  There is a simpler solution.  Just start a program
that shows the video of the webcam in some window and position it on
your screen.  For this to work nicely, your presentation program
should also run the presentation in a window.  Preview (PDF) can do
this.  Also Powerpoint can do that (from the menu "Slide Show"-->"Set
Up Show..." choose "browsed by an individual (window)").  Since
version 10 also Keynote can do that: menu "Play" --> "Play Slideshow
in Window".

**Note**: what program to use to the video of the webcam?  I use
"Visualizer" from IPEVO (however, lately it was showing ads, if you
don't own an IPEVO, not sure whether they removed that "bug").  If you
are familiar with the commandline and python/opencv you could also use
a little script that Tobias Uelwer and I wrote for this purpose.  It
allows you to also choose the aspect ratio, crop and mirror the image,
make it grayscale.  The script is called `webcam-sh.py` and is
included in this repository.  Start it with `python webcam-sh.py` or
with parameters, e.g.

    python webcam-sh.py -p 0 223 -s 0.302500 -c 300 0 680 720

works for me.  While running you can use some hotkeys (see code) to
change settings.  After quitting (q) it will show you how to call it
next time to get the settings immediately.

## Include a video of yourself (during lectures in classrooms)

**Problem**: can I use the trick to show the webcam output on the
screen (instead of editing it into the video afterwards) in classroom?

**Solution**: get an external camera for this purpose!  I use an IPEVO
V4K USB document camera with a 5 meter USB extension cable (this is
at the limit of USB, try a shorter one if it is not working).  The
camera is placed in the front or second row and then just show the
video of that camera on the screen to include it in your lecture video.

**Note**: the only problem with this setup is that also the beamer
will project the video of yourselves, but it almost eliminates the
video editing afterwards.

## Externals microphones?

**Problem**: sound from the internal microphone might not be great,
especially when you walk around in a classroom 

**Solution**: get a better microphone!  I use a Rode NT-USB-mini for
home made lectures (and video conferences), but there are many
alternatives.  After plugging it in you can select it in Camtasia's
recording dialog and check the level.  For classroom I use a
"Sennheiser XSW2-ME2 E", which is a wireless lavalier microphone with
a (non-battery) receiver that is then connected with a "LINE 2 USB
Behringer" cable that connects directly to the USB of the laptop.

**END** of the text (for now)
