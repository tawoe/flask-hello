from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
	return 'Hello World!'

@app.route('/whoever')
def hello_whoever():
	return f'Hello {os.getenv("WHOEVER")}!'

@app.route('/myoptions')
def hello_myoptions():
	return f'Hello {os.getenv("MYOPTIONS")}!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.getenv('FLASK_PORT', 8080))
