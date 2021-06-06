import speech_recognition as sr
import librosa
import json
import base64
import soundfile as sf
from datetime import datetime
import re

import time
start_time = time.time()

input_data = open("input.json",)
input_data_dict = json.load(input_data)
# to_match = input_data_dict["options"]
if "options" in input_data_dict:
    to_match = input_data_dict["options"]
else:
    exit()

audio = input_data_dict["audio"]
question = input_data_dict['question_key']
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
if question == 'q1':
    for i in to_match:
        if i in a:
            b.append(i)
    k = { "answers" : b}
    f = open("output.json", "w+")
    # arr = a.split()
    f.write(json.dumps(k))
    f.close()


# if question == 'q2':
#     num = int(audio.split("lakh")[0])

# limits = []

# limits.append(int(options[0].split("<")[1].split("lakh")[0]))


# for i in range(1,len(options)-1):
#     num = int(audio.split("lakh")[0])

#     limits = []

#     limits.append(int(options[0].split("<")[1].split("lakh")[0]))


#     for i in range(1,len(options)-1):
#         check = options[i].split("-")
#         upper = int(check[1].split("lakh")[0])
#         limits.append(int(upper))

#     pos=-1

#     for i in range(0,len(options)-1):
#         if num <= limits[i]:
#             pos=i
#             break

# if pos is -1:
#     print( options[len(options)-1])
# else:
#     print(options[pos])


if question == 'q3':
    listToStr = ' '.join(map(str, a))
    date_time_obj = datetime.strptime(listToStr, '%d/%m/%y %H:%M:%S')
    # b.append[date_time_obj]
    k = { "answers" : date_time_obj}
    f = open("output.json", "w+")
    # arr = a.split()
    f.write(json.dumps(k))
    f.close()


# print(b)



print(a)
print("--- %s seconds ---" % (time.time() - start_time))
