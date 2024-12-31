from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Welcome to My Flask App!</h1><p>Go to <code>/greet/yourname</code> to get a custom greeting.</p>"

@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello, {name}!</h1><p>Welcome to my Flask app.</p>"

if __name__ == '__main__':
    app.run(debug=True)
