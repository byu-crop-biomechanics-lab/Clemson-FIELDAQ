The Poor Undergraduate's Guide for Surviving and Fixing Bugs in the DARLING Software
===========================

Goal
----
For a mechanical engineering with a rudementary understanding of coding to be able to understand the DARLING code base and be able to fix minor bugs. 

Outline
--------

1. Get familiar with the BYU Crop Biomechanics Lab Github page
2. Set up the DARLING GUI on your computer
3. Learn how to navigate the code base. 
4. Fix bugs and upload them to the DARLING Devices

Crop Biomechancis Github
--------

-Since you are reading this, clearly you are on the BYU Crop Biomechanics Lab Github page. Good job. Are you on the Clemson-FIELDAQ repository? Again, clearly. Another win. The Clemson-FIELDAQ repository is where all of the magic is going to happen, so make sure you know how to get here and stay here. 

-Like me, you probably are a poor undergraturate mechanichical engineer that has never taken a class where they taught you how to use Github and Git. Thats ok, its not your fault. But nevertheless, still important to know. Github and Git help us work collabortivly on code without making a mess of things. So unless you want to make a mess and have other people get frusterated with you, complete action item 1 below.
    
!Action Item 1! Become familiar with Github and Git
-I'll let you have more free reign on this one. However you do it, you should become familiar with and know how to use the following features: Clone a repository, create a branch, stage changes, committ changes, push, sync. You should also be able to explain to your super intelegent, tech savy Grandma what Github and Git are in 30 seconds.

-Similar to your friend being an identical quadruplet, there are four repositories on Github that have code for the DARLING, and getting the confused about which one to work on can lead to some akward situations. Especially when someone is wondering why none of your changes work on the physical DARLINGS because you were accedentally working on the wrong repository. With that in mind, complete aciton item 2 below. 

!Action Item 2! Become familiar w/ the 4 repositories
-No free reigns here. Read this super boring report prepared by yours truley. [FIELDAQ Repository Relationships.pdf](https://github.com/byu-crop-biomechanics-lab/Clemson-FIELDAQ/blob/Main/FIELDAQ%20Repository%20Relationships.pdf)

-What Repository are we working on? Say it with me! Clemson-FIELDAQ!. And don't forget it. (ps, if you actually said it out loud, mad respect, and I'm sorry if people looked at you weird). But its ture, Clemson-FIELDAQ contains the software actually used on the DARLINGS, so that is the code base we need to work on


DARLING GUI
--------
-Now lets get to the fun part where you get the code on your computer and spend hours frusterated that its not working. (Only hours, and not days, because you are following this super helpful guide.) Complete actioin items 3-4

!Action Item 3! Verify you have VS code and Git installed
-Not much more to it then that. If you don't have VS code and Git installed, then figure out how to do it.

!Action Item 4! Run the following commands in a Bash Terminal
-In theory, this should clone the repository for you and download all the neccecary dependencies into a virtual environment. In Theory. There were a couple things that didn't work all the way for me that I had to tweak to get everything running properly. However its been a while so I don't remember what those things are lol. Learn from my mistakes, if you have to fix anything, then I formally give you permission to edit this document to include better instructions. 

    $ git clone https://github.com/byu-crop-biomechanics-lab/Clemson-FIELDAQ.git
    $ cd Clemson-FIELDAQ/
    $ source build_project

-Well. Here is the test to see if it worked or not. Complete action item 5

!Action Item 5! Run the GUI
-Navigate to the src folder, find the file called main.py, and click run. Click the buttons, play around with it to make sure it is working properly. If you it keeps crashing when you try and take or view a test, take a look at the pro tip under action item 7

-Did it work??? Did the GUI pop up? If so, I humbly take a bow, you may call me a genius. If it didn't, sorry, I'm of no help. Use your well refined engineering debugging skills to fix it, and make sure you can do Action Item 5. When you have it up and running, take a humble bow and call your self a genius. (And make edits to this document so the next poor soul has better instructions)


Navigating the Code Base
--------
-Ok, now it gets a bit more fun. If you call being confused and clicking random buttons for hours on end fun. But I am going to run you through some exercises that will make you a little less confused and click random buttons with a little more purpose.

-But first, you are probably in need of a tidbit of info. Using your exccelent observant skills, you may have noticed that most files share the same name as another file, except one ends with .py and the other with .ky. An example is the TestingScreen.kv file and the TestingScreen.py file. Py stands for Python, and kv, for Kivy. These two files act like a good marraige should. They work together to creat something awesome. They work together to make a screen work. The Kivy files manage all of the static things on a screen. Things that you can only change if you go into the code and make some edits. The python files control anything dynamic. Anything that can change on a screen from a user using the GUI. The only exception to that is the Kivy files control what is the next screen that pops up when you hit a button. If you navigate to the documentation folder, you can find a couple documents that will teach you a little more about Kivy

-Now, understanding the difference between the Kivy and Python files is muy importante. It will save you quite a bit of debugging time if you at least know which file you should be looking at. So find that tech sevy Grandma you previously talked to about Github and Git, and teach her the difference between the Kivy and Python files. If you want. If not, just teach yourself again. 

-Ok, Ok, I promised more fun. Here it goes! After these excercises you are going to know how to navigate the DARLING code base better then the basement of the CB. (Although thats not saying much, I still get turned around down here). Complete Action Items 6-8. Answers are found at the end of this document. 

!Action Item 6! Find the name of the Python/Kivy files associated with the image linked below
[Action Item 6 image](Documentation/Begginers%20Guide%20Images/Action%20Item%206.png)
-Pro tip: Each python file associated with a screen has a funciton called 'def on_pre_enter()'. This function runs every time you enter a screen. So if you want to double check that the screen you are looking at on the GUI is indeed the python file you are looking at, type in "Print("You made it or something funny")" into the on_pre_enter function. Then rerun the GUI, and when you enter the screen associated with the python file with the print statement, you should see your text printed into your terminal. This way you can be sure that the screen you are looking at is the file you are looking at. Maybe not the most elegent of solutions, but seems fitting for a poor undergraduate mechanical engineer. 

!Action Item 7! Find the name of the Python/Kivy files associated with the image linked below
[Action Item 7 image](Documentation/Begginers%20Guide%20Images/Action_Item_7.png)
-Pro tip: Did it crash on you when you tried to look at the tests? Classic. Took me 67 minutes to figure out why. You need to make sure that you are running the main file from the src folder. So the last thing on the blue line in your terminal should be /src$. If not, it won't load data properly. 

!Action Item 8! Find the name of the Python/Kivy files associated with the image linked below
[Action Item 8 image](Documentation/Begginers%20Guide%20Images/Action_item_8.png)

-Finished items 6-8? NIIIIIICEEEE. We will make a software pro out of you yet. Really, finding the right files is two thirds the battle. If you want more practice navigating the code base, pick a random screen on the GUI, and prove what files are attached to it. There are also some resources in the Documentation folder that may help, but I found I learned best when I got down and dirty with the GUI. 

Fixing Bugs on hardware
--------
-Now what you are are really here to learn. Lets Debug some stuff!!!!!!!! Except I don't know what bugs are on the code now, so instead I am going to put you through some excercises that will prep you for when there is a nasty bug that rears its ugly head. This is also good time to stop, pause, and contemplate. Do you remember the difference between the Python and Kivy files? Complete action item 9-11.

!Action Item 9! Edit the title "Testing" on the screen linked below to say "Testing Popcorn"
[Action Item 9 image](Documentation/Begginers%20Guide%20Images/Action_Item_7.png)
-Don't get this onto the Actual Hardware yet. Just do it on the GUI, and prove that it works. Again, answers are found at the end of this document. 

!Action Item 10! Update the software on the Hardware with new code from Action Item 9
[Software Update Procedure.md](Documentation/Software%20Update%20Procedure.md)
-Use method 1 from the linked document as your instructions. Method 2 involves a little bit of sorcery, but you are free to tinker with it if wanted.

!Action Item 11! Revert the Title "Testing Popcorn" back to "Testing" on both the GUI and the hardware
-Yeah, sorry, that excercicse really didn't have any value, other than teaching you new skills. You're welcome

-Excelent. If you can do that, that you can do the hardest parts. For more practice, complete Action Items 11-12. And remember the difference between Python and Kivy!!

!Action Item 12! Make the big number shown in the image below count up by 4, instead of 1 every second
[Action Item 12 image](Documentation/Begginers%20Guide%20Images/Action_Item_12.png)
-Put this on the hardware, and then revert everything back to normal. This probably seems pointless, but remember, practice and pacience my young padawan. 

!Action Item 13! Edit the screen shown in the image below so when you press the back button, it goes to the test in progress screen from Action Item 12. 
[Action Item 13 image](Documentation/Begginers%20Guide%20Images/Action_Item_7.png)
-Put this on the hardware, and then revert everything back to normal.
-Pro Tip: The way you move to a new screen is by calling the name that the new screen is defined by. That name is not the name of the file, but rather the name found in the Kivy file. An example is line 16 of TestingScreen.kv that reads "name: 'testing_screen'". Any button that says move to testing_screen, will then go to the associated TestingScreen. So then you need to look at the associate Kivy file of the screen you want to navigate to in order to find the name to reference

Welp. That concludes "The Poor Undergraduate's Guide for Surviving and Fixing Bugs in the DARLING Software". Hopefully you did indeed survive, and do survive as you continue to work on the software. And if you found this guide somewhat lacking at times. Oops. My bad. But feel free to make it better!. 

Hasta la vista. 
-A fellow poor undergraduate who spent a decent amount of time figuring out how to do all this. 


Answers
--------

These answers are accurate as of December 16th, 2025 when this was written. It could be that something as changed sense then. 
Action Item 6: TestingScreen(.kv/.py) Found in Granusoft->src->view->screens->main folder
Action Item 7: TestFoldersScreen(.kv/py) Found in Granusoft->src->view->screens->main->testing folder
Action Item 8: TestingResultsScreen(.kv/py) Found in Granusoft->src->view->screens->main->testing folder

Action Item 9: Edit line 38 of TestingScreen.kv from "text: 'Testing'" to "text: 'Testing Popcorn'"
Action Item 12: Edit line 91 of TestInProgressScreen.py from "self.test_time = time_delta.seconds" to "self.test_time = time_delta.seconds*4"
Action Item 13: Edit line 34 of TestinScreen.ky from "root.move_to('main_screen')" to "root.move_to('test_in_progress_screen')"