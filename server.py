from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("survey.html") 

@app.route('/process', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['dojo_location'] = request.form['dojo_Location']
    session['favorite_language'] = request.form['favorite_Language']
    session['comments'] = request.form['comment']
    return redirect('/')

@app.route('/result')
def show_user():
    return render_template('show.html')

if __name__=="__main__":   
    app.run(debug=True) 