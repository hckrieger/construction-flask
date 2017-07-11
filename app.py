from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/contact')
def contact():
	return render_template('contact.html')

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.config['DEBUG'] = True
	app.run()