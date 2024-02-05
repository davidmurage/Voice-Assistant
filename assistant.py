import speech_recognition as sr
from gtts import gTTS
import winsound
from pydub import AudioSegment
import pyautogui
import webbrowser

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    winsound.PlaySound("response.wav", winsound.SND_FILENAME)
    # os.system("afplay response.mp3") for non-windows

tasks = []
listeningToTask = False

def main():
    global tasks
    global listeningToTask
    respond("Hello, david. I hope you're having a nice day today.")
    while True:
        command = listen_for_command()

        
        if command:
            if listeningToTask:
                tasks.append(command)
                listeningToTask = False
                respond("Adding " + command + " to your task list. You have " + str(len(tasks)) + " currently in your list.")
            elif "add a task" in command:
                listeningToTask = True
                respond("Sure, what is the task?")
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "take a screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("I took a screenshot for you.")
            elif "open chrome" in command:
                respond("Opening Chrome.")
                webbrowser.open("http://www.youtube.com/")
            elif "open google map" in command:
                respond("opening google map")
                webbrowser.open("https://www.google.com/maps")  
                
            elif "open youtube" in command:
                respond("opening youtube")
                webbrowser.open("https://www.youtube.com/")  
                
            elif "open whatsapp web" in command:
                respond("opening whatsapp web")
                webbrowser.open('https://web.whatsapp.com/') 
                 
            elif "Open kilimall" in command:
                respond("Opening kilimall")
                webbrowser.open("https://www.kilimall.co.ke/new/flash-sales?gad_source=1&gclid=CjwKCAiAiP2tBhBXEiwACslfnj-UTlgwUMdATQXBZldKYAAuPgHYYAe_5XD5tCPoDfJYcgbaw6XKWxoC4yUQAvD_BwE")      
                  
            elif "exit" in command:
                respond("Goodbye!")
                break
            else:
                respond("Sorry, I'm not sure how to handle that command.")

if __name__ == "__main__":
     #print(listen_for_command())
    respond("This has been building a virtual assistant with Python")
    main()