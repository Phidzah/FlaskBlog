from flask import Flask, render_template

app = Flask(__name__)

# in Jinja templating you can use filters on the information that you pass
# Examples of such filters are:
# {{ name|capitalize}} to Capitalize the first letter of name
# {{ name|upper}} to convert the name to Uppercase
# {{ name|lower}} to convert the name to Lowercase
# {{ stuff|safe}} safe is used to pass html (only done when you know its you who is passing safe html tags)
# {{ stuff|striptags}} maybe in comments that are to be stored in a database to deter html injection
# {{ stuff|trim}} remove trailing spaces from the end of string variable
# {{ stuff|title}} Capitalize the first letter of every word in the stuff variable

# Jinja also allows us to pass variables, lists and dictionaries to our html templates
@app.route('/')
def index():
	username = "phidza"
	stuff = "This is a <h1>Heading 1 text</h1>"
	list_of_favourites = ['Pizza','Cheese', 'Sadza and Gango', 'Madora', 'Beer',90]
	return render_template('index.html',
		username=username,
		stuff=stuff,
		list_of_favourites=list_of_favourites)

# localhost:5000/user/Phillip
@app.route("/user/<name>")
def user(name):
	return render_template('user.html', username=name)


# Error handling is something that is important and should be done
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'),500

if '__name___' == '__main__':
	app.run(debug=True)