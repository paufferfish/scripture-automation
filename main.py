import pyaudio

from vosk import Model, KaldiRecognizer

model = Model(r"C:\Users\okoti\Downloads\vosk-model-en-us-0.22-lgraph\vosk-model-en-us-0.22-lgraph")

recognizer = KaldiRecognizer(model, 1600)



