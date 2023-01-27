import flask 
from flask import Flask,render_template
import os
app = Flask(__name__, template_folder='templates', 
static_folder='static')


@app.route('/')
def t():
    return render_template("web.html")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
