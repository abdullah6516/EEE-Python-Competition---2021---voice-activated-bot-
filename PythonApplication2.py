import  pyttsx3   #pip install  pyttsx3 
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser as wb
import pyjokes #pip install pyjokes 
import os
import time


 


engine = pyttsx3.init()

def speak(audio):
     engine.say(audio)
     engine.runAndWait()


def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #%I for 12 hours %H for 24 hours
    speak("The current time is")
    speak(Time)


def date_():
    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    day= datetime.datetime.now().day
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)




def wishme():
    speak("welcome back")
     
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<24:
        speak("Good evening")
    else:
         speak("Good night sir")
    speak("How can I help you today ? ")









def Takecommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
         print("listening.......")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
        print("Recognizing........")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please........")
        return "None"
    return query









def joke():speak(pyjokes.get_joke())












if  __name__ =="__main__":
    wishme()

    while True:

        query=Takecommand().lower()
        if 'time' in query:
         time_()
        elif 'date' in query:
         date_()



        elif 'wikipedia'  in query:      #you have to say  wikipedia then what you want to search for 
            speak("Searching")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)





        elif 'chrome' in query:
            speak("what website do you want me to search for?")
            chromepath = ' c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s '
            search=Takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') 





        elif 'youtube' in query:
            speak("what do you want me to search for?")
            search_youtube=Takecommand().lower()
            speak("searching")
            wb.open('https://www.youtube.com/results?search_query='+search_youtube)








        elif'google' in query:
            speak("what do you want me to search for?")
            search_google=Takecommand().lower()
            speak("searching")
            wb.open('https://www.google.com/search?q='+search_google)






        elif  'something funny' in query:
            joke()






        elif  "what's your name" in query:
            speak("I do not have a name i'm just piece of code")

        elif 'how are you' in query:
            speak("i'm fine thanks for asking")





        
       
        elif 'microsoft powerpoint' in query:                  
            speak("opening")
            point=r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE' #your  program location  location might be different  
            os.startfile(point)

        elif 'microsoft word' in query:
            speak("opening")
            word=r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE' #your  program location  location might be different  
            os.startfile(word)

        elif 'adobe acrobat' in query:
            speak("opening")
            adobe=r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.EXE'   #your  program location  location might be different  
            os.startfile(adobe)





  
        elif 'take a note' in query:
             speak('I am raedy to take notes')
             notes = Takecommand()
             file =open('notes.txt','w')
             speak('whould you like me to include date and time')
             answer=Takecommand()
             if 'yes' or 'sure' in answer:
                 strtime=datetime.datetime.now().strftime("%H:%M:%S")
                 file.write(strtime)
                 file.write(':-')
                 file.write(notes)
                 speak('notes are saved')
             else:
                     file.write(notes)




        elif 'show notes' in query:
            speak("On it")
            file=open('notes.txt','r')
            print(file.read())




        
        elif 'restart' in query :
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query :
            os.system("shutdown /s /t 1")       
