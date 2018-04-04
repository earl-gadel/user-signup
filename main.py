from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    if username == password == verify == '':
    #error displayed when user leaves any of the following fields empty: username, password, verify password
        error = "Please fill in this field"
        return redirect("/?error=" + error)
    return render_template('signup.html')


app.run()
