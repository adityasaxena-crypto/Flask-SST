from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Information.html')
def page1():
    return render_template('Information.html')

@app.route('/Architecture.html')
def page2():
    return render_template('Architecture.html')

@app.route('/Publication.html')
def page3():
    return render_template('Publication.html')

if __name__ == '__main__':
    app.run(debug=True)