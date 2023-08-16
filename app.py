from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

@app.route("/")
def hello_world():
    return render_template('home.html',
                          jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

# kommet til 2:23:00 i video tutorialen
# https://www.youtube.com/watch?v=yBDHkveJUf4&t=6447s