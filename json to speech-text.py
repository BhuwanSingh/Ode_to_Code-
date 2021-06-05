
import pyttsx3
import speech_recognition as sr
import json
import base64
import fs
import wavio



# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech

encode_string = open("audio.wav", "rb").read()
wav_file = open("temp.wav", "wb")
decode_string = base64.b64decode(encode_string)
wav_file.write(decode_string)
filename='temp.wav'

wavio.write(filename, temp.wav, fs ,sampwidth=2)
#def SpeakText(command):
    # Initialize the engine
 #   engine = pyttsx3.init()
  #  engine.say(command)
   # engine.runAndWait()


# Loop infinitely for user to
# speak

while(1):

    # Exception handling to handle
    # exceptions at the runtime
    try:
            with sr.AudioFile(filename) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audio_data)
                print(text)


                text = text.lower()
                f=open("output.txt","w+")
                arr = text.split()
                f.write(json.dumps(arr))
                f.close()

                print("Did you say " + text)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
