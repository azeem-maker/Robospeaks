import os
import win32com.client as wincom
if __name__ == '__main__':
    print("Welcome")

while True:
    speak = wincom.Dispatch("SAPI.SpVoice")
    x = input("type what you want to listen:")
    if x == "q":
        speak.Speak("bye bye friends")
        break
    speak.Speak(x)








