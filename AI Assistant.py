import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit
import os
import smtplib
import pyautogui
import keyboard
import pyjokes
import requests
from bs4 import BeautifulSoup 
from PyDictionary import PyDictionary as Diction

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)


def speak(audio):
    # print("   ")
    engine.say(audio)
    print(f":{audio}")
    # print("    ")
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!,Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!,Sir")   

    else:
        speak("Good Evening!,Sir")  

    # speak("I am Jarvis Sir. Please tell me how may I help you")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def send_email(to,content):
    sender_email="tiwariaakash673@gmail.com"
    password="jyhxsjqshjdbarce"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    # message=f'Subject:{subject}\n\n{content}'
    server.sendmail(sender_email, to, content)
    server.close()


def song():
    speak("Tell Me The Name Of The Song")
    songname=takeCommand()

    if 'akeli' in songname:
        os.startfile('D:\\Songs\\akeli.mp3')
    
    elif 'senorita' in songname:
        os.startfile('D:\\Songs\\senorita.mp3')

    else:    
       pywhatkit.playonyt(songname)

    speak("Your Song Has Been Started! , Enjoy Sir!")


def openapps():
    speak("hi Sir , Wait A Second")


    if 'vs code' in query:
        codePath = "C:\\Users\\dell\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)  

    elif 'telegram' in query:
        codePath="C:\\Users\\dell\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
        os.startfile(codePath)

    elif 'chrome' in query:
        codePath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)

    elif 'facebook' in query:
        webbrowser.open("https://www.facebook.com/")

    elif 'google' in query:
        webbrowser.open("https://www.google.com/")    
    
    elif 'instagram' in query:
        webbrowser.open("https://www.instagram.com/") 

    elif 'youtube' in query:
        webbrowser.open("https://www.youtube.com/") 

    elif 'maps' in query:
            webbrowser.open("https://maps.google.com/")

    elif 'open gmail' in query:
            webbrowser.open("https://www.google.com/gmail/") 
     
    speak("Done Sir!")


def closeapps():
       speak("Ok Sir , Wait A Second")

       if 'chrome' in query :
           os.system("TASKKILL /F /im chrome.exe")
 
       elif 'telegram' in query:
           os.system("TASKKILL /F /im Telegram.exe")

       elif 'vs code' in query:
           os.system("TASKKILL /F /im Code.exe")

       elif 'youtube' in query:
           os.system("TASKKILL /F /im chrome.exe")

       elif 'instagram' in query:
           os.system("TASKKILL /F /im chrome.exe")

       elif 'maps' in query:
           os.system("TASKKILL /F /im chrome.exe")

       elif 'facebook' in query:
           os.system("TASKKILL /F /im chrome.exe")
    
       elif 'google' in query:
           os.system("TASKKILL /F /im chrome.exe")

def Temp():
    speak("Which city OF Temperature You Want")
    city=takeCommand()
    search="temperature in" + city
    # print(search)
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temperature=data.find ("div",class_= "BNeawe").text
    speak(f"The Temperature is {temperature} celcius")


def YoutubeAuto():
    speak("What's Your Command")
    comm=takeCommand()

    if 'pause' in comm:
        keyboard.press('k')

    elif 'restart' in comm:
        keyboard.press('0')
    
    elif 'mute ' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('l')
    
    elif 'back' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        keyboard.press('f')

    elif 'full mode' in comm:
        keyboard.press('t')

    elif 'next video' in query:
            keyboard.press('Shift+N')
        
    elif 'previous video' in query:
            keyboard.press('Shift+P')

    elif 'miniplayer' in query:
            keyboard.press('i')
        
    elif 'search box' in query:
            keyboard.press('/')

    elif 'increase speed' in query:
            keyboard.press('>')

    elif 'decrease speed' in query:
            keyboard.press('<')

    speak("Done Sir!")

def ChromeAuto():
    speak("Chrome Automation Started")

    command=takeCommand()

    if 'close the tab' in command:
        keyboard.press_and_release('ctrl+w')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl+t')

    elif 'open new window' in command:
        keyboard.press_and_release('ctrl+n')

    elif 'history' in command:
        keyboard.press_and_release('ctrl+h')

def screenshot():
    speak("OK Boss , What Should I Name The File ?")
    path=takeCommand()
    path1name=path+ ".png"
    path1="C:\\Users\\dell\\Pictures\\Saved Pictures\\"+ path1name
    kk=pyautogui.screenshot()
    kk.save(path1)
    os.startfile("C:\\Users\\dell\\Pictures\\Saved Pictures")
    speak("Here Is Your ScreenShot")


def Dict():
    speak("Activated Dictionary")
    speak("Tell Me The Problem")
    prob1=takeCommand()

    if 'meaning' in prob1:
        prob1=prob1.replace("what is the","")
        prob1=prob1.replace("jarvis","")
        prob1=prob1.replace("of","")
        prob1=prob1.replace("meaning of","")
        result=Diction.meaning(prob1)
        speak(f"The Meaning of {prob1} is  {result}")


    elif 'synonym' in prob1:
        prob1=prob1.replace("what is the","")
        prob1=prob1.replace("jarvis","")
        prob1=prob1.replace("of","")
        prob1=prob1.replace("synonym of","")
        result=Diction.synonym(prob1)
        speak(f"The Synonym of {prob1} is  {result}")    

    elif 'antonym' in prob1:
        prob1=prob1.replace("what is the","")
        prob1=prob1.replace("jarvis","")
        prob1=prob1.replace("of","")
        prob1=prob1.replace("antonym of","")
        result=Diction.antonym(prob1)
        speak(f"The Antonym of {prob1} is  {result}")
     
    speak("Exited Dictionary!")




if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'hello' in query:
            speak("Hello Sir,I Am Jarvis ")
            speak("Your Personal AI Assistant")
            speak("How May I Help You")
          
        elif 'how are you' in query:
            speak("I Am Fine Sir")
            speak("What About You")

        elif 'you need a break' in query:
            speak("Ok Sir , You Can Call Me Anytime , By Sir")
            break

        elif 'exit' in query:
            speak("Ok Sir,Bye")
            break

        elif 'youtube search' in query:
            speak("Ok Sir , This Is What I found For Your Search!")
            query=query.replace("jarvis","")
            query=query.replace("youtube search","")
            # query=query.replace("and search","")

            web='https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            speak("Done Sir")


        elif 'google search' in query:      
            speak("Ok Sir , This Is What I found For Your Search!")
            query=query.replace("jarvis","")
            query=query.replace("google search","")
            # query=query.replace("and search","")

            pywhatkit.search(query)
            speak("Done Sir!")
        
        
        elif 'open website' in query:
            speak("Tell Me The Name Of The Website")
            name=takeCommand()
            web='https://www.' + name + '.com'
            result=webbrowser.open(web)
            print(result)
            speak("Done Sir!")

        elif 'song' in query:
            song()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("jarvis", "")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'screenshot' in query:
            screenshot()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'send email' in query:
           try:
                speak("What should I say?")
                content = takeCommand()
                to = "tiwariaakash569@gmail.com"
                send_email(to,content)
                speak("Email has been sent!")
           except Exception as e:
                print(e)
                speak("Sorry , there being an error to send email")    


 
        elif 'open telegram' in query:
            openapps()

        elif 'open vs code' in query:
            openapps()
          
        elif 'open maps' in query:
            openapps()

        elif 'open facebook' in query:
            openapps()

        elif 'open instagram' in query:
            openapps()

        elif 'open youtube' in query:
            openapps()

        elif 'open google' in query:
            openapps()

        elif 'open gmail' in query:
            openapps()    

        elif 'open chrome' in query:
            openapps()     


        elif 'close chrome' in query:
            closeapps()  

        elif 'close telegram' in query:
            closeapps() 
            
        elif 'close vs code' in query:
            closeapps() 

        elif 'close maps' in query:
            closeapps() 
        
        elif 'close youtube' in query:
            closeapps() 
        
        elif 'close google' in query:
            closeapps() 
        
        elif 'close facebook' in query:
            closeapps() 
        
        elif 'close gmail' in query:
            closeapps() 

        

        elif 'pause' in query:
          keyboard.press('k')

        elif 'restart' in query:
          keyboard.press('0')
    
        elif 'mute' in query:  
           keyboard.press('m')

        elif 'skip' in query:
          keyboard.press('l')
    
        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'full mode' in query:
           keyboard.press('t')

        elif 'next video' in query:
            keyboard.press('Shift+N')
        
        elif 'previous video' in query:
            keyboard.press('Shift+P')

        elif 'miniplayer' in query:
            keyboard.press('i')
        
        elif 'search box' in query:
            keyboard.press('/')

        elif 'increase speed' in query:
            keyboard.press('>')

        elif 'decrease speed' in query:
            keyboard.press('<')
        
       
        elif 'youtube automation' in query:
            YoutubeAuto()


        elif 'close the tab' in query:
           keyboard.press_and_release('ctrl+w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl+t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl+n')

        elif 'history' in query:
           keyboard.press_and_release('ctrl+h')


        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_jokes()
            speak(get)

        elif 'repeat my word' in query:
            speak("Speak Sir!")
            jj=takeCommand()
            speak(f"You Said:{jj}")


        elif 'my location' in query:
            webbrowser.open('https://goo.gl/maps/PMD5FVtQZ3zXKu1h7')

        
        elif 'dictionary' in query:
            Dict()
        
        elif 'temperature' in query:
            Temp()