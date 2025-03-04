from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time
import os
import requests
import random

url = requests.get("https://xss-game.appspot.com/level1/frame")
#credentials for testing
#os.environ["PROFILE_PATH"] = "C:\\Users\\ambuj\\AppData\\Local\\Google\\Chrome\\User Data"

#options required for using existing chrome profiles
options = webdriver.ChromeOptions()
#options.add_argument(f"--user-data-dir={os.environ['PROFILE_PATH']}")
options.add_argument("--profile-directory=Default")

timers = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

def get_forms(url):
    soup = bs(url.content, "html.parser")
    print(soup.find_all("form"))

def form_details(form):
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "post").lower()

    inputs = [] 
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")

get_forms(url)
