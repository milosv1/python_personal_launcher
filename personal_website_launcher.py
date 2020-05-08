#firstly we need our imports to allow us to do the things we need it to do!
import datetime
import webbrowser
from win10toast import ToastNotifier
import os #we will need this to launch our d/a 

#create website launcher notifiers from win10toast library
youtube_ToastNotification = ToastNotifier()
google_ToastNotification = ToastNotifier()
facebook_ToastNotification = ToastNotifier()

#will also be adding desktop application launcher alongside this as a different selection to website launcher
DISCORD_PATH = ".." #add the path here soon
STEAM_PATH = ".."  #also add path here
CHROME_PATH = ".." #add chrome
BRAVE_PATH = ".." #add brave browser path

#get input from user through prompt
website_selectInput = input("1 for YouTube \n 2 for Google \n 3 for FaceBook")

#if the user enters 1
if website_selectInput == '1':
    #show desktop notification - of said opening website
    youtube_ToastNotification.show_toast("Opening YouTube", f"{website_selectInput} YouTube Selected - Opening YouTube")
    #using webbrowser library open selected webbrowser
    webbrowser.open("http://www.youtube.com")
#else if user inputs 2    
elif website_selectInput == '2':
    #notify the user using the show_toast from import ToastNotifier of said opening website
    google_ToastNotification.show_toast("Opening Google",f"{website_selectInput} Google selected - Opening Google")   
    #open using webbrowser.open() ..
    webbrowser.open("http://www.google.com")
    #else if user inputs anything else - show they can only use 1 or 2
elif website_selectInput == '3':
    #notify User of selection    
    facebook_ToastNotification.show_toast("Opening FaceBook", f"{website_selectInput} FaceBook Selected - Opening FaceBook")
    #open facebook website
    webbrowser.open("http://www.facebook.com")
elif website_selectInput == 'q' or website_selectInput == 'Q':
    #if input is lowercase q or uppercase q - quite the launcher
     print("Quitting Launcher")
     exit    
else:
    print("input can only be 1 OR 2 OR 3")     