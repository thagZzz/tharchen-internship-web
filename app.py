from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Thimphu, Bhutan',
    'salary': 'Nu. 150,000'
}, {
    'id': 2,
    'title': 'Network admin',
    'location': 'Thimphu, Bhutan',
}, {
    'id': 3,
    'title': 'System admin',
    'location': 'Thimphu, Bhutan',
    'salary': 'Nu. 60,000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='TaTa')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
