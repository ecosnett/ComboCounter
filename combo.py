import numpy as np
import random as rd
import time 
import pyttsx3
from flask import Flask, render_template, request, redirect, url_for, jsonify

hits = {"jab": 1, "cross": 2, "look": 2, "rook": 2, "lut": 2, "rut": 2, "lunder": 2, "runder": 2, "lip": 1, "rip": 1, "lean": 2}
right = ["cross", "rook", "rut", "runder", "rip"]
left = ["jab", "look", "lut", "lunder", "lip"]
intervals = {1:0.0, 2:0.5, 3:1}
current = []
used = []

# app = Flask(__name__)

# @app.route('/')
# def homePage():
#      return render_template('FrontPage.html')

# @app.route('/startCountdown', methods=['POST'])
# def startCountdown():
#   try:
#       global length
#       length = request.form.get('length', '').strip()
#       if not length:
#             return "Give a valid option"
#       return redirect(url_for("countdown"))
#   except Exception as e:
#       return f"An error occurred: {str(e)}", 500   

# @app.route("/countdown")
# def countdown():
#     return render_template("Countdown.html", seconds=3)

# @app.route("/startCombo", methods=["POST"])
# def start():
#     callout()
#     return jsonify(success=True)


def speak(voice):
  engine = pyttsx3.init()
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate + 1)
  engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
  engine.say(voice)

  engine.runAndWait()

def IntervalCalc():
    interval = intervals[hits[current[0]]]
    if (current[0] in left and current[1] in left) or (current[0] in right and current[1] in right):
        return interval+0.5

    return interval

def Start(length):
    while len(used) < length:
        if not bool(current):
            current.append(rd.choice(list(hits.keys())))

        current.append(rd.choice(list(hits.keys())))
        WaitTime = IntervalCalc()
        used.append(current[0])
        current.pop(0)
        speak(current[0])
        print(f"action:{current[0]}\ninterval:{WaitTime}")
        time.sleep(WaitTime)

Start(10)
