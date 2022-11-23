from flask import Flask, render_template, request

#setting up the webpage service
app = Flask(__name__)

#here you can add routes
@app.route('/', methods =['GET', 'POST'])
def index():
  if request.method=='POST':
    input = str(request.form['w3review'])
    
    song = input + " bien y tu" # generate(input)
    


    # call func
    return render_template("index.html", song= song)
  else:
    return render_template('index.html', song="")
    
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)