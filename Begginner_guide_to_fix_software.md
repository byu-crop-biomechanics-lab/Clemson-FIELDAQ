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

1. Crop Biomechancis Github

    -Since you are reading this, clearly you are on the BYU Crop Biomechanics Lab Github page. Good job. Are you on the Clemson-FIELDAQ repository? Again, clearly. Another win. The Clemson-FIELDAQ repository is where all of the magic is going to happen, so make sure you know how to get here and stay here. 

    -Like me, you probably are a poor undergraturate mechanichical engineer that has never taken a class where they taught you how to use Github and Git. Thats ok, its not your fault. But nevertheless, still important to know. Github and Git help us work collabortivly on code without making a mess of things. So unless you want to make a mess and have other people get frusterated with you, complete action item 1 below.
    
        !Action Item 1! Become familiar with Github and Git
        -I'll let you have more free reign on this one. However you do it, you should become familiar with and know how to use the following features: Clone a repository, create a branch, stage changes, committ changes, push, sync. You should also be able to explain to your super intelegent, tech savy Grandma what Github and Git are in 30 seconds.

    -Similar to your friend being an identical quadruplet, there are four repositories on Github that have code for the DARLING, and getting the confused about which one to work on can lead to some akward situations. Especially when someone is wondering why none of your changes work on the physical DARLINGS because you were accedentally working on the wrong repository. With that in mind, complete aciton item 2 below. 

        !Action Item 2! Become familiar w/ the 4 repositories
        -No free reigns here. Read this super boring report prepared by yours truley. [FIELDAQ Repository Relationships.pdf](https://github.com/byu-crop-biomechanics-lab/Clemson-FIELDAQ/blob/Main/FIELDAQ%20Repository%20Relationships.pdf)

    -What Repository are we working on? Say it with me! 'Clemson-FIELDAQ!. And don't forget it. (ps, if you actually said it out loud, mad respect, and I'm sorry if people looked at you weird). But its ture, Clemson-FIELDAQ contains the software actually used on the DARLINGS, so that is the code base we need to work on

    -Now lets get to the fun part where you get the code on your computer and spend hours frusterated that its not working. (Only hours, and not days, because you are following this super helpful guide.) Complete actioin items 3-4

        !Action Item 3! Verify you have VS code and Git installed
        -Not much more to it then that. If you don't have VS code and Git installed, then figure out how to do it.

        !Action Item 4! Run the following commands in a Bash Terminal
        -In theory, this should clone the repository for you and download all the neccecary dependencies into a virtual environment. In Theory. There were a couple things that didn't work all the way for me that I had to tweak to get everything running properly. However its been a while so I don't remember what those things are lol. Learn from my mistakes, if you have to fix anything, then I formally give you permission to edit this document to include better instructions. 

        $ git clone git@github.com:byu-crop-biomechanics-lab/FIELDAQ-Software-and-Electronics.git
        $ cd FIELDAQ-Software-and-Electronics/
        $ source build_project











    1. Review, or learn, about git hub and git hub edicut so we don't go around making an online mess of things that the next person can't understand. 