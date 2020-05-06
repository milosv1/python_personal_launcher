#firstly we need our imports to allow us to do the things we need it to do!
import datetime
import webbrowser
from win10toast import ToastNotifier

#create website launcher notifiers from win10toast library
youtube_ToastNotification = ToastNotifier()
google_ToastNotification = ToastNotifier()

#get input from user through prompt
website_selectInput = input("1 for YouTube \n 2 for Google")

if website_selectInput == '1':
    youtube_ToastNotification.show_toast("Opening YouTube", f"{website_selectInput} YouTube Selected - Opening YouTube")
    webbrowser.open("http://www.youtube.com")
elif website_selectInput == '2':
    google_ToastNotification.show_toast("Opening Google",f"{website_selectInput} Google selected - Opening Google")   
    webbrowser.open("http://www.google.com")
else:
    print("input can only be 1 OR 2")     