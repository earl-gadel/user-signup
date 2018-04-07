from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST', 'GET'])
def index():
    error_user = ''
    error_pass = ''
    error_verify = ''
    error_email = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        for i in username:
            if i == '':
                error_user = "That's not a valid username"
            elif i == ' ':
                error_user = "That's not a valid username"

        if len(username) < 3 or len(username) > 20:
            error_user = "That's not a valid username"

        for i in password:
            if i == '':
                error_pass = "That's not a valid password"
            elif i == ' ':
                error_pass = "That's not a valid password"

        if len(password) < 3 or len(password) > 20:
            error_pass = "That's not a valid password"

        if verify != password:
            error_verify = "Passwords don't match"

        for i in email:
            if '@' not in email and '.' not in email:
                error_email = 'Not valid email'
        return render_template('signup.html', error_user=error_user, error_pass=error_pass,
                                       error_verify=error_verify, error_email=error_email, username=username, email=email)


        #return render_template('signup.html', username=username, password=password, verify=verify)
    return render_template('signup.html')


app.run()
