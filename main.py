import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import google.generativeai as genai

recognizer = sr.Recognizer()


def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# integration with AI
def aiprocess(c):

    genai.configure(api_key="AIzaSyBbK-9XaFslJtzvdmcS2iJja-45jIhf1RE")

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction="You are a friendly and helpful assistant named jarvis that provides concise answers and do not use * in text")

    response = model.generate_content(c)
    return(response.text)


def processcommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif command.lower().startswith("play"):
        s = command.lower().split("play ")[1]
        # song = " ".join(s)
        link = music_library.music[s]
        webbrowser.open(link)
    else:
        output=aiprocess(command)
        speak(output)




if __name__=="__main__":
    speak("Intializing Jarvis......")
    while True:
        # listen for word Jarivis
        r = sr.Recognizer()
       # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source,timeout=3,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("hello sir, how can i help you")

                # listen for command
                with sr.Microphone() as source:
                    print("jarvis ACTIVE .....")
                    audio = r.listen(source,timeout=3)
                    command = r.recognize_google(audio)
                    print(command)
                    processcommand(command)

        except sr.UnknownValueError:
            print("google could not understand audio")
        except sr.RequestError as e:
            print("error; {0}".format(e))
