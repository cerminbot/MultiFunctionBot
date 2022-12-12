import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "MultiFunction Bot is Up & Running!"

@app.route('/pahe')
def pahe():
    if request.args.get('q'):
        judul = request.args.get('q')
        return judul
    else:
        return {
            'success': False,
            'msg': 'Isi parameter query, ex: https://yasirapi.eu.org/yt-search?q=scraping%20tutorial',
            'info': 'Join telegram channel @YasirPediaChannel for updates.',
        }

app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
