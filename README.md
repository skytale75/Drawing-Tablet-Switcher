# Drawing-Tablet-Switcher
Simple python script I threw together to toggle which screen my drawing tablet stylus is bound to, figured it might help others.

setup instructions


step 1
Copy the "toggle" and "status.txt" file to your "~/bin" directory.
if you don't have a "~/bin" directory, in the terminal type

    cd ~/
    mkdir bin
    chmod +x bin

Move the two files into the `~/bin' directory.

step 2
create a shortcut for your system, I set mine to the "F3" key, command = toggle.
you can also bind the script to autostart with the system to make sure the tablet
automatically binds to the primary monitor.

you may have to change the permissions on the "toggle" file

    cd ~/bin
    chmod +x toggle