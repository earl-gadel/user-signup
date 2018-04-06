from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        if username == '':
            error_user = "That's not a valid username"

        elif password == '':
            error_pass = "That's not a valid password"

            return render_template('signup.html', error_user=error_user, error_pass=error_pass)
        #elif len(password) < 3 or len(password) > 20:
            #error_pass = "That's not a valid password"
            #return render_template('signup.html', error_pass=error_pass)
        #elif verify == '':
            #error_verify = "Passwords don't match"
            #return render_template('signup.html', error_verify=error_verify)


        #return render_template('signup.html', username=username, password=password, verify=verify)
    return render_template('signup.html')

app.run()
