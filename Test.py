from flask import request,Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/profile/<yourname>", methods=['GET'])
def profile(yourname):
    return render_template('profile.html', name=yourname)

@app.route('/calc',methods=['GET','POST'])              
def calc():
    num1 = num2 = result = 0
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        result = num1 + num2 + 99
    return render_template('calc.html', sum=result, num1=num1, num2=num2)

if __name__ == "__main__":
    app.run(debug=True)