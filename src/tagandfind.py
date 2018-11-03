from flask import Flask, render_template
app = Flask(__name__, template_folder='assets/templates')


@app.route('/')
def render_static():
    return render_template('tag.html')
