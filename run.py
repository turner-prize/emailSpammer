from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
      result = request.form
      print (result)
      print (result['emailAddress'])
      return render_template("index.html")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)