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
        #for i in username:
        if username == '':
            error_user = "That's not a valid username"
            #return render_template('signup.html', error_user=error_user)

        #for i in password:
        if password == '':
            error_pass = "That's not a valid password"
            #return render_template('signup.html', error_user=error_user, error_pass=error_pass)

        if verify == '':
            error_verify = "Passwords don't match"
            #return render_template('signup.html', error_user=error_user, error_pass=error_pass, error_verify=error_verify)

        for i in email:
            if i == '@':
                error_email = 'Not valid email'
                return render_template('signup.html', error_user=error_user, error_pass=error_pass,
                                       error_verify=error_verify, error_email=error_email)


        #return render_template('signup.html', username=username, password=password, verify=verify)
    return render_template('signup.html', error_user=error_user, error_pass=error_pass)


app.run()
