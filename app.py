from flask import Flask,render_template ,jsonify
app = Flask(__name__)
JOBS =[
  {
    'id' : 1,
    'title' : 'Python Developer',
    'location' :' Pune,India',
    'salary': '4LPA'
},
{
    'id' : 2,
    'title' :'Data Analyst',
    'location' :' Mumbai,India',
    'salary': '5LPA'
},
{
    'id' : 3,
    'title' : 'Web Developer',
    'location' :'Banglore,India',
    'salary': '4 - 5LPA'
},
{
    'id' : 4,
    'title' :'Python Developer',
    'location' :' Pune,India',
    'salary': '4LPA - 5LPA'
},
{
    'id' : 5,
    'title' : 'Django Developer',
    'location' :' Pune,India',
    'salary': '5LPA - 7LPA'
}
]

@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS,company_name='Fresher')
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
   app.run(host = '0.0.0.0',debug = True)