## Performing a Software Update on the Device

### Method 1: Load files onto USB stick and move files
1. Format a flash drive to use the FAT file system. This can be done on Windows or on a Mac; look this up online if you're not sure how to do it.
2. Clear the flash drive so their is nothing on it
3. Copy the FIELDAQ folder over into the drive. (With the Clemson code, it is "FIELDAQ From ClemDarlingSMALL.img" folder you need to copy over. However, once it is copied over,you need to change the name to FIELDAQ)
4. If there is already a FIELDAQ folder and you know the code is the same code you've been working on, the easiest thing to do is replace the file that you edited, instead of replacing the entire FIELDAQ folder
5. Once the flash drive contains your new code, unmount if from your computer
6. Boot up the DARLING, then insert the flash drive into the DARLING
7. Navigate to settings an hit the "Update with USB" button
8. The screen will freeze. Wait until it unfreezes, then restart the DARLING
9. Verify any changes


### Method 2: Connecting to internet and pulling changes directly from github (Outdated)
1. Enter the command line on the pi device. The granusoft box interface can be exited on the main screen by selecting "Exit", then "Exit" again.
2. Plug in a USB keyboard. (SSH can also be used, but a keyboard is easier and this guide will assume you are using a keyboard.)
3. Connect the device to internet. This can usually be done by running "sudo raspi-config" and using the menu that provides. If more instructions
   are needed, refer to: https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
   You can also use an ethernet cable instead of a wireless connection.
4. Ensure you are in the FIELDAQ file directory. The command line will list your current directory. It should say ```~/FIELDAQ/Granusoft/src```
   If you just exited the granusoft software then you should already be in the correct directory.
   If you are not in the correct directory, type ```cd ~/FIELDAQ/Granusoft/src```
5. Type ```git pull``` into the command line. This will download the latest update onto your device.
6. The device is now updated! You can enter the updated software by either turning the device off and on again or running the command ```python3 main.py```
