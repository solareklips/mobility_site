from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)
"""
JOBS = [
  {
    'id' : 1,
    'title' : 'Choose equipment',
    'info' : 'Choose between a bunch of equipment. If you have none, choose none.',
  },
  {
    'id' : 2,
    'title' : 'Choose muscle groups',
    'info' : 'Choose between six major muscle groups, that you want to stretch.',
  },
  {
    'id' : 3,
    'title' : 'Choose duration',
    'info' : 'Minimum time for a workout is two minutes, maximum is 60. Only choose whole minutes.'
  },
]
"""

def load_exercises_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM mobility.exercises"))
    exercises = []
    for row in result.all():
      exercises.append(dict(row))
    return exercises

"""
def load_exercises_from_db():
    with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM mobility.exercises"))
    result_all = result.all()
  
  first_result = result_all[0]
  item_nr = 0
  
  for item in result_all:
    exercise_result = result_all[item_nr]
    print("Exercise ID: ", exercise_result[0])
    print("Exercise Name: ", exercise_result[1])
    print("Two Side: ", exercise_result[2])
    item_nr += 1
"""
@app.route("/")
def hello_world():
    exercises = load_exercises_from_db
    return render_template('home.html', 
                          jobs=exercises)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

# kommet til 2:47:00 i video tutorialen
# https://www.youtube.com/watch?v=yBDHkveJUf4&t=6447s