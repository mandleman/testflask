from flask import (Flask, send_file, url_for, jsonify, render_template)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/download')
def download():
    path = '123.png'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5050",debug=True)
