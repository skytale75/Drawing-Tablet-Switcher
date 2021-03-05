# Drawing-Tablet-Switcher
Simple python script I threw together to toggle which screen my drawing tablet stylus is bound to, figured it might help others.

setup instructions

    step 1
    Type "xsetwacom --list" into your terminal, it should reply something like . . .

    HUION PenTablet Pen stylus   <---	id: 10	type: STYLUS    
    HUION PenTablet Pad pad         	id: 11	type: PAD


step 2
Then copy and paste the name of your stylus, pad, or whatever to the appropriate variable in the 'toggle' file and save.

    Example:
    pen_name = "HUION PenTablet Pen stylus"
    pad_name = "HUION PenTablet Pad pad"
    cursor_name = "na"
    eraser_name = "na"

if xsetwacom --list doesn't return an eraser or cursor . . . leave them as "na".

step 3
Copy the "toggle" and "status.txt" file to your "~/bin" directory.
if you don't have a "~/bin" directory, in the terminal type

    cd ~/
    mkdir bin
    chmod +x bin

Move the two files into the `~/bin' directory.

step 4
create a shortcut for your system, I set mine to the "F3" key, command = toggle.
you can also bind the script to autostart with the system to make sure the tablet
automatically binds to the primary monitor.

you may have to change the permissions on the "toggle" file

    cd ~/bin
    chmod +x toggle