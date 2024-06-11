from flask import Flask, render_template

app = Flask(__name__)


@app.route('/world')
def get_hello_world():
    return "Hello World!"


@app.route('/mth')
def get_hello_mth():
    return "Hello Minn Thiha!"


@app.route('/html')
def get_html():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
