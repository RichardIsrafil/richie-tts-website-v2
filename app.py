from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru',
  'salary': 'Rs. 1,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'San Francisco, USA'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Remote',
  'salary': 'Rs. 12,00,000'
}]

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/")
def ai4bharat():
  return render_template('home.html',jobs=JOBS, about="Text To Speech")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
