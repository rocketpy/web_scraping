import time
import pyttsx3
import pyautogui
from selenium import webdriver
import speech_recognition as sr
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By


rec = sr.Recognizer()
with sr.Microphone() as source_2:
    rec.adjust_for_ambient_noise(source_2, duration = 0.2)
    audio_2 = rec.listen(source_2)
    my_text = rec.recognize_google(audio_2)
    my_mext = str(my_text.lower())
