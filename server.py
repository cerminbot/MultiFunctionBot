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
    parse = BeautifulSoup(driver.page_source, "lxml")
    driver.quit()
    return parse

@app.route('/')
def root():
    return "MultiFunction Bot is Up & Running!"

@app.route('/pahe')
def pahereq():
    judul = request.args.get('q') if request.args.get('q') else ""
    if request.args.get('q'):
        try:
            DATA = []
            parse = pahe(judul)
            for i in parse.findAll(class_="post-box-title"):
                link = "ss"
                judul = str(i.find("a"))
                DATA.append({"judul": judul, "link": link})
            return {
                "success": True,
                "result": DATA,
                "info": "Join telegram channel @YasirPediaChannel for updates."
            }
        except Exception as err:
            return str(err)
    else:
        try:
            DATA = []
            parse = pahe(judul)
            for i in parse.findAll(class_="post-box-title"):
                link = "ss"
                judul = "xx"
                DATA.append({"judul": judul, "link": link})
            return {
                "success": True,
                "result": DATA,
                "info": "Join telegram channel @YasirPediaChannel for updates."
            }
        except Exception as err:
            return str(err)

app.run(host="0.0.0.0", port=os.environ.get("PORT", 80))
