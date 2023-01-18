import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime
import pyaudio
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
from mpg123 import Mpg123, Out123
import os
import time

r = sr.Recognizer()
with sr.Microphone() as source:
	sound = AudioSegment.from_wav('MUSIC_POP.wav')
	start = AudioSegment.from_wav('Start.wav')
	play(start)
	play(sound)
	audio = r.record(source, duration=3)
	play(sound)
	try:
		text = r.recognize_google(audio, language="th")
		print(text)
		if "1" or "ภาษาไทย" in text:
			text = "เข้าสู่โหมดภาษาไทยครับ"
		#if "2" or "ภาษาอังกฤษ" in text:
			#text = "เข้าสู่โหมดภาษาอังกฤษครับ"
		else:
			#text = "ขอโทษครับsoftwareอยู่ในช่วงพัฒนาครับ"
			text = "เข้าสู่โหมดภาษาอังกฤษครับ"

	except:
		text = "ขอโทษครับsoftwareอยู่ในช่วงพัฒนาครับ"
	print(text)
	tts = gTTS(text, lang="th")
	tts.save('1.mp3')
	os.system("start 1.mp3")
	time.sleep(12)
	print(text)






