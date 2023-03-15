from flask import Flask,render_template

app=Flask(__name__)

JOBS=[
  {
    'id':1,
  'title': 'data analyst',
    'salary':'Rs.100000'
  
  },
  {
    'id':2,
  'title': 'data scientist',
  'salary': 'Rs.1000040'
  },
{
    'id':3,
  'title': 'devop',
  'salary':'Rs.2000000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)