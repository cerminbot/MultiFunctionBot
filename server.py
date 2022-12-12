import os
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, request

app = Flask(__name__)

def pahe(title: str) -> str:
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"https://pahe.li/?s={title}")
    result = driver.page_source
    return result

@app.route('/')
def root():
    return "MultiFunction Bot is Up & Running!"

@app.route('/pahe')
def pahereq():
    if request.args.get('q'):
        judul = request.args.get('q')
        try:
            parse = BeautifulSoup(pahe(judul), "lxml")
            return parse
        except Exception as err:
            return str(err)
    else:
        return {
            'success': False,
            'msg': 'Isi parameter query, ex: https://yasirapi.eu.org/yt-search?q=scraping%20tutorial',
            'info': 'Join telegram channel @YasirPediaChannel for updates.',
        }

app.run(host="0.0.0.0", port=os.environ.get("PORT", 80))
