from flask import Flask, render_template

#initialization
app = Flask(__name__)

#configuration
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.gitignore', 'readme.md']
app.config['FREEZER_RELATIVE_URLS'] = True

#controllers
@app.route("/")
def index():
    return render_template('internet-of-things-2018.html')

@app.route("/archive.html")
def archive():
    return render_template('archive.html')

@app.route("/compact-living.html")
def compact():
    return render_template('compact-living.html')

@app.route("/internet-of-things-2018.html")
def iot():
    return render_template('internet-of-things-2018.html')

@app.route("/about-me.html")
def about():
    return render_template('about-me.html')

@app.route("/jupyter-css.html")
def jupyter_css():
    return render_template('jupyter-css.html')

#launch
if __name__ == "__main__":
    app.run(debug=True)
