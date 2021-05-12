# Импорты модулей прослушки и преобразования в текст
import pyttsx3
import speech_recognition as sr
import time 
import webbrowser
import datetime
import os
run = True
options = {
	"name": ("катя" , "екатерина" , "катерина" , "катюша") ,

	"key_w": ("скажи" , "покажи" , "произнеси" , "расскажи" , "сколько"),

	"ctime" : ("сколько время" , "который час" , "время"),
	"browser" : ("вк" , "инстаграм" , "вконтакте" , "инста" , "экж" , "дневник" , "ютуб" , "видосы"), 
	"windows" : ("выключи компьютер" , "перезагрузи" , "выключи" , "перезагрузи компьютер"),
	"calculator" : ("посчитай" , "умножь" , "раздели" , "вычитание"),
	"work": ("заканчивай" , "стоп", "отключайся")


	
}
#Функци
def speak(what):
	print(what)
	engine.say(what)
	engine.runAndWait()
	engine.stop()

def recognize_cmd(cmd):
	if cmd.startswith(options['ctime']):
		now = datetime.datetime.now()
		speak("Сейчас " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
	elif cmd.startswith(options["browser"]):
		if cmd == 'вк' or cmd == 'вконтакте':
			speak("Открываю")
			webbrowser.open_new("https://vk.com")
		if cmd == 'инста' or cmd == 'instagram':
			speak("Открываю")
			webbrowser.open_new("https://www.instagram.com")
		if cmd == 'экж' or cmd == 'дневник':
			speak("Знания, оценки, домашка..")
			webbrowser.open_new("https://cop.admhmao.ru/")
		if cmd == "видосы" or cmd == "ютуб":
			speak("Открываю")
			webbrowser.open_new("https://www.youtube.com")	
	elif cmd.startswith(options["windows"]):
		if cmd == 'выключи' or cmd == 'выключи компьютер':
			speak("Произвожу выключение системы.")
			os.system("shutdown /s /t 1")
		if cmd == 'перезагрузи'	or cmd == "перезагрузи компьютер":
			speak("Произвожу перезагрузку системы.")
			os.system("shutdown /s /t 1")
	elif cmd.startswith(options["work"]):
		speak("Отключаюсь")
		exit()	
def record_volume():		
	r = sr.Recognizer()
	micro = sr.Microphone(device_index = 1)
	with micro:
	#Слушает микро, чтобы отличать шум от речи
		r.adjust_for_ambient_noise(micro)
		audio = r.listen(micro)
	try:
		voice = r.recognize_google(audio , language = "ru-RU").lower()
		if voice.startswith(options['name']):
			cmd = voice
			speak("Слушаю")
			for x in options['name']:
				cmd = cmd.replace(x,"").strip()	
				print("[log] Распознано: " + str(cmd))
			recognize_cmd(cmd)
		if voice.startswith(options['key_w']):
			cmd = voice
			speak("Слушаю")
			for x in options['key_w']:
				cmd = cmd.replace(x,'').strip()
				print("[log] Распознано: " + str(cmd))
				recognize_cmd(cmd)
		else:
			print("[log] Распознано: " + str(voice))		
			recognize_cmd(voice)
	except sr.UnknownValueError:
		print("[log] Голос не распознан!")
	except sr.RequestError as e:
		print("Неизвестная ошибка, проверьте интернет.")		
engine = pyttsx3.init()	
#Установить уникальный голос
voices = engine.getProperty('voices' )
engine.setProperty('voice' , voices[0].id )
speak("Приветствую Вас, Александр..Слушаю")

while run: 
	time.sleep(0.1)
	record_volume()
