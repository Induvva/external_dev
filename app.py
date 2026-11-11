from flask import Flask, request, render_template, redirect, url_for
app=Flask(__name__)
@app.route('/')
def index():
    return <center>Welcome<br><a href='/register'>Register</a><br></center>
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('success', username=username))
    return render_template('register.html')
@app.route('/success/<username>/<email>/<roll_no>')
def success(username, email, roll_no):
    return render_template('success.html', user=username, email=email, roll_no=roll_no)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    