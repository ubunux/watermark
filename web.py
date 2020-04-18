# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import flash, get_flashed_messages
from watermark import Watermark

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def onpost():
    text = request.form.get('text', type = str, default = None)
    if not text:
        flash("Watermark text cannot be NULL")
        return render_template("index.html")
    watermark = Watermark()
    watermark.text = text
    watermark.draw()
    with open(watermark.output, "rb") as image:
        resp = Response(image.read(), mimetype="image/jpeg")
    return resp

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001)
