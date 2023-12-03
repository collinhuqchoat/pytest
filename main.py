import time
import pyttsx3

def say_phrase():
    engine = pyttsx3.init()

    phrase = "yor phrase"

    engine.say(phrase)
    engine.runAndWait()

if __name__ == "__main__":
    interval_seconds = 6000

    while True:
        time.sleep(interval_seconds)
        say_phrase()
