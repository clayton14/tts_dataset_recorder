#!/usr/bin/env python3
import os
import speech_recognition as sr
import pyaudio
import wave
import time
import csv
import sounddevice as sd
from scipy.io.wavfile import write
import multiprocessing
import time
import os
import sys

#audip stuff
wav_iteration = 0  # num of recordings
sec_wav = 10            # duration the of each audio recoring in seconds
fs = 44100              # samplerate
FORMAT = pyaudio.paInt16
CHUNK = 1024
path = os.getcwd()

# make dir for the audio stuff

if not os.path.exists('wav'):
    os.makedirs('wav')

try:
    max_recordings = int(input("how many recordings do you want to make\n"))
except Exception as e:
    print("Sorry, you can only enter whole numbers\n")

#starts recording the audio in wav format
def record(wav_iteration):
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=2,
                        rate=fs, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(fs / CHUNK * sec_wav)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(str(path) + "/wav/" +
                         str(wav_iteration) + ".wav", 'wb')
    waveFile.setnchannels(2)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(fs)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


#converts wav to text and outputs to csv
def tts(wav_iteration):
    r = sr.Recognizer()
    with sr.AudioFile(str(path) + "/wav/" + str(wav_iteration) + ".wav") as source:
        audo_listener = r.listen(source)
        audio_recognizer = r.recognize_google(audo_listener, language='en-US')
        print(audio_recognizer)

        #csv stuff
    with open("dataset.csv", 'a',  newline='') as csvf:
        fieldnames = ['itration', 'wav', 'text']
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writerow({'itration': str(wav_iteration), 'wav': str(
            wav_iteration) + '.wav', 'text': str(audio_recognizer) + '\n'})

    if (os.path.exists(path + "/wav") and not os.listdir(path + "/wav") == 0):
        # print("resume recording")
        list = os.listdir("./wav")
        wav_iteration = len(list)
    else:
        print("no files found in dir ressume recording")


#main loop
count = 0
while True:
    if(count == max_recordings):
        break

    count += 1
    if (os.listdir(path + "/wav") != 0):
        list = os.listdir("./wav")
        wav_iteration = len(list)
    else:
        print("no files found in dir\nressume recording")
        break

    print("recording in")
    #countdown
    t = 3
    while t >= 1:
        print(t)
        time.sleep(1)
        t -= 1
    #starts recording
    record(wav_iteration)
    time.sleep(3)
    try:
        print("proccessing audio...")
        tts(wav_iteration)

    except AttributeError as ttsError:
        print("an error has occurred, processing audio again")
        tts(wav_iteration)

    except Exception as ttsError:
        print("an error has occurred, processing audio again")
        tts(wav_iteration)
