import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import pyjokes  # pip install pyjokes
import requests, json  #inbuilt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am desktop assistant , Please tell me how may I help you")
def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

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
def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "D:\\desktop assistant\\screenshot\\ss.png"
    )

#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


#weather condition
def weather():
    api_key = "e22fcbd36baffc5ba1b4b250e3e8e54a" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('virtualassistantmini@gmail.com', 'Desktop@123')
    server.sendmail('virtualassistantmini@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

# Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
#open youtube
        elif ('date' in query):
            date()
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
# open google
        elif 'open google' in query:
            webbrowser.open("google.com")
#open stackoverflow
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

# jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

# weather
        elif ("weather" in query or "temperature" in query):
            weather()
# sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t +1")
        elif ("switch off" in query or 'shutdown'in query):
            os.system("shutdown /r /t 1")
# reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("reminderlist.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

 # reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("reminderlist.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())


# searching on wikipedia

        elif ('search' in query or 'what' in query or 'who' in query or 'when' in query or 'where' in query):
            try:
                speak("searching...")
                query = query.replace("search", "")
                query = query.replace("what", "")
                query = query.replace("when", "")
                query = query.replace("where", "")
                query = query.replace("who", "")
                query = query.replace("is", "")
                result = wikipedia.summary(query, sentences=2)
                print(query)
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to find the query on wikipedia")
#music
        elif 'play music' in query or 'songs' in query or 'music' in query:
            music_dir = 'D:\\desktop assistant\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
            exit()
#time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
# email
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ashishyadav5012002@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")
#visual studio
        elif 'open code' in query:
            codePath = "C:\\Users\\ashis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
#screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")
# quit
        elif ('i am done' in query or 'bye' in query
                  or 'go offline' in query or 'goodbye' in query
                  or 'nothing' in query):
            wishme_end()


        else:
             speak(" i found something have a look")
             webbrowser.open(query)
             exit()


