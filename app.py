from flask import Flask, render_template,jsonify
app=Flask(__name__)

JOBS=[
  {
    'id':1,
    'job':'software developer',
    'loc':'bangalore',
    'SAL':'2,00,000'
  },
  {
  'id':2,
    'job':'Automation engineer',
    'loc':'chennai',
    'SAL':'2,50,000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS,company='JOVIAN')

@app.route('/api/jobitem')
def jobdetail():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)