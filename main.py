import pyaudio

from vosk import Model, KaldiRecognizer

model = Model(r"C:\Users\okoti\Downloads\vosk-model-en-us-0.22-lgraph\vosk-model-en-us-0.22-lgraph")

recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()

init_mic = mic.open(channels=1, frames_per_buffer=8192, rate=16000, input=True, format=pyaudio.paInt16)

init_mic.start_stream()

while True:
    data = init_mic.read(8192)
    if recognizer.AcceptWaveform(data):
        new_data = recognizer.Result()
        print(new_data)


















