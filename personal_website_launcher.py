#firstly we need our imports to allow us to do the things we need it to do!
import datetime
import webbrowser
from win10toast import ToastNotifier
import os #we will need this to launch our d/a 
import subprocess #launch d/a
import sys

#create website launcher notifiers from win10toast library
youtube_ToastNotification = ToastNotifier()
google_ToastNotification = ToastNotifier()
facebook_ToastNotification = ToastNotifier()

#will also be adding desktop application launcher alongside this as a different selection to website launcher
DISCORD_PATH = ".." #add the path here soon
STEAM_PATH = ".."  #also add path here
CHROME_PATH = ".." #add chrome path
BRAVE_PATH = ".." #add brave browser path

#get input from user through prompt
select_lancher = input("d for DESKTOP APPLICATIONS or w for WEBSITES")
# if lowercase w or uppercase W is selected...
if select_lancher == 'w' or select_lancher == 'W':
    #we allow the user to only launch websites
   launcher_selectInput = input("1 for YouTube \n 2 for Google \n 3 for FaceBook")
   if launcher_selectInput == '1':
       #user enters 1 - show windows notification on their Desktop
        youtube_ToastNotification.show_toast("Opening YouTube", f"{launcher_selectInput} YouTube Selected - Opening YouTube")
        #open youtube on browser
        webbrowser.open("http://www.youtube.com")
        #if input is 2
   elif launcher_selectInput == '2':
       #open google - show desktop notification
        google_ToastNotification.show_toast("Opening Google", f"{launcher_selectInput} Google Selected - Opening Google")
        #open Google on their browser
        webbrowser.open("http://www.google.com")
        #if 3 is entered
   elif launcher_selectInput == '3':
       #show desktop notification that facebook will be open - and that, that is their input of choice
        facebook_ToastNotification.show_toast("Opening FaceBook", f"{launcher_selectInput} FaceBook Selected - Opening FaceBook")    
        #open FaceBook on their browser
        webbrowser.open("http://www.facebook.com")
        #in the case that lowercase q or uppercase Q are entered, quit the program.
   elif launcher_selectInput == 'q' or launcher_selectInput == 'Q':
       #show this print message, then exit.
       print("closing")
       exit
 #in the case that the user selects lowercase d or uppercase D, allow them to open desktop applications.      
if select_lancher == 'd' or select_lancher == 'D':
    desktop_select = input("1 for discord \n 2 for Steam \n 3 for Chome \n 4 for Brave")
    #if 1 is selected, show message that discord will open.
    if desktop_select == '1':
     print("this is meant to open Discord")
    elif desktop_select == '2':
        #if 2 is entered - show that steam is meant to open.
        print("this is meant to open Steam") 
    elif desktop_select == '3':
        #if 3 is entered show that chrome is meant to be opened
        print("This is meant to open Chrome")
    elif desktop_select == '4':
        #if 4 is entered - show that Brave browser is meant to be opened
        print("this is meant to open Brave")         
    elif desktop_select == 'qd' or desktop_select == 'QD':
        #if lowercase and uppercase qd are entered meaning quick desktop application
        print("closing")
        #show closing message and exit program.
        exit








