# spelling_bot.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openai
import time
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
AUDIO_FILENAME = "word.wav"
RECORD_SECONDS = 4
URL = "https://www.vocabulary.com/play/spelling-bee"

def run_bot():
    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(5)

    try:
        while True:
            try:
                driver.find_element(By.CLASS_NAME, "audio-icon").click()
                time.sleep(1)
            except:
                continue

            os.system(f"ffmpeg -y -f dshow -i audio='Stereo Mix (Realtek High Definition Audio)' -t {RECORD_SECONDS} -acodec pcm_s16le -ar 44100 -ac 1 {AUDIO_FILENAME}")
            
            with open(AUDIO_FILENAME, "rb") as audio_file:
                word = openai.Audio.transcribe("whisper-1", audio_file)["text"].strip()

            input_box = driver.find_element(By.CLASS_NAME, "spelling-input")
            input_box.clear()
            input_box.send_keys(word)
            input_box.send_keys(Keys.RETURN)

            time.sleep(4)
            try:
                restart = driver.find_element(By.CLASS_NAME, "btn-continue")
                if restart.is_displayed():
                    restart.click()
                    time.sleep(2)
            except:
                continue
    except KeyboardInterrupt:
        driver.quit()
