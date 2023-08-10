from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Equipment',
    'location' : 'Bengaluru, India',
    'salary' : 'Rs. 20,00,000'
  },
  {
    'id' : 2,
    'title' : 'Muscles',
    'location' : 'Delhi, India',
    'salary' : 'Rs. 25,00,000'
  },
  {
    'id' : 3,
    'title' : 'Musclegrups',
    'location' : 'Junlge, Amazonas'
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

# kommet til 1:51:18 i video tutorialen
# https://www.youtube.com/watch?v=yBDHkveJUf4&t=6447s