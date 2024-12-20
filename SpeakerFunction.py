from playsound import playsound
from gtts import gTTS
import os

def speak(Context="Space", save_file = False, save_file_name = "SpeakerFunction", slow_bool = False):

    language = "en" #You can easily change the language from here, example: "tr", "en", "fr"

    if save_file == False:
        speaker = gTTS(text=Context, lang=language, slow=slow_bool)
        file = "SpeakerFunction.mp3"
        speaker.save(file)
        playsound(file)
        os.remove(file)
    if save_file == True:
        save_file_names = f"{save_file_name}.mp3"

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        now_speak = os.path.join(desktop_path, save_file_names)
        speaker = gTTS(text=Context, lang=language, slow=slow_bool)

        speaker.save(now_speak)
        playsound(now_speak)

speak(Context="Hello World!", save_file=False, slow_bool=False)
