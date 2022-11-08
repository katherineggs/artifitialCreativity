from flask import Flask, render_template

#setting up the webpage service
app = Flask(__name__)

#here you can add routes
@app.route('/', methods =['GET', 'POST'])
def index():
    return render_template("index.html")

    
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)