from recognition import Ears
from voice import voice
from commands import Command
import time


listener = Ears()
text_gen = listener.listen()
voice.text_to_speech('Привет! Я Лосяш!')
for text in text_gen:
    print(text)
    listener.stream.stop_stream()
    Command(text)
    time.sleep(0.5)
    listener.stream.start_stream()
