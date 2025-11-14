import numpy as np
import random as rd
import time 
import pyttsx3
from flask import Flask, render_template, request, redirect, url_for, jsonify

hits = ["1", "2", "3", "4", "5", "6", "roll", "lean"]
weights = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2]
intervals = {1:0.0, 2:0.25, 3:0.5, 4:0.75, 5:1, 5:1.5, 6:2, }
keys = list(intervals.keys())
intWeights = [1/k for k in keys]
length = ""

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
        hit = np.random.choice(hits, size=int(length), replace=True, p=weights)
        return hit

def callout():
    for i in random_hits():
        interval = rd.choices(keys, weights=intWeights, k=1)[0]
        speak(i)
        print("Move: " + i + "\n" + "Interval: " + str(intervals[interval]) + "s")
        time.sleep(intervals[interval])

if __name__ == '__main__':
    app.run(debug=True)

