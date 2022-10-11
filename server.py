from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = "counter123assignment098"  # Change the secret key so each assignment is unique.

@app.route('/', methods=['GET'])
def counter_up():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/plus2', methods=['POST'])
def increase_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset_counter():
    session.clear()
    return redirect('/')

@app.route('/custom_increase', methods=['POST'])
def custom_up():
    holder = int(request.form['count_amount'])
    if holder >=1:
        session['counter'] = session['counter'] + (holder - 1)
        return redirect('/')
    else:
        return redirect('/')

if __name__== "__main__":  # lines 10 and 11 are required on all server.py files and will not run without them.
    app.run(debug=True)

# For macs, remember to add port = 5001 << something like this check the platform