from gtts import gTTS
from os import listdir
from threading import Thread
from playsound import playsound

__author__ = "Nadav Shani"

language = 'en'  # language to speak
sound_files = listdir("textToSpeechFolder")  # folder with the existing files


######################################
# does: speak sentences in order     #
######################################
class Speak:
    speak = True  # on exit it will be false

    def __init__(self):
        self.num = 0  # make order
        self.ind = 0

    ###################################################
    # does: check text validation and play the file   #
    ###################################################
    def say(self, my_num, *text):
        text = ''.join(text).replace(' ', '').replace(':', '')
        # if it's a question or if there isn't a text
        if '?' in text or not text:
            print("couldn't find text")
            self.num += 1
            return

        name_to_save = "textToSpeechFolder/" + text + ".mp3"
        if (text + ".mp3") not in sound_files:  # if the file doesn't exist
            print(f"not here- {text}")
            output = gTTS(text=text, lang=language)
            output.save(name_to_save)
            sound_files.append(text + '.mp3')

        # wait until it's the file's turn
        while self.num < my_num:
            pass

        if self.speak:
            playsound(name_to_save)  # play the file
        self.num += 1

    ############################################
    # does: start threading for say function   #
    ############################################
    def start_say(self, text):
        func = Thread(target=self.say, args=(self.ind, text))
        func.start()
        self.ind += 1
