import subprocess 
import pyttsx3 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from urllib.request import urlopen 

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)  #voice id 0 for male


def speak(audio): 
    engine.say(audio) 
    engine.runAndWait()


  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Epax's AI 1 point o") 
    speak("I am your Assistant") 
    speak(assname) 


def usrname(): 
    speak("What should i call you sir") 
    uname = takeCommand() 
    speak("Welcome Mister") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("#####################".center(columns)) 
    print("Welcome Mr ", uname.center(columns)) 
    print("#####################".center(columns)) 


def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone(device_index= 0) as source: 
          
        print("Listening...") 
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to Recognizing your voice.")   
        return "None"
      
    return query 
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('YOUR EMAIL', 'PASSWORD') 
    server.sendmail('YOUR EMAIL', to, content) 
    server.close() 




clear = lambda: os.system('cls')
clear() 
wishMe()
usrname() 
 
f = True
while f:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "") 
        try :
            results = wikipedia.summary(query, sentences = 3) 

            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
        except :
            speak("No result found")
    elif 'open youtube' in query: 
        speak("Here you go to Youtube\n") 
        webbrowser.open("youtube.com") 
    elif 'open google' in query: 
        speak("Here you go to Google\n") 
        webbrowser.open("google.com") 
    elif 'shutdown' in query:
        speak("Ok BYE BYE")
        f = False
    elif 'the time' in query: 
        strTime = datetime.datetime.now().time()  
        l = str(strTime).split(':')

        speak(f"Sir, the time is {l[0]} hours and {l[1]}minutes") 
    elif 'email to swastik' in query: 
           try: 
               speak("What should I say?") 
               content = takeCommand() 
               to = "xxxxxxx@gmail.com"    
               sendEmail(to, content) 
               speak("Email has been sent !") 
           except Exception as e: 
               print(e) 
               speak("I am not able to send this email") 
    elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whome should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email")
    elif 'how are you' in query: 
            speak("I am bad ass fuck , haha just kidding i am not fine") 
            speak("How are you, Sir")    
    elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine")
    elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
    elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
    elif "what's your name" in query or "What is your name" in query: 
            speak("actually i dont have name , no one named me lol")
    elif "who made you" in query or "who created you" in query:  
            speak("I have been created by swasthik , also known as EPAX") 
    elif 'joke' in query or 'tell me a joke' in query: 
            speak(pyjokes.get_joke()) 
    elif 'search' in query : 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
    elif "who i am" in query: 
            speak("If you talk then definately your human.")
    
    elif "who are you" in query: 
        speak("I am your virtual assistant created by EPAX") 
    elif 'open spotify' in query: 
            speak("opening Spotify, play some music") 
            appli = r"C:\\Users\\swasthik\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(appli) 
    elif 'open discord' in query: 
            speak("opening Discord") 
            disco = r"C:\\Users\\swasthik\\AppData\\Local\\Discord\\Update.exe"
            os.startfile(disco) 
    elif "where is" in query: 
           query = query.replace("where is", "") 
           location = query 
           speak("User asked to Locate") 
           speak(location) 
           webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
    elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time") 
  
    elif "i love you" in query: 
            speak("It's hard to understand") 
    elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
    elif 'empty recycle bin' in query: 
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
        speak("Recycle Bin Recycled") 
    elif "weather" in query: 
            
        # use 'Open weather' API Key 
          
        api_key = "API-KEY OF OPEN WEATHER" 
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        speak(" City name ") 
        print("City name : ") 
        try:
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
            else:  
              speak(" City Not Found ")
        except :
            speak("try again")
        
        



  
    

  
