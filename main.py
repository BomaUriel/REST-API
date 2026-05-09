from flask import Flask   
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

db = SQLAlchemy(app)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            
        }



# Create Routes
@app.route("/")
def home():
    return "Hello!"





if __name__ == "__main__":
    app.run(debug=True)