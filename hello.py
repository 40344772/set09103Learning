from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "The default, 'root' route"

@app.route('/hello/')
def hello():
	return "Hello Napier!!! :D"

@app.route('/goodbye/')
def goodbye():
	return "Goodbye cruel world :("

@app.errorhandler(404)
def page_not_found(error):
	return "This is not the page you are looking for", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

