from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', name="kuldeep")

app.run(debug=True)