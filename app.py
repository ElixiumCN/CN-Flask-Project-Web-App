from flask import Flask
from views import views
# we import our views from our views file

app = Flask(__name__)
# we instantiate the app object

# create application with Flask class.

app.register_blueprint(views)
# we register the views Blueprint

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# running the application

# if the flask app is actioned on this global code space
# then run it.