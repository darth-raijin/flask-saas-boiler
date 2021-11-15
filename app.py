import os
from flask import Flask, session, request, redirect, render_template, url_for, flash
from flask_session import Session
from dotenv import load_dotenv
from datetime import date
import sys
import uuid
import random
import json
import css_builder


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)


builder = css_builder.load_colors()

caches_folder = './.spotify_caches/'
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

def session_cache_path():
    return caches_folder + session.get('uuid')

@app.route('/')
def index():
        return render_template("index")

if __name__ == '__main__':
    app.run(threaded=True, port = 5000)