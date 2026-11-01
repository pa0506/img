import speech_recognition as sr
import wave

r = sr.Recognizer()

with wave.open("audio1.wav", "rb") as f:
    duration = f.getnframes() / f.getframerate()

with sr.AudioFile("audio1.wav") as source:
    audio = r.record(source)

print("Audio Duration:", round(duration, 2), "seconds")

try:
    text = r.recognize_google(audio)
    print("Recognized Speech:", text)

except:
    print("Speech not recognized")
