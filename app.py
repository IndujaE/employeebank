from flask import Flask,render_template,request
from empdata import Employee

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

getemployee=Employee()
@app.route('/emp')

def empdata():
    return render_template('empdata.html',getemployee=getemployee)


if(__name__=='__main__'):
    app.run(debug=True)
