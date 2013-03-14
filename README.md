# seamless

sublime plugin for real-time collaboration

Note: the full demo is meant to be run on two machines,
each running sublime with the seamless plugin installed.

Repeat the following steps for both computers.

Installation:
========

Install the sublime text editor.

Next, install the following dependencies, assuming you have pip:

````
sudo pip install sleekxmpp
sudo pip install dnspython
sudo pip install pyasn1
sudo pip install pyasn1-modules
````

Clone this branch anywhere:

  git clone -b stuff git@github.com:fireblade99/seamless.git

Next, go to the Packages folder of sublime:

  cd ~/.config/sublime-text-2/Packages/

Create a folder called seamless:

  mkdir seamless
  cd seamless

Place the file called seamless.py from this code repository into the plugin folder you just created.

  cp seamless.py ~/.config/sublime-text-2/Packages/seamless

You are now ready for execution.

Execution:
========
The plugin is set up so that there are two clients which login automatically when run:
1. butteryseamless@gmail.com
2. olinseamlesstest@gmail.com

On computer 1, you will be running the scripts for "buttery".
On computer 2, you will be running the scripts for "olinseam".

First, run buttery_recv.py on computer 1:
python buttery_recv.py

Then, open sublime on computer 1.

Now, run olinseam_recv.py on computer 2.
python olinseam_recv.py

Next, open sublime on computer 2.

Now you should run the send scripts on each computer.

computer 1:
python buttery_send.py

computer 2:
python olinseam_send.py

You're done!

Start typing in one of the sublime text editing windows.
As soon as you go to the other computer and enter text there, the changes should show up!

