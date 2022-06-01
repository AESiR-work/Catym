from flask import Flask, redirect, render_template, request, redirect
app = Flask(__name__,template_folder='templates')
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)