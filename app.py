from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Frontend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$250,000'
    },
    {
        'id': 2,
        'title': 'Backend Engineer',
        'location': 'Chicago',
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Abuja, Nigeria',
        'salary': '$120,000'
    },
    {
        'id': 4,
        'title': 'Software Engineer',
        'location': 'Los Angeles',
        'salary': '$350,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name = 'Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)