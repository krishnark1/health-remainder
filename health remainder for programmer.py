from pygame import mixer
from datetime import datetime
import time
print("      welcome to the healthy programmer      ")
# to set mp3 for water and calling it
def watermusic():
    mixer.music.load("One More Drink.mp3") #location of your mp3 song
    mixer.music.set_volume(.9)
    mixer.music.play(10)
def water():
    time.sleep(1200)
    watermusic()
# to set mp3 for eyes and calling it
def eyemusic():
    mixer.music.load("Take The Message.mp3")
    mixer.music.set_volume(.9)
    mixer.music.play(10)
def eye():
    time.sleep(600)
    eyemusic()
# to set mp3 for phyiscal activity and calling it
def physicalactivitymusic():
    mixer.music.load("Wake up.mp3")
    mixer.music.set_volume(.9)
    mixer.music.play(10)
def physicalactivity():
    time.sleep(900)
    physicalactivitymusic()
# to stop the function and creating the file in the system
def stopwatermusic():
    print("drink some water")
    n = input("type drank to stop")
    if n == "drank":
        mixer.music.stop()
    with open("report.txt", "a") as f:
        f.write(str(datetime.now()) + " drank water \n")
def stopeyemusic():
    print("please do some eye execrise ")
    n = input("type eydone to stop")
    if n == "eydone":
        mixer.music.stop()
    with open("report.txt", "a") as f:
        f.write(str(datetime.now()) + " did eye execrise ")
def stopphysicalactivitymusic():
    print("please do some physical execrise ")
    n = input("type exdone to stop")
    if n == "exdone":
        mixer.music.stop()
    with open("report.txt", "a") as f:
        f.write(str(datetime.now()) + " did physical execrise \n")
while True:
    mixer.init()
    #to set the particular timing in remainder uncomment the bellow code 
    """moringtime = "09:00:00"
    eveningtime = "19:00:00"
    now = datetime.now()
    currenttime = now.strftime("%H:%M:%S")
    if currenttime <= moringtime and currenttime >= eveningtime:
        break"""
    water()
    stopwatermusic()
    eye()
    stopeyemusic()
    physicalactivity()
    stopphysicalactivitymusic()
