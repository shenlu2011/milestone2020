from flask import Flask, render_template, request, redirect


app = Flask(__name__, static_url_path='/static', static_folder="static")

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/taxi')
def taxi():
  return render_template('taxi.html')


if __name__ == '__main__':
  app.run(debug=True)