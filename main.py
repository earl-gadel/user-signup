from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = 't'#request.form['password']
        verify = 't' #request.form['verify']
        if username == '':

    #error displayed when user leaves any of the following fields empty: username, password, verify password
            error = "Please fill in this field"
            return render_template('signup.html', error=error)
        return render_template('signup.html', username=username, password=password, verify=verify)
    return render_template('signup.html')

app.run()
