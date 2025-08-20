from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form['username']
    user_age = request.form['userage']
    return render_template('greet.html', name=user_name, age=user_age)

if __name__ == "__main__":
    app.run(debug=True)
