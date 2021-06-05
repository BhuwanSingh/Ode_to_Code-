import speech_recognition as sr
import librosa
import json
import base64
import soundfile as sf

import time
start_time = time.time()

input_data = open("input.json",)
input_data_dict = json.load(input_data)
to_match = input_data_dict["options"]

audio = input_data_dict["audio"]
wav_file = open("temp.wav", "wb")
decode_string = base64.b64decode(audio)
wav_file.write(decode_string)

x, _ = librosa.load('./temp.wav', sr=16000)
sf.write('tmp.wav', x, 16000)
# wave.open('tmp.wav','r')

filename = "tmp.wav"

a = []

r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    text = text.lower()
    a = list(text.split(" "))



# print(to_match)

b = []

for i in to_match:
    if i in a:
        b.append(i)

# print(b)

k = { "answers" : b}
print(k)

f = open("output.json", "w+")
# arr = a.split()
f.write(json.dumps(k))
f.close()

print(a)
print("--- %s seconds ---" % (time.time() - start_time))
