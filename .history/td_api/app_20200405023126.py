from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from oauth2 import routes
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://quickbooksuser:quickbookspassword@localhost/quickbooks-postgres'
# db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "sup"

app.register_blueprint(
    routes.oauth2_routes)

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8080)