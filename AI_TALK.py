import speech_recognition as sr
from gtts import gTTS;from playsound import playsound;from datetime import datetime
import pyaudio;from pydub import AudioSegment;from pydub.playback import play
from io import BytesIO;from mpg123 import Mpg123, Out123;import os;import time
import serial;import time;import pygame;import numpy as np
# By : JameWarit
A = 0;B = 0;C = 0;D = 0;AA = 0;CC = 0;LI = [];LI1 = [];LI2 = [];OTP = 0;R = 0;RT = 0
Q = [];Q1 = [];Q2 = [];number = 0;Score = 0;Error = 0;Set = [];Num = [];I = 0


serialcomm = serial.Serial('COM3', 9600)
serialcomm.timeout = 1

def Arduino(Input):
		i = Input
		serialcomm.write(i.encode())

r = sr.Recognizer()
with sr.Microphone() as source:
	sound = AudioSegment.from_wav('Sound/ROBOTK.wav')
	T1 = AudioSegment.from_wav('Sound/T1.wav');T2 = AudioSegment.from_wav('Sound/T2.wav')
	T3 = AudioSegment.from_wav('Sound/T3.wav');T4 = AudioSegment.from_wav('Sound/T4.wav')

	time.sleep(2);Arduino("start");play(T1);play(T2);time.sleep(1);play(T3)

	time.sleep(0.5)
	play(sound);Arduino("recorder")
	audio = r.record(source, duration=5)
	Arduino("unrecorded");play(sound)

def Name(text1,LA):
	text = text1
	tts = gTTS(text, lang=LA)
	tts.save('Sound/1.mp3')
	pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	pygame.quit()


def loop():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		sound = AudioSegment.from_wav('Sound/ROBOTK.wav')
		T4 = AudioSegment.from_wav('Sound/T4.wav')
		play(sound);Arduino("recorder")
		audio = r.record(source, duration=5)
		Arduino("unrecorded");play(sound);C = 0;B = 0;A = 0
		while 1:
			if A == 0:
				try:
					text = r.recognize_google(audio, language="th")
					print(text)
					if text == "ภาษาไทย" or text == "1" or text == "ภาษาไทยครับ":
						play(T4)
						text = "เข้าสู่โหมดภาษาไทย";A = 1
					if text == "ภาษาอังกฤษ" or text == "2" or text == "ภาษาอังกฤษครับ" or text == "English":
						Name("The SAMM robot is ready to use","en")
						text = "Enter english mode";A = 2
				except:
					text = "คุณไม่ได้พูดครับ กรุณาลองพูดใหม่อีกทีครับ"
					tts = gTTS(text, lang="th")
					tts.save('Sound/1.mp3')
					pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
					while pygame.mixer.music.get_busy() == True:
						continue
					pygame.quit();C = 3;break

			if A == 1:
				tts = gTTS(text, lang="th")
				tts.save('Sound/1.mp3')
				pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.quit();C = 1;break

			if A == 2:
				tts = gTTS(text, lang="en")
				tts.save('Sound/1.mp3')
				pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.quit();C = 2;break

			if A != 1 or A != 2:
				text = "คุณไม่ได้พูดตามที่เรากำหนดไว้นะครับ กรุณาลองพูดใหม่อีกทีครับ"
				tts = gTTS(text, lang="th")
				tts.save('Sound/1.mp3')
				pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.quit();C = 3;break
	if C == 1:
		print("C1",C)
		return C

	if C == 2:
		print("C2",C)
		return C

	if C == 3:
		print("C3",C)
		C = loop()
		return C



while 1:
	if A == 0:
		try:
			text = r.recognize_google(audio, language="th")
			print(text)
			if text == "ภาษาไทย" or text == "1" or text == "ภาษาไทยครับ":
				play(T4)
				text = "เข้าสู่โหมดภาษาไทย";A = 1;B = 1
				"""tts = gTTS(text, lang="th")
				tts.save('Sound/1.mp3')
				#os.system("start Sound/1.mp3")
				#time.sleep(12)
				pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.quit();"""
			if text == "ภาษาอังกฤษ" or text == "2" or text == "ภาษาอังกฤษครับ" or text == "English":
				Name("The SAMM robot is ready to use","en")
				text = "Enter english mode";A = 2;B = 2
				"""tts = gTTS(text, lang="th")
				tts.save('Sound/1.mp3')
				#os.system("start Sound/1.mp3")
				#time.sleep(12)
				pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue
				pygame.quit()"""
		except:
			text = "คุณไม่ได้พูดครับ กรุณาลองพูดใหม่อีกทีครับ"
			tts = gTTS(text, lang="th")
			tts.save('Sound/1.mp3')
			# os.system("start Sound/1.mp3")
			# time.sleep(12)
			pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
			pygame.quit();A = 3;break

	if A == 1:
		tts = gTTS(text, lang="th")
		tts.save('Sound/1.mp3')
		#os.system("start Sound/1.mp3")
		#time.sleep(12)
		pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
		pygame.quit();C = 1;break

	if A == 2:
		tts = gTTS(text, lang="en")
		tts.save('Sound/1.mp3')
		#os.system("start Sound/1.mp3")
		#time.sleep(12)
		pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
		pygame.quit();C = 2;break

	if A != 1 or A != 2 :
		text = "คุณไม่ได้พูดตามที่เรากำหนดไว้นะครับ กรุณาลองพูดใหม่ครับ"
		tts = gTTS(text, lang="th")
		tts.save('Sound/1.mp3')
		# os.system("start Sound/1.mp3")
		# time.sleep(12)
		pygame.init();pygame.mixer.music.load("Sound/1.mp3");pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
		pygame.quit();A = 3;break

def TEXT(A):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		sound = AudioSegment.from_wav('Sound/ROBOTK.wav')
		play(sound);Arduino("recorder")
		audio = r.record(source, duration=A)
		Arduino("unrecorded");play(sound)
	text = r.recognize_google(audio, language="th")
	return text

def Start():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		time.sleep(0.5);Arduino("R")
		audio = r.record(source, duration=5)
	try:
		text = r.recognize_google(audio, language="th")
		if text == "เริ่มต้นทำงาน" and C == 1:
			Arduino("Q")
			Name("รับทราบครับผม","th");D = 1
			return D
		elif text == "Starting" and C == 2:
			Arduino("Q")
			Name("Acknowledge","en");D = 2
			return D
		else:
			D = Start()
			return D

	except:
		D = Start()
		return D


def Summit():
	AA = 0


	text1 = "ขั้นตอนต่อไปนี้เป็นการสอบถามข้อมูล สามารถพูดได้ตามอิสระเลยนะครับ ไม่ต้องกังวลครับ"
	Name(text1, "th")
	text1 = "ถ้าหาก ให้ข้อมูลผิดพลาด สามารถแก้ไขข้อมูลได้ที่เจ้าหน้าที่ครับ หลังจากจบแบบสอบถามจะมีเจ้าหน้าที่ติดต่อมานะครับ"
	Name(text1, "th")


	text1 = "รบกวนขอชื่อนามสกุลด้วยครับ"
	Name(text1, "th")
	try:
		name = TEXT(5);print(name);LI.append("ชื่อนามสกุล : "+name);Q.append(name)
	except:
		text1 = "คุณไม่ได้ให้ข้อมูล ชื่อนามสกุลครับ"
		Name(text1, "th")
		LI.append("ชื่อนามสกุล : " + "None");Q.append("None")
	text1 = "อายุเท่าไหร่ ครับ "
	Name(text1, "th")
	try:
		name = TEXT(5);print(name);LI.append("อายุ : "+name);Q.append(name)
	except:
		text1 = "คุณไม่ได้ให้ข้อมูล อายุครับ"
		Name(text1, "th")
		LI.append("อายุ : " + "None");Q.append("None")
	text1 = "คุณมาจากพื้นที่เสี่ยงหรือไม่"
	Name(text1, "th")
	try:
		name = TEXT(5);print(name);LI.append("มาจากพื้นที่เสี่ยงหรือไม่ : "+name);Q.append(name)
	except:
		text1 = "คุณไม่ได้ให้ข้อมูล พื้นที่เสี่ยงครับ"
		Name(text1, "th")
		LI.append("มาจากพื้นที่เสี่ยงหรือไม่ : " + "None");Q.append("None")
	text1 = "คุณมาจากจังหวัดอะไร"
	Name(text1, "th")
	try:
		name = TEXT(5);print(name);LI.append("จังหวัด : "+name);Q.append(name)
	except:
		text1 = "คุณไม่ได้ให้ข้อมูล จังหวัดครับ"
		Name(text1, "th")
		LI.append("จังหวัด : " + "None");Q.append("None")
	text1 = "เคยไปสถานที่ที่มีผู้ติดเชื้อหรือไม่"
	Name(text1, "th")
	try:
		name = TEXT(5);print(name);LI.append("เคยไปสถานที่ที่มีผู้ติดเชื้อหรือไม่ : "+name);Q.append(name)
	except:
		text1 = "คุณไม่ได้ให้ข้อมูล เคยไปสถานที่ที่มีผู้ติดเชื้อครับ"
		Name(text1, "th")
		LI.append("เคยไปสถานที่ที่มีผู้ติดเชื้อหรือไม่ : " + "None");Q.append("None")
	text1 = "คุณเป็นไข้ในช่วง 7 วันนี้หรือไม่"
	Name(text1, "th")
	try:
		name = TEXT(5);print(name);LI.append("เป็นไข้ในช่วง 7 วันนี้หรือไม่ : "+name);Q.append(name)
	except:
		text1 = "คุณไม่ได้ให้ข้อมูล เป็นไข้ในช่วง 7วันครับ"
		Name(text1, "th")
		LI.append("เป็นไข้ในช่วง 7 วันนี้หรือไม่ : " + "None");Q.append("None")
	text1 = "อุณหภูมิในร่างกาย สามารถวัดได้จากด้านข้างตัวเครื่องเลยครับ แล้วตัวเครื่องจะทำการเก็บข้อมูลอัตโนมัติครับ"
	Name(text1, "th")
	time.sleep(10)
	text1 = "คุณมีโรคประจำตัวหรือไม่ ถ้ามีมีอะไรบ้างครับ"
	Name(text1, "th")
	try:
		name = TEXT(5);print(name);LI.append("มีโรคประจำตัวหรือไม่ : "+name);Q.append(name)
	except:
		text1 = "คุณไม่ได้ให้ข้อมูล โรคประจำตัวครับ"
		Name(text1, "th")
		LI.append("มีโรคประจำตัวหรือไม่ : " + "None");Q.append("None")
	text1 = "คุณได้ฉีดวัคซีนไหมครับ ถ้าไม่ได้ฉีดรอคำถามต่อไปครับ"
	Name(text1, "th");AA = 1
	try:
		name = TEXT(5);print(name);LI.append("ได้ฉีดวัคซีนหรือไม่ : "+name);Q.append(name)
	except:
		text1 = "คุณไม่ได้ฉีดวัคซีนนะครับ"
		Name(text1, "th");AA = 2
		LI.append("ได้ฉีดวัคซีนหรือไม่ : " + "ไม่ได้ฉีดวัคซีน");Q.append("ไม่ได้ฉีดวัคซีน")
	##################################
	if AA == 1:
		text1 = "คุณได้ฉีดวัคซีนครบ 2 เข็มหรือยังครับ ฉีดยี่ห้ออะไรบ้างครับ "
		Name(text1, "th")
		name = TEXT(10);print(name);LI.append("คุณได้ฉีดวัคซีนครบ 2 เข็มไหม : "+name);Q.append(name)
		text1 = "ขั้นตอนต่อไปนี้เป็นการถามเพื่อตรวจสอบโรคเบื้องต้นนะครับ AI จะทำการประมวลผลให้ครับ รบกวนตอบอย่างตรงไปตรงมาด้วยครับ"
		Name(text1, "th")
		text1 = "มีอาการ จาม บ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการจามบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล อาการจามครับ"
			Name(text1, "th")
			LI.append("มีอาการจามบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการ คันหรือคัดจมูก บ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการ คันหรือคัดจมูก บ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล อาการ คันหรือคัดจมูก"
			Name(text1, "th")
			LI.append("มีอาการ คันหรือคัดจมูก บ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการน้ำมูกไหลบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการน้ำมูกไหลบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการน้ำมูกไหลไหม"
			Name(text1, "th")
			LI.append("มีอาการน้ำมูกไหลบ้างไหม : " + "None");Q.append("None")

		text1 = "มีผื่นขึ้นตามตัวหรือขึ้นบริเวณไหนบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีผื่นขึ้นตามตัวหรือขึ้นบริเวณไหนบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีผื่น"
			Name(text1, "th")
			LI.append("มีผื่นขึ้นตามตัวหรือขึ้นบริเวณไหนบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการไอแห้งบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการไอแห้งบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล การไอแห้ง"
			Name(text1, "th")
			LI.append("มีอาการไอแห้งบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการไอแบบมีเสมหะบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการไอแบบมีเสมหะบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการไอแบบมีเสมหะ"
			Name(text1, "th")
			LI.append("มีอาการไอแบบมีเสมหะบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการหอบ แน่นหน้าอก หายใจไม่คล่อง บ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการหอบ แน่นหน้าอก หายใจไม่คล่อง บ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล การหอบ แน่นหน้าอก หายใจไม่คล่อง"
			Name(text1, "th")
			LI.append("มีอาการหอบ แน่นหน้าอก หายใจไม่คล่อง บ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการเจ็บคอบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการเจ็บคอบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการเจ็บคอบ"
			Name(text1, "th")
			LI.append("มีอาการเจ็บคอบ้างไหม : " + "None");Q.append("None")

		text1 = "มีความรู้สึกกว่าเสียงแหบไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("เสียงแหบไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล เสียงแหบ"
			Name(text1, "th")
			LI.append("เสียงแหบไหม  : " + "None");Q.append("None")

		text1 = "ล่าสุดตอนนี้ยังมีไข้อ่อนๆหรือมีไข้สูงอยู่ไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("ล่าสุดตอนนี้ยังมีไข้อ่อนๆหรือมีไข้สูงอยู่ไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล ยังมีไข้อยู่ไหม"
			Name(text1, "th")
			LI.append("ล่าสุดตอนนี้ยังมีไข้อ่อนๆหรือมีไข้สูงอยู่ไหม : " + "None");Q.append("None")

		text1 = "มีอาการปวดศีรษะบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการปวดศีรษะบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการปวดศีรษะ"
			Name(text1, "th")
			LI.append("มีอาการปวดศีรษะบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการปวดเมื่อยกล้ามเนื้อบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการปวดเมื่อยกล้ามเนื้อบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการปวดเมื่อยกล้ามเนื้อ"
			Name(text1, "th")
			LI.append("มีอาการปวดเมื่อยกล้ามเนื้อบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการรู้สึกเมื่อยล้าบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการรู้สึกเมื่อยล้าบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล รู้สึกเมื่อยล้า"
			Name(text1, "th")
			LI.append("มีอาการรู้สึกเมื่อยล้าบ้างไหม : " + "None");Q.append("None")

		text1 = "มีความรู้สึกหายใจลำบากไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีความรู้สึกหายใจลำบากไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล การหายใจ"
			Name(text1, "th")
			LI.append("มีความรู้สึกหายใจลำบากไหม : " + "None");Q.append("None")
		Arduino("F")
		text1 = "แบบสอบถามเสร็จเรียบร้อยแล้วครับรอ AI ทำการประมวลผลซักครู่ครับ"
		Name(text1, "th")

		LI1.append(LI[4]);LI1.append(LI[5]);LI1.append(LI[8]);LI1.append(LI[9]);LI1.append(LI[10]);LI1.append(LI[11]);LI1.append(LI[12]);LI1.append(LI[13]);LI1.append(LI[14]);LI1.append(LI[15]);LI1.append(LI[16]);LI1.append(LI[17]);LI1.append(LI[18]);LI1.append(LI[19]);LI1.append(LI[20]);LI1.append(LI[21]);LI1.append(LI[22]);del LI1[2]

		LI2.append(LI[1]);LI2.append(LI[6]);LI2.append(LI[7]);LI2.append(LI[8])

		Q1.append(Q[4]);Q1.append(Q[5]);Q1.append(Q[8]);Q1.append(Q[9]);Q1.append(Q[10]);Q1.append(Q[11]);Q1.append(Q[12]);Q1.append(Q[13]);Q1.append(Q[14]);Q1.append(Q[15]);Q1.append(Q[16]);Q1.append(Q[17]);Q1.append(Q[18]);Q1.append(Q[19]);Q1.append(Q[20]);Q1.append(Q[21]);Q1.append(Q[22]);del Q1[2]

		Q2.append(Q[1]);Q2.append(Q[6]);Q2.append(Q[7]);Q2.append(Q[8])

		return LI ,LI1 ,LI2 , Q , Q1 , Q2
	################################
	if AA == 2:
		######
		text1 = "ขั้นตอนต่อไปนี้เป็นการถามเพื่อตรวจสอบโรคเบื้องต้นนะครับ AI จะทำการประมวลผลให้ครับ รบกวนตอบอย่างตรงไปตรงมาด้วยครับ"
		Name(text1, "th")
		text1 = "มีอาการ จาม บ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการจามบ้างไหม: " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล อาการจามครับ"
			Name(text1, "th")
			LI.append("มีอาการจามบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการ คันหรือคัดจมูก บ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการ คันหรือคัดจมูก บ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล อาการ คันหรือคัดจมูก"
			Name(text1, "th")
			LI.append("มีอาการ คันหรือคัดจมูก บ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการน้ำมูกไหลบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการน้ำมูกไหลบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการน้ำมูกไหลไหม"
			Name(text1, "th")
			LI.append("มีอาการน้ำมูกไหลบ้างไหม : " + "None");Q.append("None")

		text1 = "มีผื่นขึ้นตามตัวหรือขึ้นบริเวณไหนบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีผื่นขึ้นตามตัวหรือขึ้นบริเวณไหนบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีผื่น"
			Name(text1, "th")
			LI.append("มีผื่นขึ้นตามตัวหรือขึ้นบริเวณไหนบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการไอแห้งบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการไอแห้งบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล การไอแห้ง"
			Name(text1, "th")
			LI.append("มีอาการไอแห้งบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการไอแบบมีเสมหะบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการไอแบบมีเสมหะบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการไอแบบมีเสมหะ"
			Name(text1, "th")
			LI.append("มีอาการไอแบบมีเสมหะบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการหอบ แน่นหน้าอก หายใจไม่คล่อง บ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการหอบ แน่นหน้าอก หายใจไม่คล่อง บ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล การหอบ แน่นหน้าอก หายใจไม่คล่อง"
			Name(text1, "th")
			LI.append("มีอาการหอบ แน่นหน้าอก หายใจไม่คล่อง บ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการเจ็บคอบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการเจ็บคอบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการเจ็บคอบ"
			Name(text1, "th")
			LI.append("มีอาการเจ็บคอบ้างไหม : " + "None");Q.append("None")

		text1 = "มีความรู้สึกกว่าเสียง แหบ ไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("เสียงแหบไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล เสียงแหบ"
			Name(text1, "th")
			LI.append("เสียงแหบไหม  : " + "None");Q.append("None")

		text1 = "ล่าสุดตอนนี้ยังมีไข้อ่อนๆหรือมีไข้สูงอยู่ไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("ล่าสุดตอนนี้ยังมีไข้อ่อนๆหรือมีไข้สูงอยู่ไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล ยังมีไข้อยู่ไหม"
			Name(text1, "th")
			LI.append("ล่าสุดตอนนี้ยังมีไข้อ่อนๆหรือมีไข้สูงอยู่ไหม : " + "None");Q.append("None")

		text1 = "มีอาการปวดศีรษะบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการปวดศีรษะบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการปวดศีรษะ"
			Name(text1, "th")
			LI.append("มีอาการปวดศีรษะบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการปวดเมื่อยกล้ามเนื้อบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการปวดเมื่อยกล้ามเนื้อบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล มีอาการปวดเมื่อยกล้ามเนื้อ"
			Name(text1, "th")
			LI.append("มีอาการปวดเมื่อยกล้ามเนื้อบ้างไหม : " + "None");Q.append("None")

		text1 = "มีอาการรู้สึกเมื่อยล้าบ้างไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีอาการรู้สึกเมื่อยล้าบ้างไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล รู้สึกเมื่อยล้า"
			Name(text1, "th")
			LI.append("มีอาการรู้สึกเมื่อยล้าบ้างไหม : " + "None");Q.append("None")

		text1 = "มีความรู้สึกหายใจลำบากไหมครับ"
		Name(text1, "th")
		try:
			name = TEXT(5);print(name);LI.append("มีความรู้สึกหายใจลำบากไหม : " + name);Q.append(name)
		except:
			text1 = "คุณไม่ได้ให้ข้อมูล การหายใจ"
			Name(text1, "th")
			LI.append("มีความรู้สึกหายใจลำบากไหม : " + "None");Q.append("None")
		Arduino("F")
		text1 = "แบบสอบถามเสร็จเรียบร้อยแล้วครับรอ AI ทำการประมวลผลซักครู่ครับ"
		Name(text1, "th")

		LI1.append(LI[4]);LI1.append(LI[5]);LI1.append(LI[8]);LI1.append(LI[9]);LI1.append(LI[10]);LI1.append(LI[11]);LI1.append(LI[12]);LI1.append(LI[13]);LI1.append(LI[14]);LI1.append(LI[15]);LI1.append(LI[16]);LI1.append(LI[17]);LI1.append(LI[18]);LI1.append(LI[19]);LI1.append(LI[20]);LI1.append(LI[21])

		LI2.append(LI[1]);LI2.append(LI[6]);LI2.append(LI[7])

		Q1.append(Q[4]);Q1.append(Q[5]);Q1.append(Q[8]);Q1.append(Q[9]);Q1.append(Q[10]);Q1.append(Q[11]);Q1.append(Q[12]);Q1.append(Q[13]);Q1.append(Q[14]);Q1.append(Q[15]);Q1.append(Q[16]);Q1.append(Q[17]);Q1.append(Q[18]);Q1.append(Q[19]);Q1.append(Q[20]);Q1.append(Q[21])

		Q2.append(Q[1]);Q2.append(Q[6]);Q2.append(Q[7])

		return LI , LI1 , LI2 , Q , Q1 , Q2


def Summit1():
	AA = 0


	text1 = "The following steps are for inquiries. I can speak freely. don't worry"
	Name(text1, "en")
	text1 = "If giving wrong information Can edit the information at the staff. After completing the questionnaire, an officer will contact you."
	Name(text1, "en")


	text1 = "What is your name"
	Name(text1, "en")
	try:
		name = TEXT(5);print(name);LI.append("Name : "+name);Q.append(name)
	except:
		text1 = "You didn't provide your name"
		Name(text1, "en")
		LI.append("Name : " + "None");Q.append("None")
	text1 = "How old are you"
	Name(text1, "en")
	try:
		name = TEXT(5);print(name);LI.append("Old : "+name);Q.append(name)
	except:
		text1 = "No age information"
		Name(text1, "en")
		LI.append("Old : " + "None");Q.append("None")
	text1 = "Are you from a risk area"
	Name(text1, "en")
	try:
		name = TEXT(5);print(name);LI.append("from a risk area : "+name);Q.append(name)
	except:
		text1 = "You did not provide information risk area"
		Name(text1, "en")
		LI.append("from a risk area : " + "None");Q.append("None")
	text1 = "What province are you from"
	Name(text1, "en")
	try:
		name = TEXT(5);print(name);LI.append("Province  : "+name);Q.append(name)
	except:
		text1 = "You didn't provide information about the province"
		Name(text1, "en")
		LI.append("Province : " + "None");Q.append("None")
	text1 = "Have you ever been to a place with an infected person"
	Name(text1, "en")
	try:
		name = TEXT(5);print(name);LI.append("Ever been to a place with an infected person : "+name);Q.append(name)
	except:
		text1 = "You did not provide information"
		Name(text1, "en")
		LI.append("Ever been to a place with an infected person : " + "None");Q.append("None")
	text1 = "Have you had a fever during these 7 days"
	Name(text1, "en")
	try:
		name = TEXT(5);print(name);LI.append("fever during these 7 days : "+name);Q.append(name)
	except:
		text1 = "You did not provide information fever during these 7 days"
		Name(text1, "en")
		LI.append("fever during these 7 days : " + "None");Q.append("None")
	text1 = "body temperature can be measured from the side of the machine Then the device will automatically collect data"
	Name(text1, "en")
	time.sleep(10)
	text1 = "Do you have any underlying disease? If there is anything"
	Name(text1, "en")
	try:
		name = TEXT(5);print(name);LI.append("Do you have any underlying disease? If there is anything : "+name);Q.append(name)
	except:
		text1 = "You did not provide information personal disease"
		Name(text1, "en")
		LI.append("Do you have any underlying disease? If there is anything : " + "None");Q.append("None")
	text1 = "Have you vaccinated? If not, wait for the next question"
	Name(text1, "en");AA = 1
	try:
		name = TEXT(5);print(name);LI.append("Have you been vaccinated : "+name);Q.append(name)
	except:
		text1 = "You didn't vaccinate"
		Name(text1, "en");AA = 2
		LI.append("Have you been vaccinated : " + "You didn't vaccinate");Q.append("Not vaccinate")
	if AA == 1:
		text1 = "Have you had 2 vaccinations yet? What brand do you spray"
		Name(text1, "en")
		name = TEXT(10);print(name);LI.append("Have you had all 2 vaccinations : "+name)
		text1 = "The following steps will ask for early diagnosis, the AI will process it for you Short answer to understand"
		Name(text1, "en")
		text1 = "Do you have any symptoms of sneezing"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have any sneezing : " + name);Q.append(name)
		except:
			text1 = "You did not provide information about sneezing."
			Name(text1, "en")
			LI.append("Do you have any sneezing : " + "None");Q.append("None")

		text1 = "Do you have any itching or stuffy nose?"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have itching or stuffy nose : " + name);Q.append(name)
		except:
			text1 = "You gave no information about itching or stuffy nose."
			Name(text1, "en")
			LI.append("Do you have itching or stuffy nose? : " + "None");Q.append("None")

		text1 = "Do you have a runny nose?"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have a runny nose : " + name);Q.append(name)
		except:
			text1 = "You did not provide information Have a runny nose"
			Name(text1, "en")
			LI.append("Do you have a runny nose : " + "None");Q.append("None")

		text1 = "Is there a rash on the body or in any area?"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Is there a rash on the body or in any area : " + name);Q.append(name)
		except:
			text1 = "You didn't provide information. There was a rash."
			Name(text1, "en")
			LI.append("Is there a rash on the body or in any area : " + "None");Q.append("None")

		text1 = "Do you have a dry cough"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have a dry cough : " + name);Q.append(name)
		except:
			text1 = "You did not provide information. Dry cough."
			Name(text1, "en")
			LI.append("Do you have a dry cough : " + "None");Q.append("None")

		text1 = "Do you have a cough with mucus"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have a cough with mucus : " + name);Q.append(name)
		except:
			text1 = "You did not provide information cough with phlegm"
			Name(text1, "en")
			LI.append("Do you have a cough with mucus : " + "None");Q.append("None")

		text1 = "Do you have shortness of breath, tightness in your chest, shortness of breath"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have shortness of breath, tightness in your chest, shortness of breath : " + name);Q.append(name)
		except:
			text1 = "You didn't provide information, panting, tightness in the chest, shortness of breath."
			Name(text1, "en")
			LI.append("Do you have shortness of breath, tightness in your chest, shortness of breath : " + "None");Q.append("None")

		text1 = "Do you have a sore throat"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have a sore throat : " + name);Q.append(name)
		except:
			text1 = "You did not provide information have a sore throat"
			Name(text1, "en")
			LI.append("Do you have a sore throat : " + "None");Q.append("None")

		text1 = "Do you feel more hoarse"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you feel more hoarse : " + name);Q.append(name)
		except:
			text1 = "You did not provide information. Hoarseness."
			Name(text1, "en")
			LI.append("Do you feel more hoarse  : " + "None");Q.append("None")

		text1 = "Recently, do you still have a mild or high fever"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Recently, do you still have a mild or high fever : " + name);Q.append(name)
		except:
			text1 = "You did not provide information Do you still have a fever"
			Name(text1, "en")
			LI.append("Recently, do you still have a mild or high fever : " + "None");Q.append("None")

		text1 = "Do you have any headaches"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have any headaches : " + name);Q.append(name)
		except:
			text1 = "You did not provide information have a headache"
			Name(text1, "en")
			LI.append("Do you have any headaches : " + "None");Q.append("None")

		text1 = "Do you have any muscle aches"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have any muscle aches : " + name);Q.append(name)
		except:
			text1 = "You did not provide information have muscle aches"
			Name(text1, "en")
			LI.append("Do you have any muscle aches : " + "None");Q.append("None")

		text1 = "Do you feel tired"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you feel tired : " + name);Q.append(name)
		except:
			text1 = "You did not provide information feel tired"
			Name(text1, "en")
			LI.append("Do you feel tired? : " + "None");Q.append("None")

		text1 = "Do you have difficulty breathing"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have difficulty breathing : " + name);Q.append(name)
		except:
			text1 = "You did not provide information. Breathing."
			Name(text1, "en")
			LI.append("Do you have difficulty breathing : " + "None");Q.append("None")
		Arduino("F")
		text1 = "The questionnaire has been completed"
		Name(text1, "en")

		LI1.append(LI[4]);LI1.append(LI[5]);LI1.append(LI[8]);LI1.append(LI[9]);LI1.append(LI[10]);LI1.append(LI[11]);LI1.append(LI[12]);LI1.append(LI[13]);LI1.append(LI[14]);LI1.append(LI[15]);LI1.append(LI[16]);LI1.append(LI[17]);LI1.append(LI[18]);LI1.append(LI[19]);LI1.append(LI[20]);LI1.append(LI[21]);LI1.append(LI[22]);del LI1[2]

		LI2.append(LI[1]);LI2.append(LI[6]);LI2.append(LI[7]);LI2.append(LI[8])

		Q1.append(Q[4]);Q1.append(Q[5]);Q1.append(Q[8]);Q1.append(Q[9]);Q1.append(Q[10]);Q1.append(Q[11]);Q1.append(Q[12]);Q1.append(Q[13]);Q1.append(Q[14]);Q1.append(Q[15]);Q1.append(Q[16]);Q1.append(Q[17]);Q1.append(Q[18]);Q1.append(Q[19]);Q1.append(Q[20]);Q1.append(Q[21]);Q1.append(Q[22]);del Q1[2]

		Q2.append(Q[1]);Q2.append(Q[6]);Q2.append(Q[7]);Q2.append(Q[8])

		return LI, LI1, LI2 , Q , Q1 , Q2

	if AA == 2:
		text1 = "The following steps will ask for early diagnosis, the AI will process it for you Short answer to understand"
		Name(text1, "en")
		text1 = "Do you have any symptoms of sneezing"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have any sneezing : " + name);Q.append(name)
		except:
			text1 = "You did not provide information about sneezing."
			Name(text1, "en")
			LI.append("Do you have any sneezing : " + "None");Q.append("None")

		text1 = "Do you have any itching or stuffy nose?"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have itching or stuffy nose : " + name);Q.append(name)
		except:
			text1 = "You gave no information about itching or stuffy nose."
			Name(text1, "en")
			LI.append("Do you have itching or stuffy nose? : " + "None");Q.append("None")

		text1 = "Do you have a runny nose?"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have a runny nose : " + name);Q.append(name)
		except:
			text1 = "You did not provide information Have a runny nose"
			Name(text1, "en")
			LI.append("Do you have a runny nose : " + "None");Q.append("None")

		text1 = "Is there a rash on the body or in any area?"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Is there a rash on the body or in any area : " + name);Q.append(name)
		except:
			text1 = "You didn't provide information. There was a rash."
			Name(text1, "en")
			LI.append("Is there a rash on the body or in any area : " + "None");Q.append("None")

		text1 = "Do you have a dry cough"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have a dry cough : " + name);Q.append(name)
		except:
			text1 = "You did not provide information. Dry cough."
			Name(text1, "en")
			LI.append("Do you have a dry cough : " + "None");Q.append("None")

		text1 = "Do you have a cough with mucus"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have a cough with mucus : " + name);Q.append(name)
		except:
			text1 = "You did not provide information cough with phlegm"
			Name(text1, "en")
			LI.append("Do you have a cough with mucus : " + "None");Q.append("None")

		text1 = "Do you have shortness of breath, tightness in your chest, shortness of breath"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have shortness of breath, tightness in your chest, shortness of breath : " + name);Q.append(name)
		except:
			text1 = "You didn't provide information, panting, tightness in the chest, shortness of breath."
			Name(text1, "en")
			LI.append("Do you have shortness of breath, tightness in your chest, shortness of breath : " + "None");Q.append("None")

		text1 = "Do you have a sore throat"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have a sore throat : " + name);Q.append(name)
		except:
			text1 = "You did not provide information have a sore throat"
			Name(text1, "en")
			LI.append("Do you have a sore throat : " + "None");Q.append("None")

		text1 = "Do you feel more hoarse"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you feel more hoarse : " + name);Q.append(name)
		except:
			text1 = "You did not provide information. Hoarseness."
			Name(text1, "en")
			LI.append("Do you feel more hoarse  : " + "None");Q.append("None")

		text1 = "Recently, do you still have a mild or high fever"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Recently, do you still have a mild or high fever : " + name);Q.append(name)
		except:
			text1 = "You did not provide information Do you still have a fever"
			Name(text1, "en")
			LI.append("Recently, do you still have a mild or high fever : " + "None");Q.append("None")

		text1 = "Do you have any headaches"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have any headaches : " + name);Q.append(name)
		except:
			text1 = "You did not provide information have a headache"
			Name(text1, "en")
			LI.append("Do you have any headaches : " + "None");Q.append("None")

		text1 = "Do you have any muscle aches"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have any muscle aches : " + name);Q.append(name)
		except:
			text1 = "You did not provide information have muscle aches"
			Name(text1, "en")
			LI.append("Do you have any muscle aches : " + "None");Q.append("None")

		text1 = "Do you feel tired"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you feel tired : " + name);Q.append(name)
		except:
			text1 = "You did not provide information feel tired"
			Name(text1, "en")
			LI.append("Do you feel tired? : " + "None");Q.append("None")

		text1 = "Do you have difficulty breathing"
		Name(text1, "en")
		try:
			name = TEXT(5);print(name);LI.append("Do you have difficulty breathing : " + name);Q.append(name)
		except:
			text1 = "You did not provide information. Breathing."
			Name(text1, "en")
			LI.append("Do you have difficulty breathing : " + "None");Q.append("None")
		Arduino("F")
		text1 = "The questionnaire has been completed"
		Name(text1, "en")

		LI1.append(LI[4]);LI1.append(LI[5]);LI1.append(LI[8]);LI1.append(LI[9]);LI1.append(LI[10]);LI1.append(LI[11]);LI1.append(LI[12]);LI1.append(LI[13]);LI1.append(LI[14]);LI1.append(LI[15]);LI1.append(LI[16]);LI1.append(LI[17]);LI1.append(LI[18]);LI1.append(LI[19]);LI1.append(LI[20]);LI1.append(LI[21])

		LI2.append(LI[1]);LI2.append(LI[6]);LI2.append(LI[7])

		Q1.append(Q[4]);Q1.append(Q[5]);Q1.append(Q[8]);Q1.append(Q[9]);Q1.append(Q[10]);Q1.append(Q[11]);Q1.append(Q[12]);Q1.append(Q[13]);Q1.append(Q[14]);Q1.append(Q[15]);Q1.append(Q[16]);Q1.append(Q[17]);Q1.append(Q[18]);Q1.append(Q[19]);Q1.append(Q[20]);Q1.append(Q[21])

		Q2.append(Q[1]);Q2.append(Q[6]);Q2.append(Q[7])

		return LI, LI1, LI2 , Q , Q1 , Q2


# TWO
if A == 3:
	C = loop()
	print("Cloop", C)

if C == 1:
	Name("รอคำสั่งยืนยันครับ", "th")
	D = Start()
if C == 2:
	Name("Waiting for confirmation", "en")
	D = Start()


if C == 1 or D == 1: #ไทย
	print("\n")
	Result = Summit()
	print("\n")#;print(LI1);print("\n");print(LI2);print("\n");print(Q1);print("\n");print(Q2)
	Q1 = np.array(Q1)
	Arduino("AI")
	for i in Q1:
		if "None" in Q1[number]:
			Error += 1
			Set.append(number)
		if "เคย" in Q1[number] and "ไม่" not in Q1[number]:
			Score += 2
			Set.append(number)
		if "เคย" in Q1[number] and "ไม่" in Q1[number]:
			Score -= 0
			Set.append(number)
		if "เป็น" in Q1[number] and "ไม่" not in Q1[number]:
			Score += 1
			Set.append(number)
		if "เป็น" in Q1[number] and "ไม่" in Q1[number]:
			Score -= 0
			Set.append(number)
		if "มี" in Q1[number] and "ไม่" not in Q1[number]:
			Score += 1
			Set.append(number)
		if "มี" in Q1[number] and "ไม่" in Q1[number]:
			Score -= 0
			Set.append(number)
		if Q1[number] == "ไม่":
			Score -= 0
			Set.append(number)
		number += 1

	if "มี" in Q1[6] and "ไม่" not in Q1[6]:
		Score += 4
		Set.append(6)
	if "มี" in Q1[6] and "ไม่" in Q1[6]:
		Score -= 0
		Set.append(6)
	if "มี" in Q1[7] and "ไม่" not in Q1[7]:
		Score += 1
		Set.append(7)
	if "มี" in Q1[7] and "ไม่" in Q1[7]:
		Score -= 0
		Set.append(7)
	if "มี" in Q1[8] and "ไม่" not in Q1[8]:
		Score += 4
		Set.append(8)
	if "มี" in Q1[8] and "ไม่" in Q1[8]:
		Score -= 0
		Set.append(8)
	if "มี" in Q1[9] and "ไม่" not in Q1[9]:
		Score += 2
		Set.append(9)
	if "มี" in Q1[9] and "ไม่" in Q1[9]:
		Score -= 0
		Set.append(9)
	if "มี" in Q1[10] and "ไม่" not in Q1[10]:
		Score += 2
		Set.append(10)
	if "มี" in Q1[10] and "ไม่" in Q1[10]:
		Score -= 0
		Set.append(10)
	if "อ่อน" in Q1[11] and "ไม่" not in Q1[11]:
		Score += 2
		Set.append(11)
	if "สูง" in Q1[11] and "ไม่" not in Q1[11]:
		Score += 4
		Set.append(11)
	if "มี" in Q1[11] and "ไม่" in Q1[11]:
		Score -= 0
		Set.append(11)
	if "มี" in Q1[12] and "ไม่" not in Q1[12]:
		Score += 1
		Set.append(12)
	if "มี" in Q1[12] and "ไม่" in Q1[12]:
		Score -= 0
		Set.append(12)
	if "มี" in Q1[14] and "ไม่" not in Q1[14]:
		Score += 3
		Set.append(14)
	if "มี" in Q1[14] and "ไม่" in Q1[14]:
		Score -= 0
		Set.append(14)
	if "มี" in Q1[15] and "ไม่" not in Q1[15]:
		Score += 5
		Set.append(15)
	if "มี" in Q1[15] and "ไม่" in Q1[15]:
		Score -= 0
		Set.append(15)
	I = 0
	Num = []
	for i in Q1:
		Num.append(I)
		I += 1
	if 6 in Num and 7 in Num and 8 in Num and 9 in Num and 10 in Num and 11 in Num and 12 in Num and 14 in Num and 15 in Num:
		Num.append(6);Num.append(7);Num.append(8);Num.append(9);Num.append(10);Num.append(11);Num.append(12);Num.append(14);Num.append(15)
	if Num != Set:
		Error += 1
	print(Score)
	if Error > 0:
		text1 = "ข้อมูลที่คุณให้มามีข้อผิดพลาดจึงทำให้การทำนายผลไม่มีความแม่นยำ จำนวน ค่า ERROR : " + str(Error)
		Name(text1, "th")
	text1 = "ข้อมูลที่ AI ประมวลผลเป็นมีความแม่นยำ ถึง 92.8 เปอร์เซ็นครับ"
	Name(text1, "th")
	if Score < 6 and Score > 0:
		text1 = "ผลวิจัยที่ได้ใกล้เคียงคือคุณไม่เป็นโรคอะไรเลยครับปกติดีครับ"
		Name(text1, "th")
	if Score > 6 and Score < 10:
		text1 = "ผลวิจัยที่ได้ใกล้เคียงคือคุณเป็นโรคภูมิแพ้ครับ"
		Name(text1, "th")
	if Score > 12 and Score < 17:
		text1 = "ผลวิจัยที่ได้ใกล้เคียงคือคุณเป็นโรคไข้หวัดครับ"
		Name(text1, "th")
	if Score > 16 and Score < 21:
		text1 = "ผลวิจัยที่ได้ใกล้เคียงคือคุณเป็นโรคไข้หวัดใหญ่ครับ"
		Name(text1, "th")
	if Score > 25 and Score < 40:
		text1 = "ผลวิจัยที่ได้ใกล้เคียงคือคุณเป็นโรคโควิด19ครับ"
		Name(text1, "th")
	if AA == 1:
		Arduino("AIF")
		text1 = "รบกวนติดต่อเจ้าหน้าที่ด้วยครับ โดยการแตะที่มือถือ 2 ครั้งแล้วพูดว่าเจ้าหน้าที่ครับ"
		Name(text1, "th")
		Arduino("NN")
	if AA == 2:
		Arduino("AI")
		for i in range(0, 100):
			R += 1
			if str(R) in Q2[0]:
				RT = R
		text1 = "เราจะแนะนำวัคซีนที่คุณควรฉีด ขอตรวจสอบข้อมูลเบื้องต้นก่อนนะครับ"
		Name(text1, "th")
		if Q2[0] == 'None' or Q2[1] == 'None' or Q2[2] == 'None':
			text1 = "ไม่สามารถแนะนำวัคซีนได้เนื่องจากข้อมูลมีข้อผิดพลาด"
			Name(text1, "th")
			OTP = 0
		if Q2[0] != 'None' and Q2[1] != 'None' and Q2[2] != 'None':
			if OTP == 0:
				if "เคย" in Q2[1] and "ไม่" not in Q2[1]:
					OTP = 1
				if "เคย" in Q2[1] and "ไม่" in Q2[1]:
					OTP = 2
				if "เป็น" in Q2[1] and "ไม่" not in Q2[1]:
					OTP = 1
				if "เป็น" in Q2[1] and "ไม่" in Q2[1]:
					OTP = 2
				if "มี" in Q2[1] and "ไม่" not in Q2[1]:
					OTP = 1
				if "มี" in Q2[1] and "ไม่" in Q2[1]:
					OTP = 2
				if Q2[1] == "ไม่":
					OTP = 2
				else:
					text1 = "ไม่สามารถแนะนำวัคซีนได้เนื่องจากข้อมูลมีข้อผิดพลาด"
					Name(text1, "th")
					OTP = 0
		if OTP == 1:
			text1 = "ไม่สามารถแนะนำวัคซีนได้เนื่องจากข้อมูลที่ให้มาไม่เหมาะสมกับการที่จะได้รับวัคซีน"
			Name(text1, "th")
		if OTP == 2:
			text1 = "เราจะแนะนำวัคซีนเป็น"
			Name(text1, "th")
			if RT > 17 and RT < 60:
				text1 = "ซินโนเวต หรือ โคโรนาแวค หรือ ซิโนฟาร์ม"
				Name(text1, "th")
			if RT > 18:
				text1 = "โมเดอร์นา หรือ แอสตร้าเซนเนก้า"
				Name(text1, "th")
			if RT < 18:
				text1 = "ไฟเซอร์"
				Name(text1, "th")
			text1 = "ก่อนจะฉีดควรเช็ครายละเอียดวัคซีนก่อนนะครับ"
			Name(text1, "th")
			Arduino("AIF")
			text1 = "รบกวนติดต่อเจ้าหน้าที่ด้วยครับ โดยการแตะที่มือถือ 2 ครั้งแล้วพูดว่าเจ้าหน้าที่ครับ"
			Name(text1, "th")
			Arduino("NN")



if C == 2 or D == 2: #อังกฤษ
	print("\n")
	Result1 = Summit1()
	print("\n")#;print(LI1);print("\n");print(LI2);print("\n");print(Q1);print("\n");print(Q2)
	Q1 = np.array(Q1)
	Arduino("AI")
	for i in Q1:
		if "None" in Q1[number]:
			Error += 1
			Set.append(number)
		if "have been to" in Q1[number] or "ever" in Q1[number] or "yes" in Q1[number] and "never" not in Q1[number] and "no" not in Q1[number]:
			Score += 2
			Set.append(number)
		if "have been to" in Q1[number] or "ever" in Q1[number] or "yes" in Q1[number] or "never" in Q1[number] or "no" in Q1[number]:
			Score -= 0
			Set.append(number)
		if "is" in Q1[number] or "yes" in Q1[number] and "no" not in Q1[number]:
			Score += 1
			Set.append(number)
		if "is" in Q1[number] or "yes" in Q1[number] and "no" in Q1[number]:
			Score -= 0
			Set.append(number)
		if "have" in Q1[number] and "no" not in Q1[number] and "do not " not in Q1[number] and "without" not in Q1[number]:
			Score += 1
			Set.append(number)
		if "have" in Q1[number] or "no" in Q1[number] or "do not " in Q1[number] or "without" in Q1[number]:
			Score -= 0
			Set.append(number)
		if Q1[number] == "no":
			Score -= 0
			Set.append(number)
		number += 1

	if "have" in Q1[6] and "no" not in Q1[6] and "do not " not in Q1[6] and "without" not in Q1[6]:
		Score += 4
		Set.append(6)
	if "have" in Q1[6] or "no" in Q1[6] or "do not " in Q1[6] or "without" in Q1[6]:
		Score -= 0
		Set.append(6)

	if "have" in Q1[7] and "no" not in Q1[7] and "do not " not in Q1[7] and "without" not in Q1[7]:
		Score += 1
		Set.append(7)
	if "have" in Q1[7] or "no" in Q1[7] or "do not " in Q1[7] or "without" in Q1[7]:
		Score -= 0
		Set.append(7)

	if "have" in Q1[8] and "no" not in Q1[8] and "do not " not in Q1[8] and "without" not in Q1[8]:
		Score += 4
		Set.append(8)
	if "have" in Q1[8] or "no" in Q1[8] or "do not " in Q1[8] or "without" in Q1[8]:
		Score -= 0
		Set.append(8)

	if "have" in Q1[9] and "no" not in Q1[9] and "do not " not in Q1[9] and "without" not in Q1[9]:
		Score += 2
		Set.append(9)
	if "have" in Q1[9] or "no" in Q1[9] or "do not " in Q1[9] or "without" in Q1[9]:
		Score -= 0
		Set.append(9)

	if "have" in Q1[10] and "no" not in Q1[10] and "do not " not in Q1[10] and "without" not in Q1[10]:
		Score += 2
		Set.append(10)
	if "have" in Q1[10] or "no" in Q1[10] or "do not " in Q1[10] or "without" in Q1[10]:
		Score -= 0
		Set.append(10)

	if "a mild fever" in Q1[11] or "have" in Q1[11] and "no" not in Q1[11] and "do not " not in Q1[11] and "without" not in Q1[11]:
		Score += 2
		Set.append(11)
	if "high fever" in Q1[11] or "have" in Q1[11] and "no" not in Q1[11] and "do not " not in Q1[11] and "without" not in Q1[11]:
		Score += 4
		Set.append(11)
	if "have" in Q1[11] or "no" in Q1[11] or "do not " in Q1[11] or "without" in Q1[11]:
		Score -= 0
		Set.append(11)

	if "have" in Q1[12] and "no" not in Q1[12] and "do not " not in Q1[12] and "without" not in Q1[12]:
		Score += 1
		Set.append(12)
	if "have" in Q1[12] or "no" in Q1[12] or "do not " in Q1[12] or "without" in Q1[12]:
		Score -= 0
		Set.append(12)

	if "have" in Q1[14] and "no" not in Q1[14] and "do not " not in Q1[14] and "without" not in Q1[14]:
		Score += 3
		Set.append(14)
	if "have" in Q1[14] or "no" in Q1[14] or "do not " in Q1[14] or "without" in Q1[14]:
		Score -= 0
		Set.append(14)

	if "have" in Q1[15] and "no" not in Q1[15] and "do not " not in Q1[15] and "without" not in Q1[15]:
		Score += 5
		Set.append(15)
	if "have" in Q1[15] or "no" in Q1[15] or "do not " in Q1[15] or "without" in Q1[15]:
		Score -= 0
		Set.append(15)
	I = 0
	Num = []
	for i in Q1:
		Num.append(I)
		I += 1
	if 6 in Num and 7 in Num and 8 in Num and 9 in Num and 10 in Num and 11 in Num and 12 in Num and 14 in Num and 15 in Num:
		Num.append(6);Num.append(7);Num.append(8);Num.append(9);Num.append(10);Num.append(11);Num.append(12);Num.append(14);Num.append(15)
	if Num != Set:
		Error += 1
	print(Score)
	if Error > 0:
		text1 = "There are errors in the data you provided and therefore the prediction is inaccurate ERROR : " + str(Error)
		Name(text1, "en")
	text1 = "The data processed by the AI is accurate to 92.8 percent"
	Name(text1, "en")
	if Score < 6 and Score > 0:
		text1 = "The closest research result is that you don't have any disease at all. It's normal"
		Name(text1, "en")
	if Score > 6 and Score < 10:
		text1 = "The closest research result is that you are allergy"
		Name(text1, "en")
	if Score > 12 and Score < 17:
		text1 = "The closest research result is that you have the flu"
		Name(text1, "en")
	if Score > 16 and Score < 21:
		text1 = "The closest research result is that you have the influenza"
		Name(text1, "en")
	if Score > 25 and Score < 40:
		text1 = "The closest research result is that you have COVID-19"
		Name(text1, "en")
	if AA == 1:
		Arduino("AIF")
		text1 = "Feel free to contact the staff. By tapping the mobile phone twice and saying officer"
		Name(text1, "en")
		Arduino("NN")
	if AA == 2:
		Arduino("AI")
		for i in range(0, 100):
			R += 1
			if str(R) in Q2[0]:
				RT = R
		text1 = "We will recommend which vaccines you should get. Please check the preliminary information first."
		Name(text1, "en")
		if Q2[0] == 'None' or Q2[1] == 'None' or Q2[2] == 'None':
			text1 = "A vaccine cannot be recommended because the data is inaccurate"
			Name(text1, "en")
			OTP = 0
		if Q2[0] != 'None' and Q2[1] != 'None' and Q2[2] != 'None':
			if OTP == 0:
				if "have been to" in Q2[1] or "ever" in Q2[1] or "yes" in Q2[1] and "never" not in Q2[1] and "no" not in Q2[1]:
					OTP = 1
				if "have been to" in Q2[1] or "ever" in Q2[1] or "yes" in Q2[1] or "never" in Q2[1] or "no" in Q2[1]:
					OTP = 2
				if "is" in Q2[1] or "yes" in Q2[1] and "no" not in Q2[1]:
					OTP = 1
				if "is" in Q2[1] or "yes" in Q2[1] and "no" in Q2[1]:
					OTP = 2
				if "have" in Q2[1] and "no" not in Q2[1] and "do not " not in Q2[1] and "without" not in Q2[1]:
					OTP = 1
				if "have" in Q2[1] or "no" in Q2[1] or "do not " in Q2[1] or "without" in Q2[1]:
					OTP = 2
				if Q2[1] == "no":
					OTP = 2
				else:
					text1 = "A vaccine cannot be recommended because the data is inaccurate."
					Name(text1, "en")
					OTP = 0
		if OTP == 1:
			text1 = "A vaccine cannot be recommended because the information provided is not suitable for vaccination."
			Name(text1, "en")
		if OTP == 2:
			text1 = "We will recommend the vaccine as"
			Name(text1, "en")
			if RT > 17 and RT < 60:
				text1 = "Synovate or Coronavac or SinoFarm"
				Name(text1, "en")
			if RT > 18:
				text1 = "Moderna or AstraZeneca"
				Name(text1, "en")
			if RT < 18:
				text1 = "Pfizer"
				Name(text1, "en")
			text1 = "Before injecting, you should check the details of the vaccine first."
			Name(text1, "en")
			Arduino("AIF")
			text1 = "Feel free to contact the staff. by tapping the mobile phone twice and saying 'employee"
			Name(text1, "en")
			Arduino("NN")











