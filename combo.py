import numpy as np
import random as rd
import time 
import pyttsx3
from flask import Flask, render_template, request, redirect, url_for, jsonify

hits = {"jab": 1, "cross": 2, "look": 2, "rook": 2, "lut": 2, "rut": 2, "lunder": 2, "runder": 2, "lip": 1, "rip": 1, "lean": 2}
right = ["cross", "rook", "rut", "runder", "rip"]
left = ["jab", "look", "lut", "lunder", "lip"]
intervals = {1:0.0, 2:0.5, 3:1}
keys = list(intervals.keys())
intWeights = [1/k for k in keys]
length = ""
current = []
used = []

app = Flask(__name__)

@app.route('/')
def homePage():
     return render_template('FrontPage.html')

@app.route('/startCountdown', methods=['POST'])
def startCountdown():
  try:
      global length
      length = request.form.get('length', '').strip()
      if not length:
            return "Give a valid option"
      return redirect(url_for("countdown"))
  except Exception as e:
      return f"An error occurred: {str(e)}", 500   

@app.route("/countdown")
def countdown():
    return render_template("Countdown.html", seconds=3)

@app.route("/startCombo", methods=["POST"])
def start():
    callout()
    return jsonify(success=True)


def speak(voice):
  engine = pyttsx3.init()
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate + 1)
  engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
  engine.say(voice)

  engine.runAndWait()

def random_hits():
        hit = rd.choice(hits, replace=True)
        return hit

def callout():
    for i in random_hits():
        interval = rd.choices(keys, weights=intWeights, k=1)[0]
        speak(i)
        print("Move: " + i + "\n" + "Interval: " + str(intervals[interval]) + "s")
        time.sleep(intervals[interval])

if __name__ == '__main__':
    app.run(debug=True)


def IntervalCalc():
    interval = intervals[hits[current[0]]]
    if (current[0] in left and current[1] in left) or (current[0] in right and current[1] in right):
        return interval

    return interval +1

def Start():
    if not bool(current):
        current.append(random_hits)

    current.append(random_hits)
    WaitTime = IntervalCalc()
    speak(current[0])
    time.sleep(WaitTime)

    


