from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __getenv__ import return_env


db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:{}@{}:{}/postgres".format(return_env("SUPABASE_KEY"), return_env("SUPABASE_URL"), return_env("SUPABASE_PORT"))

db.init_app(app)

class SupaBase(db.Model):
    userkey = db.Column(db.String, primary_key=True)
    