from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def flask_mongodb_atlas():    
    return render_template('index.html')

@app.route("/procesarImg")
def procesarImg():
    return render_template("Upload.html")

@app.route("/procesarImg2")
def procesarImg2():
    return render_template("form.html")

if __name__ == '__main__':
    app.run(port=8000)